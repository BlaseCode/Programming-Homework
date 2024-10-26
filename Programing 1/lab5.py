'''
Golf scores record the number of strokes used to get the ball in the hole. 
The expected number of strokes varies from hole to hole and is called par 
(possible values: 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:

"Eagle": number of strokes is two less than par
"Birdie": number of strokes is one less than par
"Par": number of strokes equals par
"Bogey": number of strokes is one more than par


Given two integers that represent the number of strokes used and par, 
write a program that prints the appropriate score name. Print "Error" at the end of the output if
 par is not 3, 4, or 5, or if the score's name is not "Eagle", "Birdie", "Par", or "Bogey
'''

'''
def give_golf_score():
    #Get the number of strokes and par from the user
    stroke = int(input())
    par = int(input())

    #?Give all of the scores values 
    #if par is less equal to stroke
    if par == stroke:
        print(f"Par {par} in {stroke} strokes is Par")
    #if par is one less than stroke
    elif par == stroke - 1:
        print(f"Par {par} in {stroke} strokes is Birdie")
    #if par is two more than stroke
    elif par == stroke - 2:
        print(f"Par {par} in {stroke} strokes is Eagle")
    #if par is one more than stroke
    elif par == stroke + 1:
        print(f"Par {par} in {stroke} strokes is Bogey")
    elif par != 3 or par != 4 or par != 5:
        print(f"Par {par} in {stroke} strokes is Error")
    else:
        print(f"Par {par} in {stroke} strokes is Error")
              
give_golf_score

'''
#*Correct Version Bellow

'''
def golf_score(strokes, par):
    # Validate par
    if par not in (3, 4, 5):
        print("Error")
        return

    # Determine the score name based on strokes and par
    if strokes == par - 2:
        score_name = "Eagle"
    elif strokes == par - 1:
        score_name = "Birdie"
    elif strokes == par:
        score_name = "Par"
    elif strokes == par + 1:
        score_name = "Bogey"
    else:
        print("Error")
        return
    
    print(f"Par {par} in {strokes} strokes is {score_name}")

# Example input
strokes = int(input("Enter the number of strokes: "))
par = int(input("Enter the par: "))

golf_score(strokes, par)
'''


'''
def move_decimals(input1):
    #multiply the inputs by the different sets of values
    one = input1 * 6
    two = input1 * 10
    three = input1 * 2
    four = input1 * 20
    five = input1 * 13

    print(f'{one:.2f}')
    print(f'{two:.2f}')
    print(f'{three:.2f}')
    print(f'{four:.2f}')
    print(f'{five:.2f}')




input1 = float(input())
move_decimals(input1)
'''

# # TODO: Import the random module
# import random

# def number_guess(num):
#     # TODO: Get a random number between 1-100
#     random_number = random.randint(1,100)
    
#     # TODO: Compare parameter num to the random number
#     if random_number > num:
#         print(f"{user_input} is too low. Random number was {random_number}.")
#     if random_number < num:
#         print(f"{user_input} is too high. Random number was {random_number}.")
#     else:
#         print(f"{user_input} is correct!")
        
    
        
#     if __name__ == "__main__":
#     # Use the seed 900 to get the same pseudo random numbers every time
#         random.seed(900)
    
#         user_input = input()
#         tokens = user_input.split()
    
#     for token in tokens:
#         # Convert the string tokens into integers
#         num = int(token)
#         number_guess(num)