# Allow only 3 otp attempts (while loop + conditional statements)

correct_otp ="987654"
attempts = 0
max_attempts = 3

while attempts < max_attempts: # Loop until max attempts reached
    user_otp = input("Enter the OTP: ") # User input for OTP

    if user_otp == correct_otp: # Check if OTP is correct
        print("OTP is correct. Access granted.")
        break # Exit loop if OTP is correct
    else:
        print("Incorrect OTP. Please try again.")
        attempts += 1 # Increment attempts
if attempts == max_attempts: # Check if max attempts reached
    print("Maximum attempts reached. Access denied.") # Deny access after max attempts
