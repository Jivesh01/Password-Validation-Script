# Step 1: Prompt the user to enter a password
password = input("enter the password :")

# Step 2: Check if the password is shorter than 8 characters
if len(password) < 8:
    print("password is too short")  # Step 2a: Inform the user if the password is too short

# Step 3: Check if the password consists only of lowercase letters
elif password.islower():
    print("password is too weak")  # Step 3a: Inform the user if the password is too weak

# Step 4: If the password passes the previous checks, classify it as strong
else:
    print("password is strong")  # Step 4a: Inform the user that the password is strong
