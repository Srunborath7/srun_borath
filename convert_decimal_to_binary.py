def convertTobinary():
    decimal=int(input("Enter number for convert to binary:"))
    binary=''
    original_decimal = decimal
    while decimal>0:
        remaider=decimal%2
        binary=str(remaider)+binary
        decimal=decimal//2
    print ("Decimal of",original_decimal,"is:",binary)
convertTobinary()
     