# Step 1: Start a program called `main`.
# Step 2: Set `total` to 0 to keep track of the sum of valid numbers.
# Step 3: Set `count` to 0 to count how many valid numbers the user enters.
# Step 4: Repeat forever:
#   Step 4a: Ask the user to enter a number.
#   Step 4b: Try to change the input into an integer:
#     Step 4b1: If it doesn't work (ValueError), tell the user to enter a valid number and go back to Step 4a.
#   Step 4c: If the number is -1:
#     Step 4c1: Exit the loop (stop asking for numbers).
#   Step 4d: If the number is 0:
#     Step 4d1: Tell the user that 0 isn’t valid and go back to Step 4a.
#   Step 4e: Add the number to `total`.
#   Step 4f: Increase `count` by 1 (one more valid number).

# Step 5: After the loop ends:
#   Step 5a: If `count` is more than 0:
#     Step 5a1: Calculate `average` by dividing `total` by `count`.
#     Step 5a2: Show the average to the user.
#   Step 5b: If no valid numbers were entered:
#     Step 5b1: Tell the user that no valid numbers were entered.

# Step 6: If this is the main program, run the `main` function.

def main():
    total = 0  
    count = 0 

    while True: 
        user_input = input("Enter a number any number(type -1 to stop): ") 
        
        try:
            number = int(user_input)  
        except ValueError: 
            print("Please type a valid number.")
            continue 
        if number == -1: 
            break 
        elif number == 0: 
            print("0 oh god really you had to pick the only invaild one.")
            continue 
        
        total += number 
        count += 1 
    
   
    if count > 0:
        average = total / count
        print(f"The average of the valid numbers entered is: {average}")
    else:
        print("No valid numbers were entered.") 

if __name__ == "__main__":  
    main()
    