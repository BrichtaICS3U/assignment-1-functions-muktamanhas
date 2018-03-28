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


choice = int(input('Enter 1 for Celsius to Fahrenheit. Enter 2 for Fahrenheit to Celsius'))
if choice == 1:
        degrees_cel = (int(input('Enter your temperature in Celsius: ')))
        while degrees_cel < -274:
            print (CtoF (int(input("Invalid temperature, below Absolute Zero. Enter new temperature in Celsius greater than -274: "))))
            break
        else:
            print (CtoF (degrees_cel))
        #if degrees_cel < -274:
 #           print ("Invalid temperature, below Absolute Zero")
elif choice == 2:
        print (FtoC (int(input('Enter your temperature in Fahrenheit: '))))

else:
    print (int(input('Enter 1 for Celsius to Fahrenheit. Enter 2 for Fahrenheit to Celsius')))
