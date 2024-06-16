from models.employee import Employee
from models.department import Department

def list_departments():
    departments = Department.get_all()
    if departments:
        for department in departments:
            print(department)
    else:
        print("No departments found.")

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    if department:
        print(department)
    else:
        print(f"Department '{name}' not found.")

def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        print(department)
    else:
        print(f"Department with id '{id_}' not found.")

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"Department created successfully: {department}")
    except Exception as e:
        print(f"Error creating department: {e}")

def update_department():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        new_name = input("Enter the new name for the department: ")
        new_location = input("Enter the new location for the department: ")
        department.name = new_name
        department.location = new_location
        try:
            department.update()
            print(f"Department updated successfully: {department}")
        except Exception as e:
            print(f"Error updating department: {e}")
    else:
        print(f"Department with id '{id_}' not found.")

def delete_department():
    id_ = input("Enter the department's id to delete: ")
    department = Department.find_by_id(id_)
    if department:
        try:
            department.delete()
            print(f"Department with id '{id_}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting department: {e}")
    else:
        print(f"Department with id '{id_}' not found.")

def exit_program():
    print("Goodbye!")
    exit()
