import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.entry = tk.Entry(root, width=100, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=10, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text="Clear", width=21, command=self.clear_entry).grid(row=row_val, column=0, columnspan=2)
        tk.Button(self.root, text="Delete", width=21, command=self.delete_char).grid(row=row_val, column=2, columnspan=2)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def delete_char(self):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current[:-1])

root = tk.Tk()
root.title("Calculator")
calc = Calculator(root)
root.mainloop()
