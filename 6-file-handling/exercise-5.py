def convert_celcius(cel):
    # Multiply by 9, then divide by 5, then add 32
    return ((cel * 9) / 5) + 32


temperatures = [10, -20, -289, 100]

def writer(temps):
    with open('temps.txt', 'w') as file:
        for temp in temps:
            file.write(str(convert_celcius(temp)) + '\n')

writer(temperatures)