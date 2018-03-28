# Assignment 1
# ICS3U
# Mukta Manhas
# March 28, 2018

def CtoF (C):
    """Convert the temperature given in Celsius to Fahrenheit"""
    F = (1.8) * C + 32
    return round(F)

def FtoC (F):
    """Convert the temperature given in Fahrenheit to Celsius"""
    C = (0.55556) * (F-32)
    return round(C)

#Ctemperature = int(input('Enter your temperature in Celsius: '))
#Ftemperature = int(input('Enter your temperature in Fahrenheit: '))

choice = int(input('Enter 1 for Celsius to Fahrenheit. Enter 2 for Fahrenheit to Celsius'))
if choice == 1:
        print (CtoF (int(input('Enter your temperature in Celsius: '))))
elif choice == 2:
        print (FtoC (int(input('Enter your temperature in Fahrenheit: '))))
