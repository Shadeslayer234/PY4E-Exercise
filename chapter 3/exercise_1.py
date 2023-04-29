hours = int(input('Enter hours: '))
rate = float(input('Enter rate: '))
if(hours <=40):
    print(hours * rate )
else:
    print((40 * rate) + ((hours - 40) * 1.5 * rate))


