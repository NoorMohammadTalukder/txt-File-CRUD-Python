#--------------- add course function
def addCourse():
    findStatus=False

    print ("Enter Course Id:")
    courseId=input()

    print ("Enter Course name:")
    courseName=input()

    print ("Enter Pre Requite Course Id:")
    coursePreRequisite=input()
    if(coursePreRequisite==""):
        coursePreRequisite="N/A"
        print ("Enter Course Description:")
        courseDescription=input()
    
        with open("store.txt", "a") as file:
            file.write("\nId:"+ courseId +"--")
            file.write("Course Name:"+ courseName+"--")
            file.write("Pre Requite Course Id:"+ coursePreRequisite+"--")
            file.write("Description:"+ courseDescription)
    else:
        findingText="Id:"+coursePreRequisite
        
        with open("store.txt", 'r') as fp:
            for l_no, line in enumerate(fp):
                if findingText in line:
                    # print('string found in a file')
                    # print('Line Number:', l_no)
                    # print('Line:', line)
                    findStatus=True
                    print ("Enter Course Description:")
                    courseDescription=input()
    
                    with open("store.txt", "a") as file:
                        file.write("\nId:"+ courseId +"--")
                        file.write("Course Name:"+ courseName+"--")
                        file.write("Pre Requite Course Id:"+ coursePreRequisite+"--")
                        file.write("Description:"+ courseDescription)
                        break
            if(findStatus!=True):
                print("Pre Requisite Not exist \n Add the Course first")       
               

    # print ("Enter Course Description:")
    # courseDescription=input()
    
    # with open("store.txt", "a") as file:
    #     file.write("\nId:"+ courseId +"--")
    #     file.write("Course Name:"+ courseName+"--")
    #     file.write("Pre Requite Course Id:"+ coursePreRequisite+"--")
    #     file.write("Description:"+ courseDescription)

#--------------- update course function
def updateCourse():
    print ("Enter the Course Id you want to update :")
    courseId=input()
    print ("Enter Course name:")
    courseName=input()

    print ("Enter Pre Requite Course Id:")
    coursePreRequisite=input()

    print ("Enter Course Description:")
    courseDescription=input()

    with open("store.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
                # search string
            if courseId in line:
                print('string found in a file')
                print('Line Number:', l_no)
                print('Line:', line)

                with open("store.txt", 'r') as file:
                    lines = file.readlines()
                    
                if len(lines) > int(l_no):
                    lines[l_no] = "Id:"+ courseId +"--""Course Name:"+ courseName+"--" +"Pre Requite Course Id:"+ coursePreRequisite+"--"+"Description:"+ courseDescription +"\n"
                      
                   
                with open("store.txt", 'w') as fp:
                    fp.writelines( lines )


#--------------- delete course function
def courseDelete():
    print ("Enter the Course Id you want to delete :")
    courseId=input()
    with open("store.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if courseId in line:
                with open("store.txt", 'r') as file:
                        lines = file.readlines()
                    
                if len(lines) > int(l_no):
                       lines[l_no] = "\n"
                      
                   
                with open("store.txt", 'w') as fp:
                        fp.writelines( lines )  

#--------------- all course function
def allCourse():
    print("All courses are:\n")  
    f = open("store.txt", "r")
    print(f.read())  

#--------------- individual course function
def individualCourseDetail():
    print ("Please enter course Id to see the individual course details:") 
    courseId=input()
    findingText="Id:"+courseId
    findStatus=False
    with open("store.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if findingText in line:
                print('string found in a file')
                print('Line Number:', l_no)
                print('Line:', line)
                findStatus=True
                break
        if(findStatus!=True):
            print("Course Not exist")       

def search():
    print ("Enter your search text:") 
    search=input()
    findStatus=False
    with open("store.txt", 'r') as fp:
        for l_no, line in enumerate(fp):
            if search in line:
                print('Search found in a file')
                print('Line:', line)
                findStatus=True
                  
        if(findStatus!=True):
            print("Course Not exist") 