# Specify the file name containing the list of IP addresses
import_file = "allow_list.txt"

# Create a list of IP addresses to be removed from the file
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Open the file in read mode ('r') to read its contents
with open(import_file, "r") as file:
    # Read the entire content of the file and store it as a string in `ip_addresses`
    ip_addresses = file.read()

# Convert the string of IP addresses into a list using `split()`
# This assumes IP addresses are separated by spaces, tabs, or newlines
ip_addresses = ip_addresses.split()

# Iterate over each IP address in `ip_addresses`
for element in ip_addresses:
    # Check if the current IP address is in the `remove_list`
    if element in remove_list:
        # Remove the IP address from the list if it matches an entry in `remove_list`
        ip_addresses.remove(element)

# Convert the updated list of IP addresses back to a single string with space-separated values
ip_addresses = " ".join(ip_addresses)

# Open the file in write mode ('w') to overwrite its contents with the updated IP addresses
with open(import_file, "w") as file:
    # Write the updated string of IP addresses back to the file
    file.write(ip_addresses)

# Reopen the file in read mode ('r') to verify the changes
with open(import_file, "r") as file:
    # Read the contents of the updated file and store it in `text`
    text = file.read()

# Display the updated contents of the file
print(text)
