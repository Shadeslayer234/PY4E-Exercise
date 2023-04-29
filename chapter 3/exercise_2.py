
try:
    hours = int(input('Enter hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Please enter numerical values')
    exit()

if hours <= 40:
    print( hours * rate )

else:
    print((rate * 40) + ((hours - 40) * rate * 1.5))

 


