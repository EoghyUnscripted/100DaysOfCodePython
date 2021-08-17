"""

INSTITUTION: UDEMY.COM

COURSE: 100 Days of Code - The Complete Python Pro Bootcamp for 2021

INSTRUCTOR: Dr. Angela Yu

DESCRIPTION: 
Master Python by building 100 projects in 100 days. 
Learn to build websites, games, apps, plus scraping and data science

DAY: 8
PROJECT: Caesar Cipher
LEVEL: Beginner

INSTRUCTIONS:

    1. Import and print the logo from art.py when the program starts.
    2. What if the user enters a shift that is greater than the number of letters in the alphabet?
        1. Try running the program and entering a shift number of 45.
        2. Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
        3. Hint: Think about how you can use the modulus (%).
    3. What happens if the user enters a number/symbol/space?
        1. Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
            e.g. start_text = "meet me at 3" end_text = "•••• •• •• 3"
    4. Can you figure out a way to ask the user if they want to restart the cipher program?
            e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
        1. If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
        2. Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
recoded = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, message, word_shift):

    """     # Tests if the shift input is greater than the range available
    if word_shift > len(alphabet):
        print(f"Please choose a number between 1 and {len(alphabet)}.")
        exit()  # Exits the program """

    caesar_text = ""   # Holds the output string

    # Shifts the letter placements in the recoded list
    for i in range(0, word_shift):
    
        if direction == "encode":
            recoded.append(recoded[0])  # Add element at beginning of list to the end
            recoded.pop(0)  # Remove element at beginning of list

        elif direction == "decode":
            last_elem = -1  # Variable pointing to last element in the list
            recoded.insert(0, recoded[last_elem])   # Get last item in the list and insert into first position
            recoded.pop(last_elem)  # Remove element at end of list

    # Loop through each character of the input text
    for char in message:

        location = alphabet.index(char) # Get location from original alphabet 
        caesar_letter = recoded[location]     # Get letter from shifted alphabet
        caesar_text += caesar_letter  # Add to output text variable

    print(f"The {direction}d text is {caesar_text}")

caesar(direction=direction, message=text, word_shift=shift) # Call function