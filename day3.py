# #global variable
# x=10
# def myfunc(): 
#     print(x)
# myfunc()

#local variable
# def myfunc():
#     a=10
#     print(a)


#game
import random
a=random.randint(1,100)
c=0
while True:
    b=int(input("Enter the Number="))
    c=c+1
    if(b==a):
        print("Congratualations! You Win!")
        print("You Win the Game After",c-1,"Attempts")
        break
    elif(b>a):
        print("Give Lower Numbers")
    else:
        print("Give Higher Numbers")