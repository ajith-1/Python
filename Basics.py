# reverse
n = int(input("Enter number: "))  
  
reverse = 0  
  
while(n>0):  
    digit = n%10  
    reverse = reverse*10+digit  
    n=n//10  
print("The reverse of the number:",reverse)  

# Sum of digits
sum = 0
number = int(input("Enter an integer: "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)


# palindrom
a=int(input("start : "))
c=str(a)
b=(c[::-1])
if(c==b):
   print("palindrom")
else:
    print("not palindrom")
    
#     fact
a=int(input("start : "))

fac=1
for i in range(1,a+1):
    fac=fac*i
print(fac)
#  prime
a=int(input("start : "))
b=int(input("End : "))

for i in range(a,b):
   if (i>1):
    for j in range(2,i):
        if(i%j==0):
           break
    else:
        print(i,"prime")
        
# Average of numbers
count=int(input("Enter the count : "))
sum=0
for i in range(0,count):
    num=int(input("Enter number : "))
    sum=sum+num
    avg=sum/count
print(avg)
