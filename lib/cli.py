from helpers import (
    list_departments, find_department_by_name, find_department_by_id,
    create_department, update_department, delete_department, exit_program
)

def main():
    while True:
        print("\nPlease select an option:")
        print("0. Exit the program")
        print("1. List all departments")
        print("2. Find department by name")
        print("3. Find department by id")
        print("4. Create department")
        print("5. Update department")
        print("6. Delete department")

        choice = input("> ")

        if choice == '0':
            exit_program()
        elif choice == '1':
            list_departments()
        elif choice == '2':
            find_department_by_name()
        elif choice == '3':
            find_department_by_id()
        elif choice == '4':
            create_department()
        elif choice == '5':
            update_department()
        elif choice == '6':
            delete_department()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
