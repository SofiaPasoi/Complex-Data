#Pasoi Sofia, 2798
import heapq
import time
import sys

def readFile(filename):
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
        
    
    print("Bounds: " + str(minX) + " " + str(maxX) + " " + str(minY) + " " + str(maxY))
    print("Widths: " + str(maxX - minX) + " " + str(maxY - minY))
    for i in range(50):
        for j in range(50):
            if len(grid[i][j]) > 0:
                print(str(i) + " " + str(j) + " " + str(len(grid[i][j])))

    return grid, minX, minY, maxX, maxY, lines



def spaSearchRaw(areaMinX, areaMaxX, areaMinY, areaMaxY, lines):
    results = []
    for i in range(len(lines)):
        line = lines[i].split('\t')
        location = line[1].split(':')
        coord = location[1].split(',')
        
        x = float(coord[0].strip())
        y = float(coord[1].strip())
        
        if x >= areaMinX and x <= areaMaxX and y >= areaMinY and y <= areaMaxY:
            results.append(lines[i])
    return results

def spaSearchGrid(areaMinX, areaMaxX, areaMinY, areaMaxY, grid, minX, minY, maxX, maxY, lines):
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
        results.append(lines[resultFiles[i]])

    return results


grid, minX, minY, maxX, maxY, lines = readFile('Restaurants_London_England.tsv')

areaMinX = float(sys.argv[1])
areaMaxX = float(sys.argv[2])
areaMinY = float(sys.argv[3])
areaMaxY = float(sys.argv[4])


start_time = time.time()
results = spaSearchRaw(areaMinX, areaMaxX, areaMinY, areaMaxY, lines)
end_time = time.time()
total = end_time - start_time

print("spaSearchRaw: " + str(len(results)) + " results, cost = " + str(total))
'''
for i in range(len(results)):
    print(results[i])
'''
kwRaw = len(results)

start_time = time.time()
results = spaSearchGrid(areaMinX, areaMaxX, areaMinY, areaMaxY, grid, minX, minY, maxX, maxY, lines)
end_time = time.time()
total = end_time - start_time

print("spaSearchGrid: " + str(len(results)) + " results, cost = " + str(total))
'''
for i in range(len(results)):
    print(results[i])
'''
if len(results) != kwRaw:
    print("Something went wrong")

