# Genetators -------used in function with loop(yeild keyword)
def sum (num):
    for i in range(0,num):
        yield (i+1)
x=sum(20)
print(next(x))   
print (next(x))

# While loop
def sum(num):
    i=0
    while i<10:
        yield i
        i+=1
x=sum(10)
print(next(x))
print(next(x))
print(next(x))

# while Loop True
def sum(num):
    i=0
    while True:
        yield i
        i+=1
x=sum()
print(next(x))
print(next(x))
print(next(x))

# iterators with list,tuples---using iter(),next() function

li=[2,3,1,4,5,34,54,23,64]
x=iter(li)
print(next(x))


#iterators to Print infinity value ------ By class method(__iter__,__next__)
class Tokens:
    def __iter__(self):
        self.x=0          #initial value
        return self
    def __next__(self):
        if self.x<10:
            a=self.x
            self.a+=1    #increment
            return a
        else:
            raise StopIteration  #throwing Error
b=iter(Tokens())     #calling class function
print(next(b))
print(next(b)) 
print(next(b)) 
# Print value until the condition meet
