def sortFile(filename, resultFilename):
    infile = open(filename, "r")
    outfile = open(resultFilename, "w")

    lines = infile.readlines()
    firstLine = lines[0]

    del lines[0]
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
    lines.sort(key=lambda x: x[0])

    outfile.write(firstLine)
    for i in range(len(lines)):
        lines[i] = "\t".join(lines[i])
        outfile.write(str(lines[i]))
    lines.insert(0, firstLine)
    outfile.close()
    infile.close()

def mergeSortQ11(filename1, filename2, filename3):
    infile1 = open(filename1, "r")
    infile2 = open(filename2, "r")
    outfile = open(filename3, "w")

    line1 = infile1.readline()
    line2 = infile2.readline()
    
    toks1 = line1.split("\t")
    toks2 = line2.split("\t")   
    result = toks1[2] +"\t" + toks2[1] +"\n"
    outfile.write(result)
    
    line1 = infile1.readline()
    line2 = infile2.readline()
    
    while line1 != "" and line2 != "":
        toks1 = line1.split("\t")
        toks2 = line2.split("\t")

        if toks1[0] == toks2[0]:
            directors = toks2[1].split(",")
            if len(directors) > 1:
                result = toks1[2] +"\t" + toks2[1] +"\n"
                outfile.write(result)
            line1 = infile1.readline()
            line2 = infile2.readline()
        elif toks1[0] < toks2[0]:
            line1 = infile1.readline()
        else:
            line2 = infile2.readline()
    infile1.close()
    infile2.close()
    outfile.close()
    return

def mergeSortQ12(filename1, filename2, filename3):
    infile1 = open(filename1, "r")
    infile2 = open(filename2, "r")
    outfile = open(filename3, "w")

    line1 = infile1.readline()
    line2 = infile2.readline()
    
    toks1 = line1.split("\t")
    toks2 = line2.split("\t")   
    result = toks1[2] +"\t" + toks2[1] +"\t" + toks2[2] +"\n"
    outfile.write(result)
    
    line1 = infile1.readline()
    line2 = infile2.readline()
    
    while line1 != "" and line2 != "":
        toks1 = line1.split("\t")
        toks2 = line2.split("\t")

        if toks1[0] == toks2[0]:
            try:
                episode_number = int(toks2[3])
                if episode_number == 1:
                    result = toks1[2] +"\t" + toks2[1] +"\t" + toks2[2] +"\n"
                    outfile.write(result)
                line1 = infile1.readline()
                line2 = infile2.readline()
            except ValueError:
                line1 = infile1.readline()
                line2 = infile2.readline()
            
        elif toks1[0] < toks2[0]:
            line1 = infile1.readline()
        else:
            line2 = infile2.readline()
    infile1.close()
    infile2.close()
    outfile.close()
    return

def mergeSortQ13(filename1, filename2, filename3):
    infile1 = open(filename1, "r")
    infile2 = open(filename2, "r")
    outfile = open(filename3, "w")
#to filename1 einai to basics
    line1 = infile1.readline()
    line2 = infile2.readline()
    
    line1 = infile1.readline()
    line2 = infile2.readline()
    
    outfile.write("primaryTitle\n")

    while line1 != "" and line2 != "":
        toks1 = line1.split("\t")
        toks2 = line2.split("\t")

        if toks1[0] == toks2[0]:
            line1 = infile1.readline()
            line2 = infile2.readline()
        elif toks1[0] < toks2[0]:
            result = toks1[2]+"\n"
            outfile.write(result)
            line1 = infile1.readline()
        else:
        #exw rating tconst < basic tconst: kanonika den prepei na ginetai
            line2 = infile2.readline()
            
    while line1 != "":
        toks1 = line1.split("\t")
        result = toks1[2]+"\n"
        outfile.write(result)
        line1 = infile1.readline()
    infile1.close()
    infile2.close()
    outfile.close()
    return

def h(x):
    if x <= 1.0:
        return 0
    elif x <= 2.0:
        return 1
    elif x <= 3.0:
        return 2
    elif x <= 4.0:
        return 3
    elif x <= 5.0:
        return 4
    elif x <= 6.0:
        return 5
    elif x <= 7.0:
        return 6
    elif x <= 8.0:
        return 7
    elif x <= 9.0:
        return 8
    elif x <= 10.0:
        return 9
    
def hashingQ21():
    counts = [0 for i in range(10)]
    infile = open("title.ratings_sorted.tsv", "r")

    lines = infile.readlines()
    

    del lines[0]
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        avgRating = float(lines[i][1])
        pos = h(avgRating)
        
        counts[pos] = counts[pos]+1
    
    x = 0.1
    y = 1.0
    for i in range(10):
        print(str(x) + "-"+str(y) + " : "+ str(counts[i]))
        x = x+1
        y = y+1
        
    infile.close()
    
def sortingQ21():
    counts = [0 for i in range(10)]
    infile = open("title.ratings_sorted.tsv", "r")

  
    lines = infile.readlines()
    

    del lines[0]
    for i in range(len(lines)):
        lines[i] = lines[i].split("\t")
        lines[i][1] = float(lines[i][1])
    lines.sort(key=lambda x: x[1])

    pos = 0
    maxRating = 1
    for i in range(len(lines)):
        
        avgRating = float(lines[i][1])
        
        if(avgRating > maxRating):
            pos = pos + 1
            maxRating = maxRating + 1
        
        counts[pos] = counts[pos]+1
    
    x = 0.1
    y = 1.0
    for i in range(10):
        print(str(x) + "-"+str(y) + " : "+ str(counts[i]))
        x = x+1
        y = y+1
    infile.close()

def mergeSortQ22(filename1, filename2):
    infile1 = open(filename1, "r")
    infile2 = open(filename2, "r")
    
#to filename1 einai to basics
    line1 = infile1.readline()
    line2 = infile2.readline()
    
    line1 = infile1.readline()
    line2 = infile2.readline()
    
    yearsRatings = {}
    #{key:[sum_average_rating, count]}

    while line1 != "" and line2 != "":
        toks1 = line1.split("\t")
        toks2 = line2.split("\t")

        if toks1[0] == toks2[0]:
            startYear = toks1[5]
            value = yearsRatings.get(startYear, 3000)
            averageRating = float(toks2[1])
            if value == 3000:
                yearsRatings.update({startYear: [averageRating, 1]})
            else:
                value[0] = value[0] + averageRating
                value[1] = value[1] + 1
                yearsRatings.update({startYear: value})
                
            line1 = infile1.readline()
            line2 = infile2.readline()
        elif toks1[0] < toks2[0]:
            line1 = infile1.readline()
        else:
        #exw rating tconst < basic tconst: kanonika den prepei na ginetai
            line2 = infile2.readline()
    
    startYears = list(yearsRatings.keys())
    startYears.sort()
    
    for i in range(len(startYears)):
        startYear = str(startYears[i])
        value = yearsRatings.get(startYear)
        avgRating = value[0]/value[1]
        print("year: "+ startYear + " average rating: "+ str(avgRating))
    
    infile1.close()
    infile2.close()
    return   


#sortFile("crew.tsv","crew_sorted.tsv")
#sortFile("episodes.tsv","episodes_sorted.tsv")
#sortFile("principals.tsv","principals_sorted.tsv")
#sortFile("ratings.tsv","ratings_sorted.tsv")
#sortFile("titleakas.tsv","titleakas_sorted.tsv")
#sortFile("titlebasics.tsv","titlebasics_sorted.tsv")
#sortFile("name.tsv","name_sorted.tsv")

mergeSortQ11("title.basics_sorted.tsv", "title.crew_sorted.tsv", "output11.tsv")
mergeSortQ12("title.basics_sorted.tsv", "title.episode_sorted.tsv", "output12.tsv")
mergeSortQ13("title.basics_sorted.tsv", "title.ratings_sorted.tsv", "output13.tsv")

from timeit import default_timer as timer

start = timer()
hashingQ21()
end = timer()
print(end - start)
start = timer()
sortingQ21()
end = timer()
print(end - start)


mergeSortQ22("title.basics_sorted.tsv", "title.ratings_sorted.tsv")
