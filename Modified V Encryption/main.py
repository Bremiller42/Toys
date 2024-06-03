"""
A Custom modified vigenere encryption program for encrypting messages before sending. 
"""


import keyGen
import math
import pyperclip
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Big Secrets")

SYMBOLS = '%Q/JiV@m8<X:CH2N[DI43a)KPOzF|bvnq?G5cp(09rLwYjdhef!k1yo*x}A7^ug{~;,tWl6+&TUEMSRs-Z]$.#B> '
keyLength = 0


def clipboardCopy(encrypted_message):
    pyperclip.copy(encrypted_message)


def set_output_text(text):
    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert('1.0', text)
    output_text.config(state=tk.DISABLED)


def zipper_merge(key, encrypted_message):
    return ''.join(sum(zip(key, encrypted_message), ()))


def zipper_unmerge(entry):
    return entry[::2], entry[1::2]


# def handleKey(key, encrypting=True):
#     # Check if we are encrypting or decrypting
#     if encrypting:
#         # For encryption: Move the first two elements to the end of the key list
#         return key[1:] + key[:1]
#     else:
#         # For decryption: Move the last two elements to the front of the key list
#         return key[-1:] + key[:-1]


def encrypt(message, key):
    key = [SYMBOLS.index(k) for k in key]
    key_length = len(key)
    encrypted_message = ''
    message_length = len(message)

    for i, char in enumerate(message):
        if char in SYMBOLS:
            symIndex = SYMBOLS.index(char)
            encrypted_message += SYMBOLS[(symIndex + key[i % key_length]) % len(SYMBOLS)]

        else:
            encrypted_message += char
        # if i < message_length - 1:
        #     key = handleKey(key, encrypting=True)
    return encrypted_message


def decrypt(newMessage, key):
    key = [SYMBOLS.index(k) for k in key]
    key_length = len(key)
    decrypted_message = ''
    message_length = len(newMessage)

    for i, char in enumerate(newMessage):
        if char in SYMBOLS:
            symIndex = SYMBOLS.index(char)
            decrypted_message += SYMBOLS[(symIndex - key[i % key_length]) % len(SYMBOLS)]

        else:
            decrypted_message += char
        # if i < message_length - 1:
        #     key = handleKey(key, encrypting=False)
    return decrypted_message


def encrypt_message():
    message = message_entry.get()
    if len(message) % 2 != 0:
        message = f"{message} "
    key_length = math.ceil(len(message) / 2)
    key = keyGen.generateKeys(key_length)
    encrypted_message = encrypt(message, key)
    key = key[::-1]
    combined = zipper_merge(key, encrypted_message)
    clipboardCopy(combined)
    set_output_text(f"E: {combined}")


def decrypt_message():
    entry = message_entry.get()
    key, new_message = zipper_unmerge(entry)
    key = key[::-1]
    decrypted_message = decrypt(new_message, key)
    set_output_text(f"D: {decrypted_message}")


def toggle_action():
    if mode_var.get():
        action_label.config(text="Decrypt Selected")
    else:
        action_label.config(text="Encrypt Selected")

def process_message():
    if mode_var.get():
        decrypt_message()
    else:
        encrypt_message()
    message_entry.delete(0, tk.END)


frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

message_label = ttk.Label(frame, text="Enter Message:")
message_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

message_entry = ttk.Entry(frame, width=50)
message_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

mode_var = tk.BooleanVar()
toggle_button = ttk.Checkbutton(frame, text="Toggle Encrypt/Decrypt", variable=mode_var, command=toggle_action)
toggle_button.grid(row=1, column=0, padx=5, pady=5)

action_label = ttk.Label(frame, text="Mode: Encrypt")
action_label.grid(row=1, column=1, padx=5, pady=5)

process_button = ttk.Button(frame, text="Process", command=process_message)
process_button.grid(row=2, column=0, padx=5, pady=5)

output_text = tk.Text(root, height=5, width=50)
output_text.config(state=tk.DISABLED)
output_text.grid(row=3, column=0, sticky=(tk.W, tk.E), padx=10, pady=10)



message_entry.bind("<Return>", lambda event: process_message())

if __name__ == "__main__":
    try:
        root.mainloop()
    except KeyboardInterrupt:
        exit()
