N=int(input("Enter amount"))
C100=N//100
N=N%100
C50=N//50
N=N%50
C20=N//20
N=N%20
C10=N//10
N=N%10
C5=N//5
N=N%5
C2=N//2
N=N%2
C1=N//1
#print("100:",C100)
print("Number of notes:",C100+C50+C20+C10+C5+C2+C1)