import math
import tkinter as tk
from tkinter import ttk


class PiToNthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pi to the Nth Digit")
        self.root.geometry("425x150")
        self.create_widgets()

    def calculate_pi(self):
        try:
            number = int(self.entry.get())
            if 0 < number < 49:
                formatted_pi = f"{math.pi:.{number}f}"
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, formatted_pi)
            else:
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, "Invalid Entry, Max is 48")
        except ValueError:
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, "Invalid entry, enter a number between 1 and 48")
        self.entry.delete(0, tk.END)

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Enter a number for decimal places of Pi:")
        self.label.pack(side=tk.TOP, padx=5, pady=5)

        self.entry = ttk.Entry(self.root, width=10)
        self.entry.pack(side=tk.TOP, padx=5, pady=5)
        self.entry.bind('<Return>', lambda event: self.calculate_pi())

        self.button = ttk.Button(self.root, text="Calculate", command=self.calculate_pi)
        self.button.pack(side=tk.TOP, padx=5, pady=5)

        self.result_text = tk.Text(self.root, wrap=tk.WORD)
        self.result_text.pack(side=tk.TOP, padx=5, pady=5, expand=True, fill=tk.BOTH)


def main():
    root = tk.Tk()
    app = PiToNthApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
