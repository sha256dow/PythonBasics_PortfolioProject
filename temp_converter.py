def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def show_menu():
    print("\nTemperature Converter")
    print("1 - C to F")
    print("2 - F to C")
    print("3 - C to K")
    print("4 - K to C")
    print("5 - F to K")
    print("6 - K to F")
    print("7 - Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit}°F")

        elif choice == '2':
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius}°C")

        elif choice == '3':
            celsius = float(input("Enter the temperature in Celsius: "))
            kelvin = celsius_to_kelvin(celsius)
            print(f"{celsius}°C = {kelvin}K")

        elif choice == '4':
            kelvin = float(input("Enter the temperature in Kelvin: "))
            celsius = kelvin_to_celsius(kelvin)
            print(f"{kelvin}K = {celsius}°C")

        elif choice == '5':
            fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f"{fahrenheit}°F = {kelvin}K")

        elif choice == '6':
            kelvin = float(input("Enter the temperature in Kelvin: "))
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f"{kelvin}K = {fahrenheit}°F")

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
