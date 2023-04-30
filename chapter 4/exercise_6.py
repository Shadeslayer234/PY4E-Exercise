def computepay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + ((hours - 40) * 1.5 * rate)
        print('Pay: ', pay)

    else:
        pay = (40 * rate)
        print("Pay: ", pay)

try:
    hours = int(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    computepay(hours, rate)
    
except:
    print('Please enter numerical values')
    

