# This file contains five functions,
# each of which performs a physics calculation.

# Describe to the user how to use the program
print("Welcome to PHY 101! What do you want to calculate?\n"
      "Enter 'a' to calculate work done\n"
      "Enter 'b' to calculate power\n"
      "Enter 'c' to calculate pressure\n"
      "Enter 'd' to calculate potential energy\n"
      "Enter 'e' to convert Celsius to Fahrenheit\n")


# Define the five available functions
def calculate_work_done():
    # Get inputs
    force = float(input("Enter force: "))
    displacement = float(input("Enter displacement: "))
    # Calculate work done
    work_done = force * displacement
    # Print result
    print("Calculating work done...")
    print(f"Work done = {work_done} Joules")


def calculate_power():
    # Get inputs
    work_done = float(input("Enter work done: "))
    time_taken = float(input("Enter time taken: "))
    # Calculate power
    power = work_done / time_taken
    # Print result
    print("Calculating power...")
    print(f"Power = {power} Watts")


def calculate_pressure():
    # Get inputs
    force = float(input("Enter force: "))
    area = float(input("Enter area: "))
    # Calculate pressure
    pressure = force / area
    # Print result
    print("Calculating pressure...")
    print(f"Pressure = {pressure} Pascals")


def calculate_potential_energy():
    # Get inputs
    mass = float(input("Enter mass: "))
    height = float(input("Enter height: "))
    # Calculate potential energy
    potential_energy = mass * 9.8 * height
    # Print result
    print("Calculating potential energy (take g = 9.8m/s^2)...")
    print(f"Potential energy {potential_energy} Joules")


def convert_celsius_to_fahrenheit():
    # Get celsius value
    celsius_value = float(input("Enter celsius value: "))
    # Convert it to Fahrenheit
    fahrenheit_value = (celsius_value * (9 / 5)) + 32
    # Print result
    print(f"Converting {celsius_value} Celsius to Fahrenheit...")
    print(f"Fahrenheit value = {fahrenheit_value} Fahrenheit")

# Ask the user to input a letter
response = input("Input a letter: ")

# Run the different functions based on user's input
if response == "a":
    calculate_work_done()

elif response == "b":
    calculate_power()

elif response == "c":
    calculate_pressure()

elif response == "d":
    calculate_potential_energy()

elif response == "e":
    convert_celsius_to_fahrenheit()

else:
    print("Invalid input. Please re-run the program and enter a letter between a-e")