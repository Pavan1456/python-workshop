# a=input("enter yiour name")
# print(len(a))
# a=25
# if a>=18 :
#     print("you are N ADULTS")
# else:
#     print("you are a mino0r")
# score=85
# if(score>90):
#     print("A")
# elif(score>80):
#     print("B")
# else:
#     print("C")

# a=True
# b=False
# if(a):
#     print("bring an umbrella")
#     if(b):
#         print("wear a jacket")
# a=int(input())
# if(a>0 ):
#     print("the number is positive")
# elif(a==0):
#     print("the number is zero")
# else:
#     print("the number is negative")
# name=set(input().split())
# name.add("mkmfd")
# name.discard("pavan")
# name.pop()
# print(name)
# def myfun(a,b):
#     return a.intersection(b)
# a=set(input().split())
# b=set(input().split())
# print(myfun(a,b))
# class pavan:
#     def __init__(self,name):
#         self.name = name
# a=pavan("oaikdn")
# print(a.name)
# class car:
#     def __init__(self,name,model):
#         self.name=name
#         self.model = model
# a=car("suzuki","zen")
# print(a.name,end=", ")
# print(a.model)
# b=car("tvs","XL100")
# print(b.name,end=" ,")
# print(b.model)

# class bankaccount:
#     def __init__(self,accountnumber,balance):
#         self.accountnumber = accountnumber
#         self.balance = balance
#     def get_balance(self):
#         return self.balance
# account = bankaccount("1878100100009311","0010")
# print(account.balance)


# class animals:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         pass
# class dog(animals):
#     def speak(self):
#         return "woof!"
# class cat(animals):
#     def speak(self):
#         return "meow!"
# dog=dog("uday")
# cat=cat("parmeet")
# print(dog.name,dog.speak())
# print(cat.name,cat.speak())

# a=[1,2,3,4,5,6,7,8,9]
# b=set(a)
# print(b)

# d={"khana":"i want","gaana":"i want to hear","machine learning":"bakwass","mam":"Rajeeve"}
# print(d)
# a=d.get("fh")
# print(a)
# print(d.keys())
# for key,value in d.items():
#     print(f"{key}:{value}")
# for i,j in d.items():
#     print(i,":",j)
# d.update({"khana":"djjdn"})
# print(d)
# a={1,2,4,5,6,7,8,9,10,11,12}
# b=list(a)
# print(b)
# a={1:3,2:4,3:5,4:6}
# a[5]=6
# print(a)
# a={1:3,2:4,3:5,4:6}
# b={1:3,2:4}
# c={1:3,2:4,3:5,4:6,5:6}
# a.update(b)
# a.update(c)
# print(a)

# a={"red":"#FF0000", "green":"#008000", "black":"#000000","white":"#FFFFFF"}
# b=sorted(a)
# for i in b:
#     print(i,":",a[i])
# d={"x":10,"y":20,"z":30}
# for i in d:
#     print(i,":",d[i])

# d={}
# n=int(input())
# for i in range(1,n+1):
#     s=i*i
#     d[i]=s
# print(d)

# d={}
# for i in range(1,16):
#     s=i*i
#     d[i]=s
# print(d)
def fn(a):
    if(a in d ):
        print(a,":",d[a])
    else:
        print("key does not exist")
d={1:10,2:10,3:10,4:10,5:50,6:60}
b=int(input("enter the key="))
fn(b)













