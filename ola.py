place=["tambaram","adayar","vandalur","perambur"]
dist=[35,45,55,78]
print("WHERE YOU WANT TO GO?\n 1.thambaram,2.adayar,3.vandalur,4.perambur")
choice=int(input())
if choice==1:
      kms=dist[0]
elif choice==2:
      kms=dist[1]
elif choice==3:
      kms==dist[2]
elif choice==4:
      kms=dist[3]
car=["nano","micro","mini","prime"]
amount=[5,7,8,10]
print("WHICH TYPE YOU WANT TO GO?\n 1.nano,2.micro,3.mini,4,prime")
choice=int(input())
if choice==1:
      price=amount[0]
elif choice==2:
      price=amount[1]
elif choice==3:
      price=amount[2]
elif choice==4:
      price=amount[3]
print("Estimated amont is",kms*price)
