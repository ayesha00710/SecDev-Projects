import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to check password strength based on its characters
def check_strength(password):
    length = len(password)  # Get the length of the password

    # Check if the password contains at least one uppercase letter, one lowercase letter,
    # one digit, and optionally one symbol.
    has_upper = any(c.isupper() for c in password)    # A-Z
    has_lower = any(c.islower() for c in password)    # a-z
    has_digit = any(c.isdigit() for c in password)    # 0-9
    has_symbol = any(c in string.punctuation for c in password)  # !@#$...

    # Add up how many types of characters are present in the password
    score = sum([has_upper, has_lower, has_digit, has_symbol])

    # Determine password strength based on length and character types
    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"

# Function to generate a random password with guaranteed complexity
def generate_password(length, use_symbols=True):
    # Ensure the password has a minimum length of 4 for complexity
    if length < 4:
        raise ValueError("Password should be at least 4 characters long.")

    # Start with one character from each required category: lowercase, uppercase, digit
    password_chars = [
        random.choice(string.ascii_lowercase),  # Pick a random lowercase letter
        random.choice(string.ascii_uppercase),  # Pick a random uppercase letter
        random.choice(string.digits)            # Pick a random digit
    ]

    # If the user wants symbols, add one symbol to the password
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))
        # Allow all letters, digits, and punctuation symbols
        allowed_chars = string.ascii_letters + string.digits + string.punctuation
    else:
        # Only allow letters and digits if no symbols are requested
        allowed_chars = string.ascii_letters + string.digits

    # Fill the remaining length of the password with random characters from allowed_chars
    while len(password_chars) < length:
        password_chars.append(random.choice(allowed_chars))

    # Shuffle the characters to avoid predictable patterns
    random.shuffle(password_chars)

    # Join the list of characters into a string and return it
    return ''.join(password_chars)

# Function to handle password generation and update the UI
def generate():
    try:
        length = int(entry_length.get())  # Get the length from the user input
        use_symbols = var_symbols.get()   # Get whether symbols should be included

        # Generate the password
        password = generate_password(length, use_symbols)

        # Check the strength of the password
        strength = check_strength(password)

        # Display the password and strength in the labels
        label_password.config(text=f"Generated Password: {password}")
        label_strength.config(text=f"Password Strength: {strength}")
    
    except ValueError as e:
        messagebox.showerror("Error", str(e))  # Show error if input is invalid

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a frame for the layout
frame = tk.Frame(root)
frame.pack(pady=20)

# Label to explain the password length input
label_length = tk.Label(frame, text="Enter Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=5)

# Entry widget for password length input
entry_length = tk.Entry(frame)
entry_length.grid(row=0, column=1, padx=10, pady=5)

# Checkbutton to ask if symbols should be included
var_symbols = tk.BooleanVar()
check_symbols = tk.Checkbutton(frame, text="Include Symbols?", variable=var_symbols)
check_symbols.grid(row=1, columnspan=2, pady=5)

# Button to generate the password
button_generate = tk.Button(frame, text="Generate Password", command=generate)
button_generate.grid(row=2, columnspan=2, pady=10)

# Labels to display the generated password and its strength
label_password = tk.Label(root, text="Generated Password: ")
label_password.pack(pady=10)

label_strength = tk.Label(root, text="Password Strength: ")
label_strength.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
