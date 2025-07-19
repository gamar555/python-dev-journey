#use range() to generate invoice numbers
# use a for loop to iterate through the range of invoice numbers

strat = int(input("Enter the starting invoice number: "))  # User input for starting invoice number
end = int(input("Enter the ending invoice number: "))  # User input for ending invoice

if strat > end:  # Check if starting number is greater than ending number
    print("Starting number must be less than or equal to ending number.")

else:
    print("Generated Invoice Numbers:") #

for invoice_number in range(strat, end + 1):  # Loop through the range from start to end
    print(f"Invoice Number: {invoice_number}")  # Print each invoice number
# This code generates invoice numbers from the starting to ending number provided by the user.  