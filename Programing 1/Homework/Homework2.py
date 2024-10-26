
#Exercise 1
def titleMaker(title, character1, character2):#Set Parameters
    #Get the inputs
    title = input("Please put in the tittle of the program: ").upper()
    character1 = input("Please enter a character: ")
    character2 = input("Please enter a character: ")
    space = ' '
    #Create the title with the gathered inputs
    print(character1*50)
    print(f"{character1*2} {space*44} {character1*2}")
    print(f"{character1*2} {space*15} {character2*2} {title} {character2*2} {space*15}  {character1*2}")
    print(f"{character1*2} {space*44} {character1*2}")
    print(character1*50)
    #Return the function
    return title, character1, character2

print(titleMaker())


#Exercise 2
def format_number(num):
    # Check if the input number has exactly 12 digits
    if num < 100000000000 or num >= 1000000000000:
        return "Error: Input number must have 12 digits"
    
    # Extract the three sections of four digits each using floor division and modulo operator
    section1 = num // 1000000
    section2 = (num // 1000) % 1000
    section3 = num % 1000
    
    # Format the output with hyphens
    formatted_num = f"{section1:04}-{section2:03}-{section3:03}"
    
    return formatted_num

# Test the function
num = int(input("Enter a 12-digit integer number: "))
print(format_number(num))


#Exercise 3
def age_comparison():
    people = [{"name": input("Enter the name of person 1: "), "age": int(input("Enter the age of person 1: "))},
              {"name": input("Enter the name of person 2: "), "age": int(input("Enter the age of person 2: "))},
              {"name": input("Enter the name of person 3: "), "age": int(input("Enter the age of person 3: "))}]

    oldest_person = people[0]
    youngest_person = people[0]

    for person in people:
        if person["age"] > oldest_person["age"]:
            oldest_person = person
        if person["age"] < youngest_person["age"]:
            youngest_person = person

    def get_age_category(age):
        if 13 <= age <= 19:
            return "Teen: Ages 13-19"
        elif 20 <= age <= 64:
            return "Adult: Ages 20–64"
        else:
            return "Senior: Ages 65 and above"

    for person in people:
        print(f"{person['name']}'s age category is {get_age_category(person['age'])}.")

    print(f"The oldest person is {oldest_person['name']}.")
    print(f"The youngest person is {youngest_person['name']}.")

# Run the program
age_comparison()



#Exercise 4
def calculate_age():
    name = input("Enter your name: ")
    year_of_birth = int(input("Enter your year of birth: "))

    age_at_2024 = 2024 - year_of_birth
    print(f"Hello, {name}, At the end of 2024, you will be {age_at_2024} years old.")

    # Calculate age in minutes and seconds
    minutes_lived = age_at_2024 * 525600  # 525600 minutes in a year
    seconds_lived = minutes_lived * 60
    print(f"Your age in minutes is approximately {minutes_lived} minutes.")
    print(f"Your age in seconds is approximately {seconds_lived} seconds.")

    # Find leap years
    print("The leap years you have lived through are:")
    leap_years = [year for year in range(year_of_birth, 2024) if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)]
    for year in leap_years:
        print(year)

    print(f"You have lived through {len(leap_years)} leap years.")

calculate_age()