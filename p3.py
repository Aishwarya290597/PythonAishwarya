c = float(input('Please enter the temperature in Celsius'))
print(c)

f = (c * 1.8) + 32
print(f)

temp = f

if(temp > 104):
    print('Its hot')
elif(temp < 60):
    print('Its Cold')
else:
    print('Its Pleasant')