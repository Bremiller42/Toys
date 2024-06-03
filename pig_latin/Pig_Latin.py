import tkinter as tk
from tkinter import ttk

class PigLatinTranslatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Pig Latin Translator")
        master.geometry("500x250")
        master.resizable(True, True)  # Allow both width and height to be resizable

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.message_label = ttk.Label(self.frame, text="Enter a phrase to translate:")
        self.message_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)

        self.message_entry = ttk.Entry(self.frame, width=50)
        self.message_entry.grid(row=1, column=0, columnspan=2, sticky="we", padx=5, pady=5)

        self.translate_to_button = ttk.Button(self.frame, text="Translate to Pig Latin", command=self.translate_to_piglatin)
        self.translate_to_button.grid(row=2, column=0, padx=5, pady=5)

        self.translate_from_button = ttk.Button(self.frame, text="Translate from Pig Latin", command=self.translate_from_piglatin)
        self.translate_from_button.grid(row=2, column=1, padx=5, pady=5)

        self.output_text = tk.Text(master, wrap=tk.WORD, height=5, width=50)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.grid(row=1, column=0, columnspan=2, sticky="we", padx=10, pady=10)

        self.message_entry.bind("<Return>", lambda event: self.translate_to_piglatin())

        # Configure grid for resizing
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(1, weight=1)

    def translate_to_piglatin(self):
        phrase = self.message_entry.get()
        translated_phrase = self.pig_latin(phrase)
        self.set_output_text(translated_phrase)

    def translate_from_piglatin(self):
        phrase = self.message_entry.get()
        translated_phrase = self.translate_back(phrase)
        self.set_output_text(translated_phrase)

    def set_output_text(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', text)
        self.output_text.config(state=tk.DISABLED)

    def translate_back(self, text):
        say = ""
        words = text.split()
        for word in words:
            word = word[:-2]
            say += word[-1] + word[:-1] + " "
        return say.strip()

    def pig_latin(self, text):
        say = ""
        words = text.lower().split()
        for word in words:
            say += word[1:] + word[0] + "ay "
        return say.strip()


def main():
    root = tk.Tk()
    app = PigLatinTranslatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
