'''
Practice with a simple example
Practicing Loops For the exam and getting down the concepts
'''

#Make a function that makes a list of users that are put in
    #and then saves their level as well.
def make_users_list():
    #make an empty dictionary to store the user info
    database = {}

    #make a variable to help initiate the while loop
    answer = "yes"

    usernames = []
    levels = []

    #Greet the person adding the different users 
    print(f"Hello, its nice to meet you Player.\n")
    print(f"Are you ready to play?\n")

    #Make a while loop that iterates and stores users for
        # as many as the person adding will want.
    while answer == "yes":
        #Ask the username they want entered
        user = input(f"Please enter your username: \n")
        #Add the username to the list "database"
        usernames.append(user)
        #Ask the users level to the list "database" 
        level = int(input(f"Please your level: \n"))
        #Add the level to the list "database"
        levels.append(level)

        #Make a for loop that adds the "username" and "levels" list to the "database"
            #dictionary
        #for the data(objects) in the range of the length of the list "usernames"
        for data in range(len(usernames)):
            #database stores the data in "usernames" and the data in levels
            database[usernames[data]] = levels[data]

        #Give the user the option to leave stop inputting users
        answer = input(f"Do you want to add one more user (enter - yes/no): ").lower
        #Give the option to end the function
        if answer == "no":
            print(f"Okay, i'll be sure to add the users and their levels to the database.")
            #break the function if answer = "no"
            break
            #RETURN DATABASE
        return database


make_users_list()