# reverse
n = int(input("Enter number: "))  
  
reverse = 0  
  
while(n>0):  
    digit = n%10  
    reverse = reverse*10+digit  
    n=n//10  
print("The reverse of the number:",reverse)  

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
