def wish():
    print("Hello Good Morning")
wish()
wish()
wish()


#Parameter
def wish(name):
    print("Hello",name, "Good Morning")
wish("Ujjwal")
wish("Vishal")
wish("Sujeet")


#Square
def square(number):
    print("The Square of",number,"is",number*number)
square(4)
square(5)


#Write a function to accept 2 numbers as input and return sum.(Return Statement)
def add(x,y):
    return x+y
result=add(10,20)
print("The sum is",result)
print("The sum is",add(100,200))


#Check factorial
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
    for i in range(1,10):
        print("The Factorial of",i,"is :",fact(i))


#Check even or odd
def check(num):
    if num%2==0:
        print(num," is even number")
    else:
        print(num," is odd number")
check(10)
check(15)
