from datetime import datetime
from tkinter import messagebox
import os

# Current Time
def get_current_time():
    return datetime.now().strftime("%I:%M %p")

# Current Date
def get_current_date():
    return datetime.now().strftime("%d %B %Y")

# Save Chat
def save_chat(chat_history):

    try:

        with open("chat_history.txt", "w", encoding="utf-8") as file:
            file.write(chat_history)

        messagebox.showinfo(
            "Success",
            "Chat saved successfully!"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"Unable to save chat.\n\n{e}"
        )

# Load Chat
def load_chat():

    if not os.path.exists("chat_history.txt"):
        return ""

    with open("chat_history.txt", "r", encoding="utf-8") as file:
        return file.read()

# Clear Chat File
def clear_chat_file():

    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write("")