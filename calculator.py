#Defining basic functions

#Adddition
def add(a,b):
    answer = a+b
    print( str(a) + "+" + str(b) + "=" + str(answer) ) 

#Subtraction
def sub(a,b):
    answer = a-b
    print( str(a) + "-" + str(b) + "=" + str(answer))

#Division
def div(a,b):
    answer = a/b
    print( str(a) + "/" + str(b) + "=" + str (answer))

#Multiplication
def mult(a,b):
    answer = a*b 
    print (str(a) + "*" + str(b) + "=" + str (answer))


print("A. Addition \n B. Subtraction \n C. Divisoin \n D. Division \n E. Exit ")

choice = input("Input your choice: ")

if choice == "a" or choice == "A": 
    print ("Addition")
    a = int(input("Input the first number = "))
    b = int(input("Input the second number = "))
    add(a,b)
 
elif choice == "b" or choice == "B": 
    print ("Subtraction")
    a = int(input("Input the first number = "))
    b = int(input("Input the second number = "))
    sub(a,b)

elif choice == "c" or choice == "C": 
    print ("Division")
    a = int(input("Input the first number = "))
    b = int(input("Input the second number = "))
    div(a,b)

elif choice == "d" or choice == "D": 
    print ("Multiplication")
    a = int(input("Input the first number = "))
    b = int(input("Input the second number = "))
    mult(a,b)

elif choice == "e" or choice == "E":
    print("Exited")
    quit() 

    