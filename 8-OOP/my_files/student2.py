# Source name: CS50P - Lecture 8 - Object-Oriented Programming (YouTube)
# Source url: https://youtu.be/e4fwY9ZsxPw?si=osIHegPhw-7vzZrI  
# Object-oriented paradigm (AKA 'OOP')
# Solution uses a class - CODE 2  "Classes and Objects - Part 2"
# # Defines a class for a Student - improved efficiency
# Note: TypeError will occur when executed (proceed to CODE 3 for fix)
# (start: 0:36:36)
# (end:  0:39:17)


# Create a class 
# The following 2 lines are enough code to create a class 
class Student:
    ... # placeholder syntax (incomplete Class implementation)


# Dot notation used to access attributes
def main():
    student = get_student() # The student object is returned and assigned to a variable
    print(f"{student.name} from {student.house}") 
 

# APPROACH 2 - More powerful: 
    # Create an object of type Student, passing arguments directly in, on first call
    # - Call Student() function, passing 2 arguments 
    # - Note: Python WON'T YET know what to do with these, but now we are starting to standardise the way we 
    # pass data onto the class, providing improved future opportunities to error check user input.
def get_student():
    name = input("Name: ") # Assign user input to local variable, name
    house = input("House: ") # Assign user input to local variable, house
    student = Student(name, house) # Calls Student function, passing 2 arguments - Creates an object of type Student
    return student # Returns the student object


if __name__ == "__main__":
    main()