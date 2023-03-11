from PyTest import *
##/////////////////////////////// PROBLEM STATEMENT ////////////////////////////////
## Write a Python program that calculates the deposit on a home loan as follows:  //
##   Loan < $25,000, deposit = 5% of Loan value                                   //
##   Loan >= $25,000 and < $50,000, deposit = $1,250 + 10% of loan over $25,000   //
##   Loan >= $50,000 and < $100,000, deposit = $5,000 + 25% of loan over $50,000  //
##                                                                                //
##   12000 -> 600                                                                 //
##   30000 -> 1750                                                                //
##   80000 -> 12500                                                               //
##//////////////////////////////////////////////////////////////////////////////////

# Input the value.
loan = float(input())

# Calculate the deposit value.
if loan < 25000:
    print(int(loan * 0.05))
elif 25000 <= loan < 50000:
    print(int((loan - 25000) * 0.1 + 1250))
elif 50000 <= loan < 100000:
    print(int((loan - 50000) * 0.25  + 5000))