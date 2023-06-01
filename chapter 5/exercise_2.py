def minmax():
    min = None
    max = None

    while True:
        value = input('Insert your value: ')
        if value == "Done" or value == "done":
            break
        try:
            value= int(value)
        except:
            print('Please enter a value number')
            continue

        if min is None or value < min:
            min = value
        if max is None or value > max:
            max = value

    print(min, max)        
    return min,max

minmax()