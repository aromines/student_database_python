#Team 1: Samantha Davis, Anya Romines, Tianle Lila Zeng

#globals
gradebook = {}  # a global dictionary.  Key:name  value:scores.
count =0
total=0
countA=0
countB=0
countC=0
countD=0

def compute_score(scores):
    hwscore = scores[0]+scores[1]+scores[2]
    examscore=scores[3]+scores[4]

    finalscore=hwscore*0.4+examscore*0.2

    return round(finalscore,2)

def compute_grade(sco):
    global countA, countB, countC, countC, countD
    if(sco>=90):
        grade ='A'
        countA+=1
    elif(sco>=80):
        grade ='B'
        countB+=1
    elif(sco>=70):
        grade= 'C'
        countC+=1
    else:
        grade ='D'
        countD+=1
    
    return grade

def parse_line(line):    
    inputstring=line.split()
    name=inputstring[0]
    scorestrings=inputstring[1:]
    scores=[]
    for score in scorestrings:
        scores.append(int(score))
        
    return name, scores

def process_line(linestring):
    global count, total
    name,scores = parse_line(linestring)

    score = compute_score(scores)
    
    grade = compute_grade(score)
    
    scores.append(score)
    scores.append(grade)

    count+=1
    total+=score

    return name, scores

def compute_mean():
    global total, count
    average=0

    if(count!=0):
        average=total/count
    
    return average

def enter_data():
    global count
    global gradebook

    line=input("\nPlease enter your name and scores:")
    name,scores = process_line(line)
    gradebook[name]=scores
    print('\n'+name,scores)

def display_data():
    global gradebook

    if bool(gradebook):  #check if empty
        print("\nThe students and their grades are as follows:")
        header = "Name            HW1   HW2   HW3   Exam1 Exam2 Score Grade"
        print(header)
        for name in gradebook.keys():
            strings=[name]
            for element in gradebook[name]:
                strings.append(str(element))
            print("{:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(*strings))             
    else:
        print('\nNo data in gradebook.')

def display_stats():
    print("\nThe total number of students is: %d \nThe average score is: %.2f \nThe standard deviation is: %.2f"%(count,compute_mean(),compute_standard_deviation()))
    print("The number of each grade is:\nA: %d\nB: %d\nC: %d\nD: %d"%(countA,countB,countC,countD))
    print("The median is: %d\nThe mode is: %s"%(compute_median(),compute_mode()))

def reset_data():
    global count, countA,countB,countC,countD,total
    global gradebook
    gradebook.clear()
    count =0 
    total=0
    countA=0
    countB=0
    countC=0
    countD=0

    print('\nData reset, ready for new input.')

def read_data():
    lines = []        
    datafile = open('scores.txt') #scores.txt must be in same folder as project run path
    lines = datafile.readlines()
    datafile.close()

    for l in lines:
        name,scores = process_line(l)
        gradebook[name]=scores
        print(name,scores)

def write_data():
    global gradebook

    if bool(gradebook):
        outputfile = open('outputs.txt', 'w')
        for name in gradebook.keys():
            strings=[name]
            for element in gradebook[name]:
                strings.append(str(element))
            for i in strings:
                outputfile.write(i + " ")
            outputfile.write("\n")
        outputfile.close()
        print('\ngradebook data written to outputs.txt.') #outputs.txt will go in same folder as project run path
    else:
        print('\nNo valid data to write.')

def search():
    key = input('\nEnter name')
    if key in gradebook.keys():
        header = "\nName            HW1   HW2   HW3   Exam1 Exam2 Score Grade"
        print(header)
        strings=[key]
        for element in gradebook[key]:
            strings.append(str(element))
        print("{:<15} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(*strings))        
    else:
        print('\nNo student with that name.')

def search_grade(): #search by grade extra credit
    global gradebook
    nameswithgrade = []
    searched_grade = input('\nProvide grade')
    for name in gradebook.keys():
        for values in gradebook[name]:
            if values == searched_grade:
                nameswithgrade.append(name)            
    if nameswithgrade == []:
        print('\nNo students with that grade.')
    else:        
        print('\nStudents with that grade:\n%s'%(nameswithgrade))        

def compute_standard_deviation():
    mean = compute_mean()
    delta_squares=[]

    for student in gradebook.keys():
        delta_squares.append((gradebook[student][5]-mean)**2)
    
    if len(delta_squares) <= 1:
        standard_deviation=0
    else:
        standard_deviation=(sum(delta_squares)/(len(delta_squares)-1))**0.5

    return standard_deviation

def compute_median(): #compute median extra credit
    median = 0
    if bool(gradebook):    
        scores=[]    
        for student in gradebook.keys():
            scores.append(gradebook[student][5])

            scores.sort()

            size=len(scores)
            if size%2 == 0:
                index= int (size/2)
                median=(scores[index-1]+scores[index])/2
            else:
                index=int ((size-1)/2)
                median=scores[index]     
    return median        

def compute_mode(): #compute mode extra credit
    modes = 0
    if bool(gradebook):
        scores=[]
        for student in gradebook.keys():
            scores.append(gradebook[student][5])
        
        modes= []   
        counts={}

        for score in scores:
            counting = scores.count(score)
            counts[counting]=score
        
        max_count=max(counts.keys())
        
        for score in scores:
            if scores.count(score)==max_count and score not in modes:
                modes.append(score)
            else:
                continue

    return modes
    
#main body
quit = False
while not quit :   #an infinite loop that will stop only when quit is True
    print("\n1 read 2 enter 3 display 4 stats 5 save 6 reset 7 search 8 exit ")
    choice = int(input('Enter 1, 2, 3, 4, 5, 6, 7, or 8'))
    if choice == 1:
        read_data()        
    elif choice == 2:
        enter_data()
    elif choice == 3:
        display_data()
    elif choice == 4:
        display_stats()
    elif choice == 5:
       write_data()       
    elif choice==6:
        reset_data()
    elif choice==7:
        print('\n1 name 2 grade')
        choice = int(input('enter 1 or 2'))
        if choice == 1:
            search()
        elif choice == 2:
            search_grade()
        else:
            print('enter 1 or 2')       
    elif choice==8:
        quit=True
    else:
        print('\nMust choose 1...8 Try again, please.')
