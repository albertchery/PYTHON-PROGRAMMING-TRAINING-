class Conversion:
    def int_to_roman(self,num):
        romanValues=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        integers=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        romanEqual=""

        for i in range(len(integers)):
            while num>=integers[i]:
                romanEqual+=romanValues[i]
                num-=integers[i]
        return romanEqual
#input
num=int(input("Enter the number:"))
obj=Conversion()
print(obj.int_to_roman(num))