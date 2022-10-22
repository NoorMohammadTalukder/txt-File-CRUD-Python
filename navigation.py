import crud

def isExit():
    print("Choose an option \n 1.Return to main menu \n 0.Exit")
    option=input()
    if option=="1":
        menu()
    elif option=="0":
        exit()
    else:
        print("Wrong Option choosen")

def menu():
    print("Choose an option \n 1.Add Course \n 2.Update Course \n 3.Delete Course \n 4.See All Couse \n 5.See individual Course \n 6.Search \n 0.Exit" )
    # menu()

    option=input()
        # adding course
    if option=="1":
        crud.addCourse()
        isExit()
        
    elif option=="2":
        crud.updateCourse()
        isExit()
                
    elif option=="3": 
        crud.courseDelete()
        isExit()
            
    elif option=="4": 
        crud.allCourse() 
        isExit()

    elif option=="5":
        crud.individualCourseDetail()
        isExit()
        
    elif option=="6":
        crud.search()

    elif option=="0":
            exit()
        
    else:
            print("Wrong Option chooden")
            isExit()