no=int(input('Enter number of test cases: '))
if(no>10 or no<=0):
    print('Invalid number of test cases, try a number between 0 and 10.')
m=n=0
for i in range(no):
    m,n=input('Enter two numbers: ').split()
    m=int(m)
    n=int(n)
    if(m>=n):
        t=n
        n=m
        m=t
    if(m>=1 and n<=1000000000 and n-m<=100000):
        pass
    else:
        print('Try again')
        continue
    lst=list()
    for x in range(m,n+1):
        if(x>1):
            for y in range(2,x):
                if(x%y)==0:
                    break
            else:
                if x not in lst:
                    lst.append(x)
    for i in lst:
        print(i, end=' ')



