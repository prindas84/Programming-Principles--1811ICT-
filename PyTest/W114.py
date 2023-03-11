from PyTest import *
##/////////////// PROBLEM STATEMENT /////////////////
## Convert a height input as centimetres to metres //
## and centimetres                                 //
##                                                 //
##  centimetres     metres centimetres             //
##      110      ->    1       10                  //
##     1256      ->   12       56                  //
##///////////////////////////////////////////////////

# Prompt for user input
length = int(input())

# Split the length into metres and centimetres
metres = length // 100
centimetres = length % 100

# Print the result.
print(f"{metres}:{centimetres}")