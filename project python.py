#this line is added by PyProder
a=int(input("Enter a number: "))
f=0
for i in range(2,a):
    if a%i==0:
        f=1
        print("it is divisible by",i)
        break
    if f==1:
        print(a,"is not a prime number")
    else:
        print(a,"is a prime number")
        c=a
        rev=0
        while c>0:
            r=c%10
            rev=rev*10+r
            c=c//10
         print("reverse of the number is:",rev)
         if rev==a:
             print(a,"is a palindrome number")
         else:
             print(a,"is not a palindrome number")
