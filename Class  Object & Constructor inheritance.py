# ------Constructor function
class Person:
  def __init__(self,name,age):
      self.name=name
      self.age=age
  def getData(self):
      print("My name ",self.name," Age ",self.age," From ",self.city)
class Person1(Person):
    def __init__(self,name,age,city):
        self.city=city
        super().__init__(self,name,age)    #inheretence
            
      
person1=Person1("Ajith",24,"Bangalore") 
person1.getData()
      
