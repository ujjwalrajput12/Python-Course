#For loop

for x in range (0,3) :
    print ('Loop execution %d' % (x))


#2.
for letter in 'TutorialsCloud': 
   print ('Current letter is:', letter)

#3.While loop
   #initialize count variable to 1
count =1

while count < 6 :
    print (count)
    count+=1
#the above line means count = count + 1

#4.Nested loop
for g in range(1, 6):
    for k in range(1, 3):
        print ("%d * %d = %d" % ( g, k, g*k))

#Break
#count = 0

#while count <= 100:
    #print (count) count += 1 if count >= 3:
     # break

#Continue
for x in range(10):
   #check whether x is even
   if x % 2 == 0:
      continue
   print (x)

#Dictionary:
dicto = {'Bookname' : 'Python', 'Price' : 210}
print (dicto['Bookname'])
print (dicto['Price'])

#Function
def avrg(first, *rests):
    return (first + sum(rests)) / (1 + len(rests))

# Sample use, Putting values

print (avrg(1, 2))
print (avrg(1, 2, 3))
print (avrg(1,2,3,4))

#Fibonnacci using function
def fibo(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a

# Show the first 13 Fibonacci numbers.
for c in range(0, 13):
    print(fibo(c)) #Function call


#2.
def karlos():
    return 1, 2, 3

a, b, c = karlos()

print (a)
print (b)
print (c)



#Fuctions:  (Default argument example)

def defArgFunc( empname, emprole = "Manager" ):   
   print ("Emp Name: ", empname)
   print ("Emp Role ", emprole)
   return;
print("Using default value")
defArgFunc(empname="Ujjwal")
print("************************")
print("Overwriting default value")
defArgFunc(empname="Vishal",emprole = "CEO")


#Keyword argument example:
def keyArgFunc(empname, emprole):   
   print ("Emp Name: ", empname)
   print ("Emp Role: ", emprole)
   return;   
print("Calling in proper sequence")
keyArgFunc(empname = "Ujjwal",emprole = "Manager" )
print("Calling in opposite sequence")
keyArgFunc(emprole = "Manager",empname = "Ujjwal")


# Variable length argument example:
def varLenArgFunc(*varvallist ):   
   print ("The Output is: ")
   for varval in varvallist:
      print (varval)
   return;   
print("Calling with single value")
varLenArgFunc(55)
print("Calling with multiple values")
varLenArgFunc(50,60,70,80)


#Python Function Argument and Parameter
def addition(x,y):  
            print (x+y) 
x=15  
addition(x ,10)  
addition(x,x)  
y=20


#Function Definition  
def msg(Id,Name,Age=21):  
            "Printing the passed value"
            print (Id )
            print (Name) 
            print (Age)  
            return  
#Function call  
msg(Id=100,Name='Ravi',Age=20)  
msg(Id=101,Name='Ratan')


#Local Variables
def msg():  
           a=10  
           print ("Value of a is",a) 
           return  
  
msg()  
print (a) #it will show error since variable is local


#Global variables
b=20  
def msg():  
           a=10  
           print ("Value of a is",a)  
           print ("Value of b is",b)
           return  
  
           msg()  
           print (b)  
