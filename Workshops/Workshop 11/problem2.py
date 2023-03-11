# Matthew Prendergast
# 6th June, 2022 - Problem 2 (Workshop - Week 11)

# Define the DNS class.
class DNS:
    def __init__(self):
        self.dns_dict = {}
    def update(self, domain, ip):
        self.dns_dict[domain] = ip
    def display(self, domain):
        return self.dns_dict.get(domain, None)

# Define the Blacklist Sub-class.
class Blacklist(DNS):
    def __init__(self):
        DNS.__init__(self)
        self.__black_set = set()
    def update_black(self, ip):
        self.__black_set.add(ip)
    def display(self, domain):
        ip = self.dns_dict.get(domain, None)
        if ip in self.__black_set:
            return None
        else:
            return self.dns_dict.get(domain, None)


# Create the ISP object from the DNS class.
isp = Blacklist()

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

    # Update the blacklist.
    elif len(command) == 2 and command[0] == "b":
        isp.update_black(command[1])

    # Bad command.
    else:
        print("Bad command.")

    # Re-prompt the user for a new input.
    user_int = input("? ")
    command = user_int.split()