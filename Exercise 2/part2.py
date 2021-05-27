import sys
from math import ceil
from math import sqrt

def readRTree(filename):
    rtree=[]
    infile=open(filename) 
    allLines=infile.readlines()
    root=int(allLines[0])
    levels=int(allLines[1])
    allLines=allLines[2:]   
    for line in allLines:
        line=line[:-1]
        line=line.split(',')
        mbr=[int(line[0]), int(line[1])]    
        for i in range(2,len(line)):
            line[i]=line[i][1:-1]
            toks=line[i].split('\t')
            toks[0]=int(toks[0])
            for j in range(1, 5):
                toks[j]=float(toks[j])
            mbr.append(toks)
            
        rtree.insert(0, mbr)
    infile.close()
    return rtree, root, levels


def readFile(filename):
    infile=open(filename)
    
    allLines=infile.readlines()
    mbr=[]
    
    for line in allLines:
        newMbr=line.split('\t')
        newMbr[0]=int(newMbr[0])
        
        for j in range(1, 5):
         
            newMbr[j]=float(newMbr[j])
            
        mbr.append(newMbr)
    infile.close()   
    return mbr

#elegxei ean to q periexei to mbr
def contains(q, mbr):
    if q[1] <= mbr[1] and q[2] >= mbr[2]:
        if q[3] <= mbr[3] and q[4] >= mbr[4]:
            return True
    return False


def intersects(q, mbr):    
    if q[2] < mbr[1]:
        return False
    if q[1] > mbr[2]:
        return False
    if q[4] < mbr[3]:
        return False
    if q[3] > mbr[4]:
        return False
    return True


def intersectionQuery(mbr, q):
    count=0
    for i in range(len(mbr)):
        if intersects(q, mbr[i])==True:
            count=count + 1
    return count


def insideQuery(mbr, q):
    count=0
    for i in range(len(mbr)):
        if contains(q, mbr[i])==True:
            count=count + 1 
    return count


def containmentQuery(mbr, q):
    count=0
    for i in range(len(mbr)):
        if contains(mbr[i], q)==True:
            count=count + 1
    return count


mylist=[]

def intersectionQueryRTree(rtree, n, q, currentLevel, treeLevel):
    global mylist
    count=0
        
    mylist.append(rtree[n])
    if currentLevel==treeLevel - 1: #4 levels: 0->root....3->leaves
        for i in range(rtree[n][1]):
            if intersects(q, rtree[n][i+2])==True:   
                count=count + 1
        return count
    else:
        for i in range(rtree[n][1]):
            if intersects(q, rtree[n][i+2])==True:
                m=rtree[n][i+2][0] 
                count=count + intersectionQueryRTree(rtree, m, q, currentLevel + 1, treeLevel)
        return count


def insideQueryRTree(rtree, n, q, currentLevel, treeLevel):
    global mylist
    count=0
    mylist.append(rtree[n])
    if currentLevel==treeLevel - 1:
        for i in range(rtree[n][1]):
            if contains(q, rtree[n][i+2])==True:   
                count=count + 1
        return count
    else:
        for i in range(rtree[n][1]):    
            if intersects(q, rtree[n][i+2])==True:
                m=rtree[n][i+2][0] 
                count=count + insideQueryRTree(rtree, m, q, currentLevel + 1, treeLevel)
        return count


def containmentQueryRTree(rtree, n, q, currentLevel, treeLevel):
    global mylist
    count=0
    mylist.append(rtree[n])
    if currentLevel==treeLevel - 1:
        for i in range(rtree[n][1]):    
            if contains(rtree[n][i+2], q)==True:
                count=count + 1
        return count
    else:
        for i in range(rtree[n][1]):
            if contains(rtree[n][i+2], q)==True:
                m=rtree[n][i+2][0] 
                count=count + containmentQueryRTree(rtree, m, q, currentLevel + 1, treeLevel)
        return count



mbr=readFile(sys.argv[1])
queries=readFile(sys.argv[2])
rt=sys.argv[3]

print("Queries: Intersection Inside Containment")
for i in range(len(queries)):
    count1=intersectionQuery(mbr, queries[i])
    count2=insideQuery(mbr, queries[i])
    count3=containmentQuery(mbr, queries[i])
    print(count1, count2, count3) #ta tupwnw wste na elegxw an oi times pou tha typwthoun parakatw einai idies

print("Rtree Queries: Intersection Inside Containment")
print("Every second number is nodes accessed")
rtree, root, levels = readRTree(rt)
    
for i in range(len(queries)):
    mylist=[]
    count1=intersectionQueryRTree(rtree, root, queries[i], 0, levels)
    len1=len(mylist)
    mylist=[]
    count2=insideQueryRTree(rtree, root, queries[i], 0, levels)
    len2=len(mylist)
    mylist=[]
    count3=containmentQueryRTree(rtree, root, queries[i], 0, levels)
    len3=len(mylist)
    mylist=[]
    print(count1, len1, count2, len2, count3, len3)

   

