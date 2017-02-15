# The lowest possible temperature that physical matter can reach is -273.15 °C.
# With that in mind, please improve the function by making it print out a message
# in case a number lower than -273.15 is passed as input when calling the function.

def convert_celcius(cel):
    # Multiply by 9, then divide by 5, then add 32
    if cel <= -273.15:
        return "not a good number"
    else:
        return ((cel * 9) / 5) + 32


print(convert_celcius(-273.20))
print(convert_celcius(-273.0))