#Nolan King
#4/1/2024
#Create a Python app that records student names and GPA

def main():
    print("Welcome to the Student Records App!")
    print("Enter 'ZZZ' as the last name to quit.")

    while True:
        last_name = input("\nEnter student's last name: ")
        if last_name == 'ZZZ':
            print("\nExiting the program.")
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} does not qualify for any recognition.")

if __name__ == "__main__":
    main()