w=int(raw_input())
if((w%4==0)):
    print("Leap year")
elif((w%400==0)):
    print("Leap year")
elif((w%100==0)):
    print("Leap year")
else:
    print("Not a leap year")

