allow_list = "allow_list.txt"
with open(allow_list, "r") as file:
    # reads the file and stores the IP addresses in a variable
    ip_addresses = file.read()

remove_list = "remove_list.txt"
with open(remove_list, "r") as file:
    # reads the file and stores the IP addresses in a variable
    remove_list = file.read()

# converting the string of IP addresses into a list
ip_addresses = ip_addresses.split()
remove_list = remove_list.split()

# removing the IP addresses in the remove_list from the ip_addresses list
for i in remove_list:
    if i in ip_addresses:
        ip_addresses.remove(i)

# converting the list of IP addresses back into a string so it can be written to the allow_list file
ip_addresses = "\n".join(ip_addresses)

with open(allow_list, "w") as file:
    # writing the IP addresses back to the allow_list file
    file.write(ip_addresses)