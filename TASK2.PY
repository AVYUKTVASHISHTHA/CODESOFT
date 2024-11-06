import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)

        self.expression = ""

        # Entry widget to display the expression
        self.display = tk.Entry(self.root, font=('Arial', 24), borderwidth=5, relief='ridge')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, font=('Arial', 18), borderwidth=3, relief='ridge',
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, sticky='nsew', padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights for responsive layout
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += button
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()