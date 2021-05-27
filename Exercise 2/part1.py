import sys
from math import ceil
from math import sqrt

def readFile():
    filename=sys.argv[1]
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


def sortMbr(mbr):
    r=len(mbr)
    n=int(1024/36)
    P=ceil(r/n)
    S=int(ceil(sqrt(P)))
    mbr.sort(key=lambda x:x[1])
    for i in range(S-1):
        l=mbr[i*S*n : (i+1)*S*n]
        l.sort(key=lambda x : x[3])
        mbr[i*S*n : (i+1)*S*n]=l
        
    l=mbr[(S-1)*S*n : ]
    l.sort(key=lambda x : x[3])
    mbr[(S-1)*S*n : ]=l


def split(mbr):
    r=len(mbr)
    n=int(1024/36)
    P=ceil(r/n)    
    newNodes=[]
    for i in range(P-1):
        node=mbr[i*n : (i+1)*n][:]
        newNodes.append(node)

    node=mbr[(P-1)*n : ][:]
    newNodes.append(node)
    return newNodes


def addNodeIds(newNodes, n):
    for i in range(len(newNodes)):
        newNodes[i].insert(0, i+n)


def convertToMbr(nodes):
    newMBR=[]    
    for i in range(len(nodes)):
        newMbr=[nodes[i][0]]
        x_low=nodes[i][1][1]
        x_high=nodes[i][1][2]
        y_low=nodes[i][1][3]
        y_high=nodes[i][1][4]
        for j in range(2, len(nodes[i])):
            x_low=min(x_low, nodes[i][j][1])
            x_high=max(x_high, nodes[i][j][2])
            y_low=min(y_low, nodes[i][j][3])
            y_high=max(y_high, nodes[i][j][4])
            
        newMbr.append(x_low)
        newMbr.append(x_high)
        newMbr.append(y_low)
        newMbr.append(y_high)
        newMBR.append(newMbr)       
    return newMBR


def findAvgArea(mbr):
    areaSum=0
    for i in range(len(mbr)):
        x_low=mbr[i][1]
        x_high=mbr[i][2]
        y_low=mbr[i][3]
        y_high=mbr[i][4]   
        areaSum=areaSum + (x_high - x_low)*(y_high - y_low)
    
    return areaSum/len(mbr)

def main():
    mbr=readFile()
    nodes=[]
    info=[]
    while len(mbr) > 1:
        sortMbr(mbr)
        newMBR=split(mbr)
        addNodeIds(newMBR, len(nodes))
        nodes.extend(newMBR)
        mbr=convertToMbr(newMBR)
        a=findAvgArea(mbr)
        info.append([a, len(mbr)])
    
    print("Height: "+str(len(info)))
    for i in range(len(info)):
        print("level "+str(i)+" : average area = " + str(info[len(info) - 1 - i][0]) + " num of nodes = " + str(info[len(info) - 1 - i][1]))

    outfile=open("rtree.txt", "w")
    outfile.write(str(nodes[len(nodes) - 1][0]) + "\n")
    outfile.write(str(len(info)) + "\n")
    for i in range(len(nodes) - 1, -1, -1):
        outfile.write(str(nodes[i][0]) + ","+str((len(nodes[i]) - 1)))
        for j in range(1, len(nodes[i])):
            outfile.write(",("+str(nodes[i][j][0]) + "\t"+str(nodes[i][j][1]) + "\t"+str(nodes[i][j][2]) + "\t"+str(nodes[i][j][3]) + "\t"+str(nodes[i][j][4]) + ")")
        outfile.write("\n")
    outfile.close()

main()
