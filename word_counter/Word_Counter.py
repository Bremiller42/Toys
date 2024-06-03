import tkinter as tk
from tkinter import ttk
from collections import OrderedDict
import string

class WordCounterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Word Counter")
        self.master.geometry("450x330")
        self.master.resizable(False, False)

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.input_label = ttk.Label(self.frame, text="Enter a phrase or link to a document:")
        self.input_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)

        self.input_entry = ttk.Entry(self.frame, width=50)
        self.input_entry.grid(row=1, column=0, columnspan=3, sticky="we", padx=5, pady=5)

        self.choose_label = ttk.Label(self.frame, text="Choose: ")
        self.choose_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.choice_var = tk.StringVar()
        self.choice_var.set("p")
        self.phrase_radio = ttk.Radiobutton(self.frame, text="Phrase", variable=self.choice_var, value="p")
        self.phrase_radio.grid(row=2, column=1, padx=5, pady=5)

        self.document_radio = ttk.Radiobutton(self.frame, text="Document", variable=self.choice_var, value="d")
        self.document_radio.grid(row=2, column=2, padx=5, pady=5)

        self.count_button = ttk.Button(self.frame, text="Count Words", command=self.count_words)
        self.count_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

        self.output_text = tk.Text(master, wrap=tk.WORD, height=10, width=50)
        self.output_text.grid(row=1, column=0, columnspan=3, sticky="we", padx=10, pady=10)

        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.output_text.yview)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.output_text.config(yscrollcommand=self.scrollbar.set)

        self.input_entry.bind("<Return>", lambda event: self.count_words())

        # Configure grid for resizing
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)

    def remove_punctuation(self, text):
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    def count_words(self):
        text = self.input_entry.get()
        choice = self.choice_var.get()

        if choice == "p":
            word_counts = self.count_words_from_phrase(text)
        elif choice == "d":
            try:
                with open(text, "r", encoding="utf-8") as f:
                    text = f.read()
                    f.close()
                    word_counts = self.count_words_from_phrase(text)
            except FileNotFoundError:
                self.set_output_text("File not found.")
                return
        else:
            self.set_output_text("Invalid choice.")
            return

        self.set_output_text(word_counts)

    def count_words_from_phrase(self, phrase):
        text_split = self.remove_punctuation(phrase).lower().split()
        total_words = len(text_split)
        word_counts = {}
        for word in text_split:
            word_counts[word] = word_counts.get(word, 0) + 1

        sorted_word_counts = OrderedDict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))

        output_text = f"Total Words: {total_words}\nUnique Words: {len(sorted_word_counts)}\nWord Counts:\n"
        for word, count in sorted_word_counts.items():
            output_text += f"{word}: {count}\n"

        return output_text.strip()

    def set_output_text(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', text)
        self.output_text.config(state=tk.DISABLED)

        # Update height of the output box and position of the scrollbar
        self.output_text.update_idletasks()
        lines = self.output_text.index('end-1c').split('.')[0]
        self.output_text.config(height=min(10, int(lines)))
        self.scrollbar.grid_forget()
        self.scrollbar.grid(row=1, column=3, sticky="ns")




def main():
    root = tk.Tk()
    app = WordCounterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
