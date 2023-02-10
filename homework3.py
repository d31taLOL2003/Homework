#Task 1. 
# Write a loop that will prompt the user to enter a word that contains the letter "o" (both uppercase and lowercase). 
# The loop should not terminate if the user entered a word without the letter "o".

message = "Hello. Please enter any word and the program will display it."
message += "\n(If you want to stop the program, enter the word that conatins the letter 'o'.)"
message += "\nEnter your word into the console: "

while True:
    text = input(message) # Outputs the text stored in the 'message' variable and gives you the option to enter a word.
    small_letter = text.lower() # Coverts the text to lowecase.
    letter_list = list(small_letter) # Converts the text into a list of letters.
    if 'o' in letter_list:
        break # Stop the loop if the user entered a word that conatins the letter "o".
    else:
        print(text) # If the user entered a word that does not contain the letter "o" it will print the text.
    
# Task 2.
# There is a list with data lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
# Write code that populates a new list (for example, lst2) that contains only the string variables that are present in lst1. Note that lst1 is not static and can be dynamically generated from run to run.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = [] # Creates a new list containing only the string elements present in lst.
for elem in lst1: 
     if type(elem) == str: # Check if the element is a string.
        lst2.append(elem) # Add elements to lst2.
print(lst2) # Displays a list.

# Task 3. 
# There is a string with a certain text (you can use input or a constant). 
# Write code that will determine the number of words in this text that end with "o" (both uppercase and lowercase are considered).

text = "Python programming is easy to learn."
text_lower = text.lower() # Reduces letters if they are capitalized, but in this case, this is not necessary.
txt = text_lower.split(' ') # Splits text into words and then turns it into a list 
count = 0 
for word in txt: # Iterates over each element in a list
    if word.endswith('o'): # Check if the word ends with "o"
        count += 1 
print(f"Number of words with letter 'o' at the end: {count}") # Displays the number of words