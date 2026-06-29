print(10+20)
print("hello"+"guys")
print(5*4)
print("hi"*4)

#custom operator overloading
class book:
    def __init__(self,page):
        self.page=page
    
    # magic method
    def __add__(self,other):
        return self.page+other.page
b1=book(200)
b2=book(300)
print(b1+b2)