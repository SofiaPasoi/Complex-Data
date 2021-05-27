import heapq 
import time
import sys
        
def part2(k):
    start_time = time.time()
    infile = open("males_sorted")
    lines = infile.readlines()
    dictionary = {}
    
    for line in lines:
        line = line.split(",")
        
        if int(line[1]) >= 18 and line[8].startswith(" Married") == False:
            age = int(line[1])
            instanceWeight = float(line[25])
            code = int(line[0])
            dictionary[age] = dictionary.get(age, []) + [[code, instanceWeight]]
    
    infile.close()
    
    heap = []
    heapq.heapify(heap)
    
    infile = open("females_sorted")
    lines = infile.readlines()
    for line in lines:
        line = line.split(",")
        
        if int(line[1]) >= 18 and line[8].startswith(" Married") == False:
            age = int(line[1])
            instanceWeight = float(line[25])
            code = int(line[0])
            
            maleList = dictionary.get(age, [])
            
            for male in maleList:
                sumInstanceWeight = instanceWeight + male[1]
                pair = str(male[0]) +","+str(code)
                join = [sumInstanceWeight, pair]
                if len(heap) < k:
                    heapq.heappush(heap, join)
                else:
                    heapSmallest = heapq.heappop(heap)
                    if heapSmallest[0] < join[0]:
                        heapq.heappush(heap, join)
                    else:
                        heapq.heappush(heap, heapSmallest)
    
    results = []
    while len(heap) > 0:
        heapSmallest = heapq.heappop(heap)
        results = [heapSmallest] + results
    

    
    for result in results:
        print("pair: "+result[1] +" score: "+str(result[0]))
    print("--- %s seconds ---" % (time.time() - start_time))

    
    
k = int(sys.argv[1])
part2(k)
