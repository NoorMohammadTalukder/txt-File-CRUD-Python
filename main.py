import navigation
import crud
def main():
    print ("-------------Welcome------------")
    print ("Enter Your Password:")
    inputPass=input()
    if inputPass=="123":
        print("--------------------------")
        print ("*Password Match*")
        navigation.menu()

        # option=input()
        # # adding course
        # if option=="1":
        #     crud.addCourse()
        #     navigation.isExit()
            
        # elif option=="2":
        #     crud.updateCourse()
        #     navigation.isExit()
                
        # elif option=="3": 
        #     crud.courseDelete()
        #     navigation.isExit()
            
        # elif option=="4": 
        #     crud.allCourse() 
        #     navigation.isExit()

        # elif option=="5":
        #     crud.individualCourseDetail()
        #     navigation.isExit()
        
        # elif option=="6":
        #     navigation.crud.search()

        # elif option=="0":
        #     exit()
        
        # else:
        #     print("Wrong Option chooden")
        #     navigation.isExit()

    else:
        print ("Wrong Password")
        main()

main()
    

