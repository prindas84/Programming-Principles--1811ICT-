# Matthew Prendergast
# 1st June, 2022 - Problem 2 (Workshop - Week 10)

class GoCard:
    """The Go Card gives a user the ability to add credit to be used on public transport"""
    def __init__(self, balance):
      """Creates the Go Card with an initial balance"""
      self.open_balance = balance
      self.balance = balance
      self.transactions = [balance]

    def topUp(self, amount):
        """Tops up the balance and records the transaction"""
        self.balance += amount
        self.transactions.append(amount)

    def ride(self, amount):
        """Records a ride in the transactions and decreases the balance"""
        self.balance -= amount
        self.transactions.append(-amount)

    def balance(self):
        """Returns the current balance"""
        return self.balance

    def statement(self):
        return [self.open_balance, self.balance, self.transactions]


def checkFloat(num):
    """This function checks to see if a string value can be converted to a float value.
    
        If the string value is a float: RETURNS TRUE
        If the string value is not a float: RETURNS FALSE"""
    try:
        float(num)
        return True
    except:
        return False


# Prompt the user to enter the new balance for the Go Card.
new_balance = float(input("Creating account. Input initial balance: "))

# Create the new Go Card object.
new_card = GoCard(new_balance)

# Prompt the user for their next command.
command = input("? ")

# Process the command
while command != "q":

    # Split the command into a list and change all number values to floats.
    command_list = command.split()
    for i in range(len(command_list)):
        if checkFloat(command_list[i]):
            command_list[i] = float(command_list[i])

    # Top up the Go Card functionality
    if len(command_list) == 2 and command_list[0] == "t" and command_list[1] > 0:
        new_card.topUp(command_list[1])

    # Record a ride
    elif len(command_list) == 2 and command_list[0] == "r" and command_list[1] > 0:
        new_card.ride(command_list[1])

    # Print the balance
    elif len(command_list) == 1 and command_list[0] == "b":
        print(f"Balance = ${new_card.balance:.2f}")

    # Inform the user of their bad command.
    else:
        print("Bad command.")

    command = input("? ")

# Print the statement after quitting.

statement = new_card.statement()

print("Statement:")
print("{:20} {:>20} {:>20}".format("event", "amount ($)", "balance ($)"))
print("{:20} {:>20} {:>20.2f}".format("Initial balance", "", statement[0]))

print_balance = statement[0]
for i in range(1, len(statement[2])):
    if statement[2][i] < 0:
        print_balance += statement[2][i]
        print("{:20} {:>20.2f} {:>20.2f}".format("Ride", abs(statement[2][i]), print_balance))
    if statement[2][i] > 0:
        print_balance += statement[2][i]
        print("{:20} {:>20.2f} {:>20.2f}".format("Top up", statement[2][i], print_balance))

print("{:20} {:>20} {:>20.2f}".format("Final balance", "", statement[1]))