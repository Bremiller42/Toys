import os
import math
import pyperclip
import tkinter as tk
from tkinter import ttk


class BigSecretsApp:
    def __init__(self, master):
        self.master = master
        master.title("Big Secrets")
        master.geometry("500x250")
        master.resizable(False, False)

        self.SYMBOLS = '%Q/JiV@m8<X:CH2N[DI43a)KPOzF|bvnq?G5cp(09rLwYjdhef!k1yo*x}A7^ug{~;,tWl6+&TUEMSRs-Z]$.#B> '
        self.keyLength = 0

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky="nsew")

        self.message_label = ttk.Label(self.frame, text="Enter Message:")
        self.message_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        self.message_entry = ttk.Entry(self.frame, width=50)
        self.message_entry.grid(row=0, column=1, sticky="we", padx=5, pady=5)

        self.mode_var = tk.BooleanVar()
        self.toggle_button = ttk.Checkbutton(self.frame, text="Toggle Encrypt/Decrypt", variable=self.mode_var, command=self.toggle_action)
        self.toggle_button.grid(row=1, column=0, padx=5, pady=5)

        self.action_label = ttk.Label(self.frame, text="Mode: Encrypt")
        self.action_label.grid(row=1, column=1, padx=5, pady=5)

        self.copy_label = ttk.Label(self.frame, text="Copied to Clipboard")
        self.copy_label.grid(row=2, column=1, padx=5, pady=5)
        self.copy_label.grid_remove()

        self.process_button = ttk.Button(self.frame, text="Process", command=self.process_message)
        self.process_button.grid(row=2, column=0, padx=5, pady=5)

        self.output_text = tk.Text(master, wrap=tk.WORD, height=5, width=50)
        self.output_text.config(state=tk.DISABLED)
        self.output_text.grid(row=3, column=0, sticky="we", padx=10, pady=10)

        self.message_entry.bind("<Return>", lambda event: self.process_message())

    def clipboardCopy(self, encrypted_message):
        pyperclip.copy(encrypted_message)
        self.copy_label.grid()

    def set_output_text(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert('1.0', text)
        self.output_text.config(state=tk.DISABLED)

    def zipper_merge(self, key, encrypted_message):
        return ''.join(sum(zip(key, encrypted_message), ()))

    def zipper_unmerge(self, entry):
        return entry[::2], entry[1::2]

    def encrypt(self, message, key):
        key = [self.SYMBOLS.index(k) for k in key]
        key_length = len(key)
        encrypted_message = ''

        for i, char in enumerate(message):
            if char in self.SYMBOLS:
                symIndex = self.SYMBOLS.index(char)
                encrypted_message += self.SYMBOLS[(symIndex + key[i % key_length]) % len(self.SYMBOLS)]
            else:
                encrypted_message += char

        return encrypted_message

    def generateKeys(self, keyLength):
        key_parts = []
        for _ in range(keyLength):
            random_bytes = os.urandom(2)
            random_number = int.from_bytes(random_bytes, byteorder='big') % 100
            key_parts.append(f"{random_number:02}")

        key = ''.join(key_parts)
        return key

    def decrypt(self, newMessage, key):
        key = [self.SYMBOLS.index(k) for k in key]
        key_length = len(key)
        decrypted_message = ''

        for i, char in enumerate(newMessage):
            if char in self.SYMBOLS:
                symIndex = self.SYMBOLS.index(char)
                decrypted_message += self.SYMBOLS[(symIndex - key[i % key_length]) % len(self.SYMBOLS)]
            else:
                decrypted_message += char

        return decrypted_message

    def encrypt_message(self):
        message = self.message_entry.get()
        if len(message) % 2 != 0:
            message = f"{message} "
        key_length = math.ceil(len(message) / 2)
        key = self.generateKeys(key_length)
        encrypted_message = self.encrypt(message, key)
        key = key[::-1]
        combined = self.zipper_merge(key, encrypted_message)
        self.clipboardCopy(combined)
        self.set_output_text(f"E: {combined}")

    def decrypt_message(self):
        self.copy_label.grid_remove()
        entry = self.message_entry.get()
        key, new_message = self.zipper_unmerge(entry)
        key = key[::-1]
        decrypted_message = self.decrypt(new_message, key)
        self.set_output_text(f"D: {decrypted_message}")

    def toggle_action(self):
        if self.mode_var.get():
            self.action_label.config(text="Decrypt Selected")
        else:
            self.action_label.config(text="Encrypt Selected")

    def process_message(self):
        if self.mode_var.get():
            self.decrypt_message()
        else:
            self.encrypt_message()
        self.message_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = BigSecretsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
