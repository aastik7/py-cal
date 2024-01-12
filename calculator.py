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


print(" A. Addition \n B. Subtraction \n C. Division \n D. Division \n E. Exit ")

while True:
    choice = input("Input your choice: ")

    if choice.lower() == "a": 
        print ("Addition")
        a = int(input("Input the first number = "))
        b = int(input("Input the second number = "))
        add(a,b)
    
    elif choice.lower() == "b": 
        print ("Subtraction")
        a = int(input("Input the first number = "))
        b = int(input("Input the second number = "))
        sub(a,b)

    elif choice.lower() == "c": 
        print ("Division")
        a = int(input("Input the first number = "))
        b = int(input("Input the second number = "))
        div(a,b)

    elif choice.lower() == "d": 
        print ("Multiplication")
        a = int(input("Input the first number = "))
        b = int(input("Input the second number = "))
        mult(a,b)

    elif choice.lower() == "e":
        print("Exited")
        break

    else:
        print("Invalid input: Please choose a valid option (A,B,C,D,E)")