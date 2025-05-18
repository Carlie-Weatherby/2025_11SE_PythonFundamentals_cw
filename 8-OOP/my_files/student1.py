class Student:
    ... # Placeholder syntax (incomplete Class implementation)


# Dot notation used to access attributes
def main():
    student = get_student() # The student object is returned and  assigned to a variable
    print(f"{student.name} from {student.house}") # Display attributes for the student object using dot notation



def get_student():
    student = Student() # Calls Student function - Creates an object of type Student
    student.name = input("Name: ") # Assign user input to name attribute
    student.house = input("House: ") # Assign user input to house attribute
    return student # Returns the student object


if __name__ == "__main__":
    main()