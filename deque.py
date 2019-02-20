print("deque implementation")
deque=[]
while True:
    print("WHAT YOU WANT TO PERFORM?\n 1.insert an element,2.remove an element,3.check size of deque,4.emptiness of deque,5.exit")
    choice=int(input())
    if choice==1:
         print("enter the element you want  to insert:")
         l=input()
         print("Where to insert?1.First,2.Last")
         c=int(input())
         if c==1:
             deque.insert(0,l)
    if choice==2:
         deque.append(l)
         print("Elements in deques are:",deque)
    elif choice==2:
         if deque==[]:
             print("Empty deque.You cannot delete!!")
         else:
             deque.pop(0)
             print("Elements in deque are:",deque)
    elif choice==3:
         print("size of deque is:",len(deque))
    elif choice==4:
         if deque==[]:
             print("Your deque is empty!!")
         else:
            print("You have ",len(deque),"elements in our deque")
    elif choice==5:
         print("Exit")
         break

