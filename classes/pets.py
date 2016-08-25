#INHERITANCE REVIEW

class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Pet):
    def __init__(self,name,age):
        super().__init__(name,age)
    def talk(self):
        return 'Meow!'
class Dog(Pet):
    def __init__(self,name,age):
        super().__init__(name,age)
    def talk(self):
        return 'Woof!'

def Main():
    
  thePet = Pet('thePet',1)
  jess = Cat('Jess',3)

##  print('Jess is a Cat', isinstance(jess,Cat))  #True 
##  print('Jess is a Pet', isinstance(jess,Pet))  #True
##  print('Pet is a Cat', isinstance(thePet,Cat)) #False
##  print('Pet is a Pet', isinstance(thePet,Pet)) #True


  pets = [jess, Dog('Jack',2), Cat('Fred',7),Pet('thePet',5)]

  for pet in pets:
      print('Name:',pet.name,', Age:',pet.age,', Says:',pet.talk())

if __name__ == '__main__':
    Main()
