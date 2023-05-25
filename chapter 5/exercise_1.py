def totcountavg():    
    total = 0
    count = 0
    average = 0
    while True:
        value = input('Insert your value: ')
        if(value == "Done" or value =='done'):
            break
        try:
            value = int(value)
        except:
            print('Please enter a numerical value')
            continue

        total = total + value
        count = count + 1
        average = total / count

    print("Total: ",total)
    print("Count: ",count)
    print("average: ",average)

totcountavg()