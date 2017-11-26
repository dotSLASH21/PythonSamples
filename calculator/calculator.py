import re

print("Simpe Python Calculator v0.1")
print("Type 'quit' to exit\n")


previous = 0
run = True

def performMath():
    #Get acess to global variables
    global run
    global previous

    #Initialize variable to hold equation
    equation = ""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

        
    if equation == 'quit':
        run = False
    else:
        #Sanitizing the entered equation for malicious contents!
        equation = re.sub('[a-zA-Z,.:=" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()
