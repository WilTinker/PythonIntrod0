def calculate_runoff(length, width, rain_inches):
    # Conversion factor: 1 cubic foot of water = 7.48052 gallons
    gallons_per_cubic_foot = 7.48052
    
    # Calculate the volume of water in cubic feet
    #volume_cubic_feet = length * width * rain_inches
    
    #The AI code is wrong. Here's a possible fix
    volume_cubic_feet = length * width * (rain_inches / 12)
    
    # Convert cubic feet to gallons
    runoff_gallons = volume_cubic_feet * gallons_per_cubic_foot
    
    return runoff_gallons

def main():
    # Get user input for length, width, and rain in inches
    length = float(input("Enter the length of the surface in feet: "))
    width = float(input("Enter the width of the surface in feet: "))
    rain_inches = float(input("Enter the number of inches of rain: "))
    
    # Calculate runoff in gallons
    runoff_gallons = calculate_runoff(length, width, rain_inches)
    
    # Display the result
    print(f"The number of gallons of water runoff is: {runoff_gallons:.2f} gallons")

if __name__ == "__main__":
    main()