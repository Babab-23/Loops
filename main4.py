# Function to calculate the power of a number
def calculate_power(base, exponent):
    return base ** exponent

# Main function
def main():
    print("Power Calculator")
    try:
        # Input the base and the exponent
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent (n): "))
        
        # Calculate the power
        result = calculate_power(base, exponent)
        
        # Display the result
        print(f"{base} to the power of {exponent} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values for base and an integer for the exponent.")

# Run the program
if __name__ == "__main__":
    main()