# solution_8.py
# MPCS 50101 - HW1
# A program to convert from Fahrenheit to Celsius
# John Yang

def main():
    fahrenheit=eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit-32)*(5/9)
    print("The temperature is", celsius, "degrees Celsius.")

main()
