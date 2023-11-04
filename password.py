import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    result_label.config(text="Generated Password: " + password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Labels
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

# Entry for password length
length_entry = tk.Entry(root)
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Start the tkinter main loop
root.mainloop()
