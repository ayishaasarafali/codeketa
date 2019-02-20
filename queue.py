print("stack implementation")
stack=[]
while True:
    print("WHAT YOU WANT TO PERFORM?\n 1.insert an element,2.remove an element,3.check size of stack,4.emptiness of stack,5.exit")
    choice=int(input())
    if choice==1:
         print("enter the element you want  to insert:")
         l=input()
         stack.append(l)
         print("Elements in stacks are:",stack)
    elif choice==2:
         if stack==[]:
             print("Empty stack.You cannot delete!!")
         else:
             stack.pop(0)
             print("Elements in stack are:",stack)
    elif choice==3:
         print("size of stack is:",len(stack))
         #print("Elements in stack are:",stack)
    elif choice==4:
         if stack==[]:
             print("Your stack is empty!!")
         else:
            print("You have ",len(stack),"elements in our stack")
            #print("Elements in stack are:",stack)
    elif choice==5:
         print("Exit")
         break
