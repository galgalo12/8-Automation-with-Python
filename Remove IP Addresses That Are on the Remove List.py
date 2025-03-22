# Specify the file name containing the list of IP addresses
import_file = "allow_list.txt"

# Create a list of IP addresses that are no longer allowed access
# These IP addresses will be removed from the imported list
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Use the `with` statement to open the file in read mode ('r') and read its contents
# This ensures the file is properly closed after reading
with open(import_file, "r") as file: 
    ip_addresses = file.read()

# Convert the file content (string) into a list by splitting it using whitespace
# This assumes IP addresses are separated by spaces, tabs, or newlines
ip_addresses = ip_addresses.split()

# Iterate through each IP address in `ip_addresses`
# The loop variable `element` represents each IP address in the list
for element in ip_addresses:
  
    # Check if the current IP address exists in the `remove_list`
    if element in remove_list:

        # If a match is found, remove the IP address from `ip_addresses`
        ip_addresses.remove(element)

# Print the final list of allowed IP addresses after removing the blocked ones
print(ip_addresses)
