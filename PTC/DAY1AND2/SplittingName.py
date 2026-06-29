name=input("enter name:")
mid=len(name)//2
firstpart=name[:mid]
secondpart=name[mid:]
revfirst=firstpart[::-1]
revsecond=secondpart[::-1]
result=revfirst+revsecond
print(result)