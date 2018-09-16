def convertToBinary(n): #function for converting binary, takes the variable n
    if n > 1: #Checks if the number n is greater than one, if it's not it will run the print function
        convertToBinary(n//2) #Recurssion, the function is called again in itself and will keep running multiple times.
    print(n % 2,end = "") #finds the remainer of dividing by 2, it can either be a 1 or 0, the end at the end indicates that any future print statements after
    #will be on the same line

def validateDenary(): #function for validating an input is a number
    while True: #A loop that only ends when broken
        dec = input("Enter a number: ") #a user input
        try: #trys to execute this command below indented
            dec = int(dec) #sets the variable to an integer
            break #breaks the while loop
        except: #if the code above could not be run succesfully then the code below runs instead
            print("Not a number")
    convertToBinary(dec) #calls the function while also giving it a variable to use as well

def validateBinary(): #function for validating a binary number is a binary number
    while True:
        binary = input("Input Binary Number: ")
        for i in binary: #for each character in the variable binary it is stored at i each time it runs
            if i == "0" or i == "1": #checks if the variable is a 1 or a 0
                valid = True
            else:
                valid = False
        if binary == "": #Checks if the input is blank
            valid = False
        if valid == True: #checks the while loop needs to be broken or not
            break
    binaryDenary(binary) #calls the function while also giving it a variable to use as well

def binaryDenary(binaryList): #the variable given is called binaryList and will be called like that in this function
    total = 0 #the variable total has to be set before it can be called
    length = len(binaryList) - 1 #gets the length of the binary variable and takes 1 away
    for i in binaryList:
        var = (pow(2,length)) #var equals 2 to the power of the variable length
        number = (int(i) * var) #2 to the power of length is times by either a 1 or a 0
        length -= 1 #takes one away from the variable length
        total += number #adds the number to the total
    print("Binary to Deanery: ",total) #prints out the total

def mainMenu(): #A main menu for selecting the functions
    print("1. Deanery to Binary")
    print("2. Binary to Deanery")
    print("3. Quit")
    var = input("Option: ")
    if var == "1":
        validateDenary() #Calls a function
    if var == "2":
        validateBinary()

if __name__ == '__main__':
    mainMenu()  #Calls the first function that is then used by future functions
