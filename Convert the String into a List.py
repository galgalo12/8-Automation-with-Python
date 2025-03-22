# Specify the file name containing the list of IP addresses
import_file = "allow_list.txt"

# Use the `with` statement to open and read the contents of the file
# This ensures the file is properly closed after reading
with open(import_file, "r") as file: 
    ip_addresses = file.read()

# Convert the contents from a single string to a list of IP addresses
# `split()` will separate by any whitespace (e.g., spaces, tabs, or newlines)
ip_addresses = ip_addresses.split()

# Display the list of IP addresses
print(ip_addresses)
