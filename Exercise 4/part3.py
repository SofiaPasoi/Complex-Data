#Pasoi Sofia, 2798
import heapq
import time
import sys

def createGrid(filename):
    grid = [[[] for j in range(50)] for i in range(50)]
    
    infile = open(filename)
    lines = infile.readlines()
    
    X = []
    Y = []
    
    for i in range(len(lines)):
        line = lines[i].split('\t')
        location = line[1].split(':')
        coord = location[1].split(',')
        
        x = float(coord[0].strip())
        y = float(coord[1].strip())
        
        X.append(x)
        Y.append(y)
    
    minX = min(X)
    maxX = max(X)
    minY = min(Y)
    maxY = max(Y)
    
    stepX = (maxX - minX)/50
    stepY = (maxY - minY)/50
    
    for i in range(len(lines)):
        cellX = 0
        minCellx = minX
        maxCellx = minX + stepX
        
        cellY = 0
        minCelly = minY
        maxCelly = minY + stepY
        
        while cellX < 49:
            if X[i] < maxCellx:
                break
            minCellx = maxCellx
            maxCellx = maxCellx + stepX
            cellX = cellX + 1
        while cellY < 49:
            if Y[i] < maxCelly:
                break
            minCelly = maxCelly
            maxCelly = maxCelly + stepY
            cellY = cellY + 1  
        grid[cellX][cellY].append(i)
        
    
    
    return grid, minX, minY, maxX, maxY, lines



def createInvertedFile(filename):
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

def kwSpaSearchIF(areaMinX, areaMaxX, areaMinY, areaMaxY,searchTags, invertedFile, lines, keywordPositions):
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
        line = lines[resultFiles[i]].split('\t')
        location = line[1].split(':')
        coord = location[1].split(',')
        
        x = float(coord[0].strip())
        y = float(coord[1].strip())
        
        if x >= areaMinX and x <= areaMaxX and y >= areaMinY and y <= areaMaxY:
            results.append(lines[resultFiles[i]])

    return results


def kwSpaSearchRaw(areaMinX, areaMaxX, areaMinY, areaMaxY, searchTags, lines):
    results = []
    for i in range(len(lines)):
        line = lines[i].split('\t')
        location = line[1].split(':')
        coord = location[1].split(',')
        
        x = float(coord[0].strip())
        y = float(coord[1].strip())
        
        if x >= areaMinX and x <= areaMaxX and y >= areaMinY and y <= areaMaxY:
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

def kwSpaSearchGrid(areaMinX, areaMaxX, areaMinY, areaMaxY, grid, minX, minY, maxX, maxY, searchTags, lines):
    stepX = (maxX - minX)/50
    stepY = (maxY - minY)/50
    
    cellX = 0
    minCellx = minX
    maxCellx = minX + stepX
    
    cellY = 0
    minCelly = minY
    maxCelly = minY + stepY
    
    resultFiles = []

    for i in range(50):
        cellY = 0
        minCelly = minY
        maxCelly = minY + stepY
        for j in range(50):
            if areaMaxX < minCellx or areaMinX > maxCellx or areaMaxY < minCelly or areaMinY > maxCelly:
                minCelly = maxCelly
                maxCelly = maxCelly + stepY
                cellY = cellY + 1

            else:
                if areaMaxX >= maxCellx and areaMinX <= minCellx and areaMaxY >= maxCelly and areaMinY <= minCelly:
                    resultFiles.extend(grid[cellX][cellY])
                else:
                    for k in range(len(grid[cellX][cellY])):
                        r = grid[cellX][cellY][k]
                        
                        line = lines[r].split('\t')
                        location = line[1].split(':')
                        coord = location[1].split(',')
                        
                        x = float(coord[0].strip())
                        y = float(coord[1].strip())
                        
                        if x >= areaMinX and x <= areaMaxX and y >= areaMinY and y <= areaMaxY:
                            resultFiles.append(r)
                minCelly = maxCelly
                maxCelly = maxCelly + stepY
                cellY = cellY + 1
        minCellx = maxCellx
        maxCellx = maxCellx + stepX
        cellX = cellX + 1
    
    results = []
    for i in range(len(resultFiles)):
        line = lines[resultFiles[i]].split('\t')
        allTags = line[2].split(':')
        tags = allTags[1].split(',')
        
        count = 0
        for j in range(len(tags)):
            tag = tags[j].strip()
            
            if tag in searchTags:
                count += 1
            
        if count == len(searchTags):
            results.append(lines[resultFiles[i]])

    return results


grid, minX, minY, maxX, maxY, lines = createGrid('Restaurants_London_England.tsv')
invertedFile, lines, keywordPositions = createInvertedFile('Restaurants_London_England.tsv')

areaMinX = float(sys.argv[1])
areaMaxX = float(sys.argv[2])
areaMinY = float(sys.argv[3])
areaMaxY = float(sys.argv[4])

searchTags = []
for i in range(5, len(sys.argv)):
    searchTags.append(sys.argv[i])

start_time = time.time()
results = kwSpaSearchRaw(areaMinX, areaMaxX, areaMinY, areaMaxY, searchTags, lines)
end_time = time.time()
total = end_time - start_time

print("kwspaSearchRaw: " + str(len(results)) + " results, cost = " + str(total))

for i in range(len(results)):
    print(results[i])

kwSpaRaw = len(results)

start_time = time.time()
results = kwSpaSearchIF(areaMinX, areaMaxX, areaMinY, areaMaxY,searchTags, invertedFile, lines, keywordPositions)
end_time = time.time()
total = end_time - start_time

print("#####################################################################################################################################")
print("#####################################################################################################################################")
print("#####################################################################################################################################")
print("#####################################################################################################################################")
print("#####################################################################################################################################")

print("kwSpaSearchIF: " + str(len(results)) + " results, cost = " + str(total))

for i in range(len(results)):
    print(results[i])
    
kwSpaIF = len(results)  
    
start_time = time.time()
results = kwSpaSearchGrid(areaMinX, areaMaxX, areaMinY, areaMaxY, grid, minX, minY, maxX, maxY, searchTags, lines)
end_time = time.time()
total = end_time - start_time

print("#####################################################################################################################################")
print("#####################################################################################################################################")
print("#####################################################################################################################################")
print("#####################################################################################################################################")

print("kwSpaSearchGrid: " + str(len(results)) + " results, cost = " + str(total))

for i in range(len(results)):
    print(results[i])
  
if len(results) != kwSpaRaw:
    print("Something went wrong")
    
if len(results) != kwSpaIF:
    print("Something went wrong")
    
if kwSpaIF != kwSpaRaw:
    print("Something went wrong")
