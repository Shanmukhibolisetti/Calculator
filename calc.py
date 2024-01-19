import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.root.geometry("365x325+550+250")

        self.entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, insertwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            "AC",
            "Del",
            "%",
            "/",
            "7",
            "8",
            "9",
            "*",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "+",
            "%",
            "0",
            ".",
            "=",
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(
                root,
                text=button,
                width=5,
                height=2,
                command=lambda btn=button: self.button_click(btn),
            ).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, value):
        current_text = self.entry.get()

        if value == "=":
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif value == "AC":
            self.entry.delete(0, tk.END)
        elif value == "Del":
            current_text = current_text[:-1]  # Remove the last character
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text)
        else:
            self.entry.insert(tk.END, value)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
