# Define the file to be imported (the file that contains the IP addresses)
import_file = "allow_list.txt"

# Open the file in read mode ('r') to read its contents
# Using 'with' ensures that the file is properly closed after reading
with open(import_file, "r") as file:
    # Read the contents of the file and store it in the variable 'ip_addresses'
    ip_addresses = file.read()

# Print the contents of the 'ip_addresses' variable to display the IP addresses
print(ip_addresses)
