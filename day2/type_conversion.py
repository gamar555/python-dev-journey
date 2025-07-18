# Demonstrate all major conversions and input types

num_str = "12"
num_int = int(num_str) # Convert string to integer
num_float = float(num_str) # Convert string to float
is_adult = num_int >= 18 # Boolean check for adulthood

print(f"String: {num_str}, Type: {type(num_str)}")
print(f"Integer: {num_int}, Type: {type(num_int)}")
print(f"Float: {num_float}, Type: {type(num_float)}")
print(f"Boolean: {is_adult}, Type: {type(is_adult)}")