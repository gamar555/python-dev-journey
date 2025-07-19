# Role based access simulation in a company

user_role = input("Enter your role (admin/qa/developer/hr): ").lower()

if user_role == "admin":
    print("Full system access granted.")

elif user_role in ["qa", "developer"]:
    print("Access to testing and development environments.")

elif user_role == "hr":
    print("Access to employee records.")

else:
    print("Access denied. Invalid role specified.")
