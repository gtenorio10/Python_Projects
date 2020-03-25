# [2019-08-05] Challenge #380 [Easy] Smooshed Morse Code 1
# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/
# Normally, you would indicate where one letter ends and the next begins, for instance with a space between the letters' codes,
# but for this challenge, just smoosh all the coded letters together into a single string consisting of only dashes and dots.

#https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python #Ideas for writing a input checker
#https://www.w3schools.com/python/python_dictionaries.asp # function for writing dictionary
#https://www.geeksforgeeks.org/taking-input-in-python/   # this explains how to use input function
#https://www.geeksforgeeks.org/python-add-one-string-to-another/ #join function
#############################################################################################


#This is the morse code dictionary for values a to z in lower case
morse_code_a_to_z = {
    "a": ".-", "b": "-...", "c": "-.-.", "d":"-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-.."
    ,"m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--.."
}

#This checks if the input is using just alphabet without any weird spaces or numbers
def input_checker(original_text):
     if original_text.isalpha():
         text_to_morse_code(original_text)
     else:
         print("Your input is incorrect. Please use letters from A-Z and no spaces")


#create a function to transform word to morse code
def text_to_morse_code(original_text):
    lower_case_text = original_text.lower() #Transform any capital letter to lower case
    morse_text = " "
    add_white_space = " "
    for letter in lower_case_text:
        morse_code_key = morse_code_a_to_z[letter]
        morse_text =  "".join((morse_text, morse_code_key)) # join function concatenate in this case str
        morse_text = "".join((morse_text, add_white_space))
    print(morse_text)

asn = "y"
while(asn == "y"):
    original_text = input("Enter your word to be transformed to morse code: ")
    morse_code = input_checker(original_text)
    asn = input("Want to try another word?(y/n): ")







