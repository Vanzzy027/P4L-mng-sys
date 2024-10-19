import tkinter as tk
from tkinter import messagebox

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Form")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=tk.W)

        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky=tk.EW)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=1, column=0, padx=(10, 5), pady=5, sticky=tk.W)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=(5, 10), pady=5, sticky=tk.EW)

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=(5, 10), padx=10, sticky=tk.EW)

        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.grid(row=3, column=0, columnspan=2, padx=10, sticky=tk.EW)

        # Configure column and row weights for responsive behavior
        root.columnconfigure(1, weight=1)  # Column with entry widgets
        root.rowconfigure(2, weight=1)     # Row with login button

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Here you can add your authentication logic, for simplicity I'm just checking if fields are empty
        if username == "" or password == "":
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            messagebox.showinfo("Success", "Login successful.")

    def register(self):
        # You can implement the registration form here, similar to the login form
        messagebox.showinfo("Register", "Registration form will be implemented here.")

def main():
    root = tk.Tk()
    app = LoginForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
