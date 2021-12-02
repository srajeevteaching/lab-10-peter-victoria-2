#Programmers: Peter Victoria
#Course: CS151, Dr. Rajeev
#Date: 12/2/21
#Lab Number: 10
#Program Inputs: morse dictionary, file to read
#Program Outputs: morse translated to english

#creates a dictionary of the morse translations from the file
def load_morse_dictionary():
    #creat empty dictionary
    morse_dictionary = {}
    try:
        #open file for reading
        file = open ("morsecode.txt", "r")
        #go through each line in the file
        for line in file:
            #split the line into the morse key and the english value
            value, key = line.split ()
            #add key and value to dictionary
            morse_dictionary [key] = value
    #except for error
    except FileNotFoundError:
        return ()
    #return the new dictionary
    return morse_dictionary

#takes the given file, decodes it, and prints it
def decode_file(dict, filename):
    try:
        x=0
        #open file for reading
        file = open (filename, "r")
        #run through each line in file
        for line in file:
            #split line into each character
            temp = line.split()
            #run through each character
            for i in temp:
                #set char as what ever the english value is in the morse dictionary that corresponds with the given morse code (i)
                char = dict[i]
                #print character
                print (char, end="")
            #print spaces between words
            print(" ", end="")
            #go to a new line after every 15 words
            x+=1
            if x%15==0:
                print ()
    #excpet for error
    except FileNotFoundError:
        return()
    return

#main function that runs program
def main():
    #calls load morse dictionary function and returns it to dict
    dict = load_morse_dictionary()
    #asks user for file to decode
    filename = input ("input name of file to decode: ")
    #takes dict and user's file as parameter for decode file function
    decode_file(dict, filename)

main()