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

def main():

    choice = int(input('Enter 1 for Celsius to Fahrenheit. Enter 2 for Fahrenheit to Celsius'))

    if choice == 1:
        degrees_cel = int(input('Enter your temperature in Celsius: '))
        while degrees_cel < -274:
                degrees_cel = (int(input("Invalid temperature, below Absolute Zero. Enter new temperature in Celsius greater than -274: ")))
        print (CtoF (degrees_cel))
            #if degrees_cel < -274:
     #           print ("Invalid temperature, below Absolute Zero")

    elif choice == 2:
        degrees_fah = int(input('Enter your temperature in Fahrenheit: '))
        while degrees_fah < -460:
            degrees_fah = (int(input("Invalid temperature, below Absolute Zero. Enter new temperature in Fahrenheiht greater than -460: ")))
        print (FtoC (degrees_fah))

    else:
        main()

    restart = (input("Would you like to do another conversion?"))
    restart = restart.upper()
    if restart == "YES":
        main()
    else:
        quit()

print (main())

