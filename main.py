# Assignment 1
# ICS3U
# Mukta Manhas
# March 28, 2018

def CtoF (C):
    """Convert the temperture given in Celsius to Fahrenheit"""
    F = (1.8) * C + 32
    return round(F)

###### uncomment this when you are ready to work on it
#def FtoC ():
#

temperature = int(input('Enter your temperature in Celsius: '))
print(CtoF (temperature))
