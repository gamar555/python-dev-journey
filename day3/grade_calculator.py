# we want to evaluate the grade based on the score
def evaluate_grade(score):
    """Assign grades based on numeric score.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return  "D"
    elif score >= 50:
        return "E"
    else:
        return "F-Fail"
try:
    score = int(input("Enter your exam score (0-100):")) # Ask user for score input
    result = evaluate_grade(score) #    Call the function to evaluate grade
    print(f"Your grade is: {result}") # Print the result
except ValueError:
    print("Invalid input! Please enter a numeric score between 0 and 100.")
# This code defines a function to evaluate grades based on a numeric score.