c = float(input('Enter the temperature at your place in Celsius'))

f = (c*1.8)+32

temp=f

print('%0.1f temperature in celsius and %0.1f is temperature in farenheit' %(c,f))
if (temp >= 104):
  print("It's hot")
elif (temp <= 50):
  print("It's cold")
else:
  print("The temperature is nice")
