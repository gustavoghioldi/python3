import requests
import os
operative_system_clear = "cls" if os.name == "nt" else "clear"

os.system(operative_system_clear)

url = "http://localhost:7001/student"

while True:
    print("1. Add Student")
    print("2. Update Student")
    print("3. Read Students")
    print("4. Delete Student")
    print("5. Exit")
    
    option = input("Choice:")
    if option == "1":
        name = input("Name: ")
        courses = int(input("Number of courses: "))
        body = {"name": name, "courses":courses}
        r = requests.post(url, json=body)
        if r.status_code == 201:
            print("OK")
        else:
            print("Error")
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        break
    else:
        print("Error choice")
    input("Enter to continue")
    os.system(operative_system_clear)