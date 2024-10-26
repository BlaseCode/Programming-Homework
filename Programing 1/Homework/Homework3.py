'''
Exercise 1: Age Category
Use functions, for loops, conditionals and lists:

a. Write a program that accepts the names and ages of three people.
b. Print the name of the oldest person.
c. Print the name of the youngest person.
d. For each person, print their age category (Child, Teen, Adult, Senior)
'''

def young_old_age():
    """Get person info, categorize age, and print oldest, youngest, and age categories"""
    people = []
    while True:
        name = input("Enter the person's name: ")
        age = int(input(f"Enter the age of {name}: "))
        people.append([name, age])
        cont = input("Add another person? (yes/no): ")
        if cont.lower() != "yes":
            break

    # Categorize age and print age categories
    for person in people:
        category = "Child" if person[1] < 13 else "Teen" if person[1] < 20 else "Adult" if person[1] < 65 else "Senior"
        print(f"{person[0]} is a {category}")

    # Print oldest and youngest person
    people.sort(key=lambda x: x[1])
    print(f"The oldest person is {people[-1][0]}")
    print(f"The youngest person is {people[0][0]}")

young_old_age()
            


'''
Exercise 2: Grades 
Using functions, for loops, conditionals and lists:

a. Create a function get_lab_grades() to obtain from the user a list of lab grades.
b. Create a function get_hw_grades() to obtain from the user a list of homework grades.
c. Create a function get_quiz_grades() to obtain from the user a list of quizzes grades.
d. Create a function get_exam_grades() to obtain from the user a list of exam grades.
e. Use the list percentages = [0.1, 0.3, 0.1, 0.5] for the weights of each group of assignments.
f. Create a function compute_grade() that inputs each of the assignments lists and percentages
weights list as inputs and return the final grade.

'''        

def get_lab_grades():
    """Get lab grades from user and return as list"""
    
    #?create an empty list to store the lab grades
    lab_grades = []

    #? Make a while loop to iterate as long as the user wants to keep adding grades 
    while True:
        #?get users input for the grade
        grade = int(input("Please enter your lab grade: "))
        #?add the users grade to the list
        lab_grades.append(grade)
        #?ask the user if they want to keep going
        keep_going = input("Do you want to enter another grade (yes/no): ").lower()
        #?break the loop if the answer is not yes
        if keep_going != "yes":
            break

        # return the lab_grades that were gathered with this function
        return lab_grades


def get_hw_grades():
    """Get homework grades from user and return as list"""
    #Make a repeat of the function since it does the exact same thing, just changing the list

    #Make an empty list:
    hw_grades = []
    #create a while loop that keeps asking the user for grades
     # until they dont want to anymore
    while True:
        #get the users input for the grade
        grade = int(input("Please enter the grade you got for your hw: "))
        #add the grade to the empty list as well
        hw_grades.append(grade)
        #ask the user if they want to keep going
        keep_going = input("Do you want to enter another grade (yes/no): ").lower
        #make an if statement that breaks the loop
        if keep_going != "yes":
            #break the loop
            break 
        #return the list of grades that were gathered with this function
        return hw_grades


def get_quiz_grades():
    """Get quiz grades from user and return as list"""
    #Make a repeat of the function since it does the exact same thing, just changing the list
    #Make an empty list to store the grades
    quiz_grades = []
    #create a while loop that keeps asking the user for grades
    # until they dont want to anymore
    while True:
        #get the grade from the user 
        grades = int(input("What is the grade you got on the quiz: "))
        #add the grades to the list
        quiz_grades.append(grades)
        #ask the user if they want to keep adding
        keep_going = input("Do you want to enter another grade (yes/no): ").lower
        #make an if statement that breaks the loop
        if keep_going != "yes":
            #break the function:
            break
        #return the list of grades
        return quiz_grades


def get_exam_grades():
    """Get exam grades from user and return as list"""
    #does the same thing as the other function

    #make and empty list to store grades
    exam_grades = []

    #make a while loop to keep iterating until the list 
    while True:
        #get the grade from the user
        grades = int(input("What is the grade you got on the exam: "))
        #add the grade to the list
        exam_grades.append(grades)
        #ask the user is they want to keep adding grades
        keep_going = input("Do you still want to add more grades (yes/no): ").lower()
        #make an if statement that breaks the loop
        if keep_going != "yes":
            #break the loop:
            break
        #return the list of grades
        return exam_grades


        #? Make the final function that puts everything together
        def compute_grade(lab_grade, hw_grade, quiz_grade, exam_grade):
            """Compute final grade based on lab, quiz, hw, and exam grades"""
            #get the average of each of the different grades 
            lab_avg = lab_grade / len(lab_grade)
            hw_avg = hw_grade / len(hw_grade)
            quiz_avg = quiz_grade / len(quiz_grade)
            exam_avg = exam_grade / len(exam_grade)
            

            #Make the final grade function that times each of the grades 
                #by percentages and adds them all together for the total 
            final_grade = (lab_average * percentage[0] +
                           hw_average * percentages[1] +
                             quiz_avg * percentages[2] + 
                             exam_avg * percentages[3])         

            #end the function by returning the final_grade outputted
                #from all the other functions :')  
            return final_grade
            













