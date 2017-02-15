def convert_celcius(cel):
    # Multiply by 9, then divide by 5, then add 32
    if cel <= -273.15:
        return "not a good number"
    else:
        return ((cel * 9) / 5) + 32


temperatures = [10, -20, -289, 100]

for temp in temperatures:
    print(convert_celcius(temp))