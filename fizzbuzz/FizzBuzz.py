import tkinter as tk
from tkinter import ttk

class FizzBuzzGUI:
    def __init__(self, master):
        self.master = master
        master.title("FizzBuzz Generator")

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.number_label = ttk.Label(self.frame, text="Enter a number to FizzBuzz to:")
        self.number_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.number_entry = ttk.Entry(self.frame, width=10)
        self.number_entry.grid(row=0, column=1, sticky="we", padx=5, pady=5)

        self.generate_button = ttk.Button(self.frame, text="Generate FizzBuzz", command=self.generate_fizzbuzz)
        self.generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.output_text = tk.Text(master, wrap=tk.WORD, height=10, width=50)
        self.output_text.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=10)

        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.output_text.yview)
        self.scrollbar.grid(row=1, column=2, sticky="ns")
        self.output_text.config(yscrollcommand=self.scrollbar.set)

        self.number_entry.bind("<Return>", lambda event: self.generate_fizzbuzz())

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def fizzbuzz(self, n):
        fizzbuzz_output = ""
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                fizzbuzz_output += "FizzBuzz\n"
            elif num % 3 == 0:
                fizzbuzz_output += "Fizz\n"
            elif num % 5 == 0:
                fizzbuzz_output += "Buzz\n"
            else:
                fizzbuzz_output += f"{num}\n"
        return fizzbuzz_output.strip()

    def generate_fizzbuzz(self):
        try:
            number = int(self.number_entry.get())
            if number <= 0:
                self.set_output_text("Please enter a positive integer.")
            else:
                fizzbuzz_output = self.fizzbuzz(number)
                self.set_output_text(fizzbuzz_output)
        except ValueError:
            self.set_output_text("Please enter a valid number.")

    def set_output_text(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', text)
        self.output_text.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = FizzBuzzGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
