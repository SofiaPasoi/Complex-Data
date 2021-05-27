#Pasoi Sofia, 2798
import heapq
import time
import sys

def readFile(filename):
    invertedFileDict = {}
    
    infile = open(filename)
    lines = infile.readlines()
    
    for i in range(len(lines)):
        line = lines[i].split('\t')
        allTags = line[2].split(':')
        tags = allTags[1].split(',')
        for j in  range(len(tags)):
            tag = tags[j].strip()
            value = invertedFileDict.get(tag, [])
            value.append(i)
            invertedFileDict[tag] = value
    
    heap = []
    heapq.heapify(heap)

    words = invertedFileDict.keys()
    for word in words:
        value = invertedFileDict.get(word)
        h = [len(value), word, value]
        heapq.heappush(heap, h)

    invertedFile = []
    keywordPositions = {}
    
    while(len(heap) > 0):
        h = heapq.heappop(heap)
        keywordPositions[h[1]] =  len(invertedFile)
        invertedFile.append(h)
    return invertedFile, lines, keywordPositions



def kwSearchRaw(searchTags, lines):
    results = []
    for i in range(len(lines)):
        line = lines[i].split('\t')
        allTags = line[2].split(':')
        tags = allTags[1].split(',')
        
        count = 0
        for j in range(len(tags)):
            tag = tags[j].strip()
            
            if tag in searchTags:
                count += 1
            
        if count == len(searchTags):
            results.append(lines[i])
    return results

def myMergeJoin(list1, list2):
    result = []
    i = 0
    j = 0
    while(i < len(list1) and j < len(list2)):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    
    return result

def kwSearchIF(searchTags, invertedFile, lines, keywordPositions):
    positions = []
    for i in range(len(searchTags)):
        positions.append(keywordPositions.get(searchTags[i]))
    
    positions.sort()
    resultFiles = invertedFile[positions[0]][2]
    for i in range(1, len(positions)):
        list2 = invertedFile[positions[i]][2]
        resultFiles = myMergeJoin(resultFiles, list2)
        if len(resultFiles) == 0:
            return []
    
    results = []
    for i in range(len(resultFiles)):
        results.append(lines[resultFiles[i]])

    return results


invertedFile, lines, keywordPositions = readFile('Restaurants_London_England.tsv')

print("number of keywords: "+str(len(invertedFile)))
frequencies = []
for i in  range(len(invertedFile)):
    frequencies.append(invertedFile[i][0])
    
print(frequencies)


searchTags = []
for i in range(1, len(sys.argv)):
    searchTags.append(sys.argv[i])

start_time = time.time()
results = kwSearchRaw(searchTags, lines)
end_time = time.time()
total = end_time - start_time
print("kwSearchRaw: " + str(len(results)) + " results, cost = " + str(total))
for i in range(len(results)):
    print(results[i])

kwRaw = len(results)

start_time = time.time()
results = kwSearchIF(searchTags, invertedFile, lines, keywordPositions)
end_time = time.time()
total = end_time - start_time
print("kwSearchIF: " + str(len(results)) + " results, cost = " + str(total))
for i in range(len(results)):
    print(results[i])

if len(results) != kwRaw:
    print("Something went wrong")
    
