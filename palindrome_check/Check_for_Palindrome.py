import tkinter as tk
from tkinter import ttk
import string

def palindrome(s):
    s = s.lower().replace(" ", "")
    s = s.translate(str.maketrans('', '', string.punctuation))  # Strip punctuation
    backwards = s[::-1]
    return s == backwards, s, backwards

class PalindromeCheckerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Palindrome Checker")

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.message_label = ttk.Label(self.frame, text="Enter a word to check for palindrome:")
        self.message_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

        self.message_entry = ttk.Entry(self.frame, width=50)
        self.message_entry.grid(row=1, column=0, columnspan=2, sticky="we", padx=5, pady=5)

        self.check_button = ttk.Button(self.frame, text="Check", command=self.check_palindrome)
        self.check_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.input_label = ttk.Label(self.frame, text="Input:")
        self.input_label.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        self.input_value = tk.StringVar()
        self.input_display = ttk.Label(self.frame, textvariable=self.input_value)
        self.input_display.grid(row=4, column=1, sticky="we", padx=5, pady=5)

        self.reversed_label = ttk.Label(self.frame, text="Reversed Input:")
        self.reversed_label.grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)

        self.reversed_value = tk.StringVar()
        self.reversed_display = ttk.Label(self.frame, textvariable=self.reversed_value)
        self.reversed_display.grid(row=5, column=1, sticky="we", padx=5, pady=5)

        self.message_entry.bind("<Return>", lambda event: self.check_palindrome())

        # Configure grid for resizing
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

    def check_palindrome(self):
        word = self.message_entry.get()
        result, original, reversed_word = palindrome(word)
        result_text = "Palindrome" if result else "Not a Palindrome"
        self.result_label.config(text=result_text)
        self.input_value.set(original)
        self.reversed_value.set(reversed_word)


def main():
    root = tk.Tk()
    app = PalindromeCheckerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
