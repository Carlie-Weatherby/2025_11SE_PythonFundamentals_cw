# Source name: CS50P - Lecture 8 - Object-Oriented Programming (YouTube)
# Source url: https://youtu.be/e4fwY9ZsxPw?si=osIHegPhw-7vzZrI  
# Object-oriented paradigm (AKA 'OOP')
# Solution uses a class - CODE 3  "INSTANCE METHODS - Part 1"
# Adds __init__ with instance variables
# (start: 0:39:18)
# (end: 0:49:44)


# Create a class 
class Student:
    # Initialise empty Student objects when first created
    def __init__(self, name, house): 
        # Instance variables
        self.name = name
        self.house = house 


# Dot notation used to access attributes
def main():
    student = get_student() 
    print(f"{student.name} from {student.house}") # Display name and house attribute for the student object


def get_student():
    name = input("Name: ") 
    house = input("House: ") 
    student = Student(name, house) # Constructor (creates an object of type Student)
    return student # Returns the student object


if __name__ == "__main__": 
    main()

