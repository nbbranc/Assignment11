"""
Program: Input Validation Assignment
Author: Nicholas Branch
Course: CY5003
Module: 5
"""

def validate_input(weight, height, age):
    """
    Validates user input for weight, height, and age.

    Parameters:
        weight (str): User's weight input in pounds
        height (str): User's height input in inches
        age (str): User's age input in years

    Raises:
        ValueError: If any input fails validation checks

    Returns:
        A tuple (float_weight, float_height, int_age) if the validation
        passes
        Returns None if the validation fails
    """
    try:
        # Validation 1: Type Checking - Convert height string to float
        float_height = float(height)

        # Validation 1: Type Checking - Convert weight string to float
        float_weight = float(weight)

        # Validation 3: Length Checking - Get the length of age string
        age_length = len(age)

        # Validation 1: Type Checking - Convert age string to integer
        age_int = int(age)

        # Validation 2: Range Checking - Verify height is between 48 and 85 inches
        if float_height < 48 or float_height > 85:
            raise ValueError("Height must be between 48 and 85 inches")

        # Validation 2: Range Checking - Verify weight is between 90 and 290 lbs
        if float_weight < 90 or float_weight > 290:
            raise ValueError("Weight must be between 90 and 290 lbs")

        # Validation 3: Length Checking - Verify age is exactly 2 digits
        if age_length != 2:
            raise ValueError("Age must be 2 digits")

        # Validation 2: Range Checking - Verify age is between 18 and 80 years
        if age_int < 18 or age_int > 80:
            raise ValueError(" Age must between 18 and 80 years")

        # Return validated values as a tuple if all checks pass
        return (float_weight, float_height, age_int)

    # Catch any ValueError exceptions from type conversion or validation checks
    except ValueError as e:
        # Display error message to user with specific validation failure details
        print(f"Invalid Input: {e}")
        # Returns None if the validation fails
        return None


def main():
    """
    Main function that runs the input validation program.
    Prompts user for input and calls validation function.
    """
    # Display the details about the program and the static analyzer I used
    print()
    print("This Python program performs input validation on three variables")
    print("(weight, height, and age) using type checking, range checking,")
    print("and length checking. It also uses the Bandit static analyzer.")
    print("Programmed by Nicholas Branch on February 5, 2026.")
    print()

    # WY: No early rejection at point of collection. Need a simple length/format check.
    # WY: Fail Fast. Dont Wasting resources.
    # WY: Immidiately reprompt the user instead of passing invalid data.
    # WY: Should show message of expectations and what is acceptable/unacceptable.
    # Prompt user to enter their weight in pounds
    weight = input("Enter weight in lbs: ")

    # WY: No early rejection at point of collection. Need a simple length/format check.
    # WY: Fail Fast. Dont Wasting resources.
    # WY: Immidiately reprompt the user instead of passing invalid data.
    # WY: Should show message of expectations and what is acceptable/unacceptable.
    # Prompt user to enter their height in inches
    height = input("Enter height in inches: ")

    # WY: No early rejection at point of collection. Need a simple length/format check.
    # WY: Fail Fast. Dont Wasting resources.
    # WY: Immidiately reprompt the user instead of passing invalid data.
    # WY: Should show message of expectations and what is acceptable/unacceptable.
    # Prompt user to enter their current age in years
    age = input("What is your current age in years: ")

    # Call validation function to check all three inputs
    result = validate_input(weight, height, age)

    # Check if the validation was successful
    if result is not None:
        # Unpack the returned tuple into different variables
        validated_weight, validated_height, validated_age = result

        # Display a message with the validated values
        print(f"I am {validated_age} years old, weigh "
              f"{validated_weight} lbs, and am {validated_height} inches tall")



# Check if this script is being run directly (not imported)
if __name__ == '__main__':
    # Execute the main function
    main()
