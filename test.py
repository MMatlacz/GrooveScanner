k = bin(0)
for i in range(10000):
    if(i == 123):
        pass
    else:
        k = bin(int(k, 2) ^ i)
print "\n"
print k

print int(bin(1013467993 ^ 0b111011100110101100101000000000), 2)
print bin(1000000000)
