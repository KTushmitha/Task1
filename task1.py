def to_do_list1():
     to_do_list=[]  
     while True:
        print("1.create 2.update 3.delete 4.Display")
           
        ch=int(input("Enter your choice:"))
        if ch==1:
            new=input("Enter task to be created")
            to_do_list.append(new)
            print("After adding task, TO-DO-LIST:",to_do_list)
        elif ch==2:
            a=int(input("Enter the number of the task to be updated"))
            new=input("Enter the updated task")
            to_do_list[a-1]=new
            print("After updating, TO-DO-LIST:",to_do_list)
        elif ch==3:
            a=int(input("Enter the number of the task to be deleted"))
            del to_do_list[a-1]
            print("After deleting, TO-DO-LIST:",to_do_list)
        elif ch==4:
            print("TO-DO-LIST:",to_do_list)
        a=input("Do you want to do anything?(yes/no)").lower()
        if a!="yes":
            break
to_do_list1()
