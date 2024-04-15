#class is a user defined data type
#genny mam classes
'''class book:
    def __init__(self,title,author,publication):
        self.title=title
        self.author=author
        self.publication=publication
def findlater(book1,book2):
    if book1.publication>book2.publication:
        return book1
    else:return book2

book1=book("The Great Gastby","F.Scort Fitzgerland",1925)
book2=book("To kill a mockingbird","Harper Lee",1960)
print("later publication year:",findlater(book1,book2).title,findlater(book1,book2).publication)'''
#area of rectangle
'''class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
def calculate_area(area):
    return area.lenght*area.width
area=Rectangle(5,3)
print("Area of Rectangle",calculate_area(area))'''
#inheritance
'''class Animal:
    def speak(self):
        pass
    def move(self):
        pass
class dog(Animal):
    def speak(self):
        print("bow")
class fish(Animal):
    def speak(self):
        print("bubble")
class bird(Animal):
    def move(self):
        print("fly")
bird_instance=bird()
dog_instance=dog()
fish_instance=fish()
bird_instance.move()
dog_instance.speak()
fish_instance.speak()'''

