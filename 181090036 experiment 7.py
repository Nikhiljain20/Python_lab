A=int(input("Enter number A "))
if(A>=0 and A<=1000):
    lst=list
    count=0
    for b in range(A+1):
        for a in range(b+1):
            if(a**2+b**2==A):
                print('The values of a and b are: ', a,b)
                count+=1
    if(count==0):
        print('No such pair exists')
else:
    print("Invalid input number")
