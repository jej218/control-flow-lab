# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

is_phrase_quit = False

while not(is_phrase_quit):
    phrase = input("Please enter a word or phrase: ")
    print("What you entered is " + str(len(phrase)) + " characters long")
    if phrase == 'quit':
        is_phrase_quit = True
