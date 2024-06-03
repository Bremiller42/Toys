import tkinter as tk
from tkinter import ttk


class FibonacciSequenceGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Sequence Generator")
        self.create_widgets()

    def fibonacci(self, n):
        n1 = 0
        n2 = 1
        fibonacci = []
        fibonacci.append(n1)
        fibonacci.append(n2)
        for i in range(1, n):
            n3 = n1 + n2
            fibonacci.append(n3)
            n1 = n2
            n2 = n3
        return fibonacci

    def generate_fibonacci(self):
        try:
            n = int(self.entry.get()) - 1
            if n < 500:
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, ', '.join(map(str, self.fibonacci(n))))
            else:
                self.result_text.delete('1.0', tk.END)
                self.result_text.insert(tk.END, "Invalid input, please select a number between 3 and 500")
        except ValueError:
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, "Invalid input, please enter a valid number")

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.pack(expand=True, fill=tk.BOTH)

        self.label = ttk.Label(self.frame, text="Enter a number to generate the Fibonacci sequence:")
        self.label.pack(padx=5, pady=5)

        self.entry = ttk.Entry(self.frame, width=20)
        self.entry.pack(padx=5, pady=5)
        self.entry.bind('<Return>', lambda event: self.generate_fibonacci())

        self.button = ttk.Button(self.frame, text="Generate", command=self.generate_fibonacci)
        self.button.pack(padx=5, pady=5)

        self.result_text = tk.Text(self.frame, wrap=tk.WORD, height=10)
        self.result_text.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)

def main():
    root = tk.Tk()
    app = FibonacciSequenceGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
