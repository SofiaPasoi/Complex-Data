import heapq 
import time
import sys
    
def part1():
    returnResults = 0
    infile1 = open("males_sorted")
    infile2 = open("females_sorted")
    turn = 0
    
    countMales = 1
    countFemales = 1
    
    dictionaryMale = {}
    dictionaryFemale = {}
    
    p1_cur = 0
    p1_max = 0
    p2_cur = 0
    p2_max = 0
    
    while True:
        line = infile1.readline()
        line = line.split(",")
        
        if int(line[1]) >= 18 and line[8].startswith(" Married") == False:
            age = int(line[1])
            instanceWeight = float(line[25])
            code = int(line[0])
            
            p1_cur = instanceWeight
            p1_max = instanceWeight
            dictionaryMale[age] = [[code, instanceWeight]]
            break
        
    while True:
        line = infile2.readline()
        line = line.split(",")
        
        if int(line[1]) >= 18 and line[8].startswith(" Married") == False:
            age = int(line[1])
            instanceWeight = float(line[25])
            code = int(line[0])
            
            p2_cur = instanceWeight
            p2_max = instanceWeight
            dictionaryFemale[age] = [[code, instanceWeight]]
            break

    T = p1_max + p2_max
    
    heap = []
    heapq.heapify(heap)
    
    while True:
        if turn%2 == 0:
            turn += 1
            while True:
                line = infile1.readline()
                if line == '':
                    break
                #    return []
                
                line = line.split(",")
                
                if int(line[1]) >= 18 and line[8].startswith(" Married") == False:
                    countMales += 1
                    age = int(line[1])
                    instanceWeight = float(line[25])
                    code = int(line[0])
                    
                    p1_cur = instanceWeight
                    dictionaryMale[age] = dictionaryMale.get(age, []) + [[code, instanceWeight]]
                    
                    values = dictionaryFemale.get(age, [])
                    break
        else:
            turn += 1
            while True:
                line = infile2.readline()
                if line == '':
                    break
                #    return []
                
                line = line.split(",")
                
                if int(line[1]) >= 18 and line[8].startswith(" Married") == False:
                    countFemales += 1
                    age = int(line[1])
                    instanceWeight = float(line[25])
                    code = int(line[0])
                    
                    p2_cur = instanceWeight
                    dictionaryFemale[age] = dictionaryFemale.get(age, []) + [[code, instanceWeight]]
                    
                    values = dictionaryMale.get(age, [])
                    break
            
        
        T = max(p1_max + p2_cur, p2_max + p1_cur)
        
        for value in values:
            sumInstanceWeight = (instanceWeight + value[1])*(-1)
            pair = str(value[0]) +","+str(code)
            join = [sumInstanceWeight, pair]
            heapq.heappush(heap, join)
        
        while len(heap) > 0:
            value = heapq.heappop(heap)
            if value[0]*(-1) >= T:
                yield value, countMales, countFemales
            else:
                heapq.heappush(heap, value)
                break
    yield []
 
k = int(sys.argv[1])
g = part1()
start_time = time.time()
for i in  range(k):
    result, countMales, countFemales = next(g)
    print("pair: "+result[1] +" score: "+str((-1)*result[0]))
print("--- %s seconds ---" % (time.time() - start_time))

print("countMales= "+str(countMales))
print("countFemales= "+str(countFemales))
print("countTotal= "+str(countMales+countFemales))
