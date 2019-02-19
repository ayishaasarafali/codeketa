w=int(raw_input())
x=w
rev=0
while x!=0:
    rev=(rev*10)+(x%10)
    x=x//10
if w==rev:
    print("Yes")
else:
    print("no")
