#skips employees on leave while taking attendance
employees = ["Anu", "Balu", "Chitra", "Dinesh", "Esha", "Feroz", "Gita", "Hari"]
# Skip employees on leave
on_leave = ["Dinesh", "Esha"]

# loop through employee list and mark attendance
for name in employees:
    if name in on_leave:  # Check if employee is on leave
       continue
    print(f"{name} is marked present.")  # Mark attendance for present employees
# This code marks each employee in the list as present, skipping those who are on leave.