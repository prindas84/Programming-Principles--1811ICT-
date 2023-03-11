# Matthew Prendergast
# 6th June, 2022 - Problem 1 (Workshop - Week 11)

# Define the DNS class.
class DNS:
    def __init__(self):
        self.dns_dict = {}
    def update(self, domain, ip):
        self.dns_dict[domain] = ip
    def display(self, domain):
        return self.dns_dict.get(domain, None)

# Create the ISP object from the DNS class.
isp = DNS()

# Ptompt the user for input. Split their input into a list.
user_int = input("? ")
command = user_int.split()

# Process the user input.
while command[0] != "q":

    # Update the ISP disctionary.
    if len(command) == 3 and command[0] == "u":
        isp.update(command[1], command[2])

    # Retrieve the IP address for a domain.
    elif len(command) == 2 and command[0] == "l":
        print(isp.display(command[1]))

    # Bad command.
    else:
        print("Bad command.")

    # Re-prompt the user for a new input.
    user_int = input("? ")
    command = user_int.split()