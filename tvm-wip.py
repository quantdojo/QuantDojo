def presentvalue(pv,n,i):
    result = pv*((1+i)**n)
    return result

pv = input("Input Dollar Amount: ")
n = input("Input Number of Periods: ")
i = input("Input the Interest Rate: ")

print('The future value is: %d' % presentvalue(pv,n,i))

input("Press any key to exit.")
