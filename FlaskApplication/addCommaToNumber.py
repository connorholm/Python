def convertNumString(number):
    stringNumber = '{:,}'.format(number)
    return stringNumber
print(convertNumString(1000000))