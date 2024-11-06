import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.config(bg="#f2f2f2")  # Light gray background

        self.title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold"), bg="#f2f2f2")
        self.title_label.pack(pady=10)

        self.length_label = tk.Label(root, text="Enter password length:", font=("Arial", 14), bg="#f2f2f2")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(root, font=("Arial", 14), width=5, borderwidth=2, relief="solid")
        self.length_entry.pack(pady=5)

        # Checkboxes for character types
        self.include_uppercase = tk.BooleanVar()
        self.include_lowercase = tk.BooleanVar()
        self.include_digits = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase, font=("Arial", 12), bg="#f2f2f2").pack(anchor='w')
        tk.Checkbutton(root, text="Include Lowercase Letters", variable=self.include_lowercase, font=("Arial", 12), bg="#f2f2f2").pack(anchor='w')
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits, font=("Arial", 12), bg="#f2f2f2").pack(anchor='w')
        tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special, font=("Arial", 12), bg="#f2f2f2").pack(anchor='w')

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised")
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333")
        self.password_label.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Length must be at least 1.")

            # Define the character set based on user preferences
            characters = ""
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_lowercase.get():
                characters += string.ascii_lowercase
            if self.include_digits.get():
                characters += string.digits
            if self.include_special.get():
                characters += string.punctuation

            if not characters:  # If no options were selected
                self.password_label.config(text="Please select at least one character type.")
                return

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError:
            self.password_label.config(text="Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()