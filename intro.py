import re

def my_function(str1,str2):
    print(str1, end =', ')
    print(str2)

def print_something(name="andi",age=19):
    # print("My name " + name + ", and my age "+str(age))
    print("My name ", name, ", and my age ",age)

def print_people(*people):
    for person in people:
        print("This person is",person)    

def do_math(num1,num2):
    return num1+num2, num1-num2

def my_exam(score, no_cheating = True):
    if no_cheating:
        if score <50:
            print("not pass")
        elif score >=50 and score <70:
            print("can repeat")
        else :
            print("Good job!")
    else :
        print("youre drop out")

###*use the function above*###
my_function("This is my function","A second string.")

# print_something("Sandro",23)
print_something(age = 23)

print_people("Nick", "Andi", "Budi", "Andre", "Drakor")

plus1,minus1=do_math(2,4)

print("sum is", plus1, "Minus is", minus1)

my_exam(90,False)

#####################################REGEX##########################################
# Function 	#   Description                                                        #
####################################################################################
# findall   #   Returns a list containing all matches                              #
# search    #  	Returns a Match object if there is a match anywhere in the string  #
# split     #   Returns a list where the string has been split at each match       #
# sub       #   Replaces one or many matches with a string                         #
####################################################################################

mystring=("'I AM NOT YELLING!' she said, though we knew it to not be true.")
new1=re.sub('[A-Z]', '', mystring)
new2=re.sub('[a-z]', '', mystring)
new3=re.sub('[.,\'!]', '', mystring)
new4=re.sub('[.,\'!a-z]', '', mystring)
new5=re.sub('[.,\'!a-z\s]', '', mystring)
new6=re.sub('[.,\'!a-zA-Z]', '', mystring)
new7=re.sub('[.,\'!a-zA-Z\s]', '', mystring)
# regex >>> a-zA-Z0-9\',!;\?\$\^:\\\/`\|~&\" @#%\*\{}\(\)_\+\.\s=-
print("0, length is :",len(mystring), "and the string is:",mystring)
print("1, length is :",len(new1), "and the string is:",new1)
print("2, length is :",len(new2), "and the string is:",new2)
print("3, length is :",len(new3), "and the string is:",new3)
print("4, length is :",len(new4), "and the string is:",new4)
print("5, length is :",len(new5), "and the string is:",new5)
print("6, length is :",len(new6), "and the string is:",new6)
print("7, length is :",len(new7), "and the string is:",new7)

# x = re.findall("[e]", mystring)
# print(x)
run = True
previous = 0
def performMath():
    global run
    global previous
    equation =""
    if previous == 0:
        equation = input("Enter Equation:")
    else:
        equation = input(str(previous))
    
    if equation == 'q':
        print("Bye!")
        run = False
    else:
        equation= re.sub('[a-zA-Z,.:{}" "]','',equation)

        if previous==0:     
            previous = eval(equation)
        else:
            previous = eval(str(previous)+equation)

        print("you typed",previous)
    
run = True
while run:
    performMath()
