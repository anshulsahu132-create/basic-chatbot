#<<<<<< # Smart ChatBot >>>>>>
import customtkinter as ctk
from datetime import datetime
from chatbot import get_response
from utils import save_chat
import pyttsx3
import threading

# Theme Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
engine = pyttsx3.init()

voices = engine.getProperty("voices")

# Male Voice
engine.setProperty("voice", voices[0].id)

engine.setProperty("rate", 170)      # Speed
engine.setProperty("volume", 1.0)    # Volume
app = ctk.CTk()
app.title("🤖 Smart ChatBot")
app.geometry("1200x750")
app.minsize(1200, 750)

# Colors
PRIMARY = "#2563EB"
BACKGROUND = "#0F172A"
SIDEBAR = "#111827"
BOT_COLOR = "#2563EB"
USER_COLOR = "#16A34A"

chat_history = []
message_count = 0

def _speak(text):
    engine = pyttsx3.init()          # Har baar naya engine
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 170)
    engine.setProperty("volume", 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def speak(text):
    threading.Thread(target=_speak, args=(text,), daemon=True).start()
# Add Message
def add_message(sender, message):

    if sender == "user":
        color = USER_COLOR
        anchor = "e"
        icon = "🧑"
    else:
        color = BOT_COLOR
        anchor = "w"
        icon = "🤖"

    bubble = ctk.CTkLabel(
        chat_frame,
        text=f"{icon}  {message}",
        fg_color=color,
        corner_radius=20,
        text_color="white",
        font=("Segoe UI", 15),
        justify="left",
        wraplength=550,
        padx=15,
        pady=12
    )

    bubble.pack(
        anchor=anchor,
        padx=10,
        pady=5
    )
    from datetime import datetime
    time_label = ctk.CTkLabel(
    chat_frame,
    text=datetime.now().strftime("%I:%M %p"),
    font=("Segoe UI", 10),
    text_color="gray70"
)
    time_label.pack(anchor=anchor, padx=15)
    chat_frame.update_idletasks()
    chat_frame._parent_canvas.yview_moveto(1.0)

    chat_frame._parent_canvas.yview_moveto(1.0)

# Send Message
def send_message():
    global message_count
    user_message = message_entry.get().strip()
    if user_message == "":
        return

    add_message("user", user_message)

    chat_history.append(f"You : {user_message}")
    message_count += 1
    typing = ctk.CTkLabel(
    chat_frame,
    text="🤖 Typing...",
    text_color="gray"
)   
    typing.pack(anchor="w", padx=10)
    app.update()
    set_status("🤖 Thinking...")
    reply = get_response(user_message)
    typing.destroy()
    add_message("bot", reply)
    speak(reply)
    set_status("🟢 AI Online")
    chat_history.append(f"Bot : {reply}")

    message_entry.delete(0, "end")
main_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

# Save Chat
def save_chat_history():

    save_chat("\n".join(chat_history))

# New Chat
def clear_chat():
    chat_history.clear()

    for widget in chat_frame.winfo_children():
        widget.destroy()

    add_message("bot", "👋 New chat started.")
    add_message("bot", "How can I help you today?")

# Change Theme
def change_theme(mode):
    ctk.set_appearance_mode(mode)

# Settings Window
def open_settings():

    settings = ctk.CTkToplevel(app)

    settings.title("Settings")

    settings.geometry("350x220")

    settings.resizable(False, False)

    title = ctk.CTkLabel(
        settings,
        text="⚙ Settings",
        font=("Segoe UI", 22, "bold")
    )
    title.pack(pady=20)
    dark_btn = ctk.CTkButton(
        settings,
        text="🌙 Dark Mode",
        command=lambda: change_theme("dark")
    )
    dark_btn.pack(pady=10)

    light_btn = ctk.CTkButton(
        settings,
        text="☀ Light Mode",
        command=lambda: change_theme("light")
    )

    light_btn.pack(pady=10)

# About Window
def open_about():
    about = ctk.CTkToplevel(app)
    about.title("About")
    about.geometry("420x300")
    about.resizable(False, False)
    title = ctk.CTkLabel(
        about,
        text="🤖 Smart ChatBot",
        font=("Segoe UI", 22, "bold")
    )

    title.pack(pady=20)
    info = ctk.CTkLabel(
        about,
        text=(
            "Version : 1.0\n\n"
            "Developed using Python & CustomTkinter\n\n"
            "Features:\n"
            "• AI Chat\n"
            "• Save Chat\n"
            "• Chat History\n"
            "• Dark / Light Theme\n"
            "• Professional GUI"
        ),
        justify="left",
        font=("Segoe UI", 14)
    )

    info.pack(pady=10)

# Chat Statistics
def open_statistics():
    stats = ctk.CTkToplevel(app)

    stats.title("Chat Statistics")

    stats.geometry("350x220")

    title = ctk.CTkLabel(
        stats,
        text="📊 Chat Statistics",
        font=("Segoe UI",20,"bold")
    )

    title.pack(pady=20)

    info = ctk.CTkLabel(
        stats,
        text=f"Total Messages : {message_count}\n\nConversation Lines : {len(chat_history)}",
        font=("Segoe UI",15)
    )

    info.pack(pady=15)

main_frame.pack(
    fill="both",
    expand=True
)
sidebar = ctk.CTkFrame(
    main_frame,
    width=248,
    corner_radius=0,
    fg_color="#111827"
)

sidebar.pack(
    side="left",
    fill="y"
)

sidebar.pack_propagate(False)

logo = ctk.CTkLabel(
    sidebar,
    text="🤖\nSmart\nChatBot",
    font=("Segoe UI", 28, "bold"),
    justify="center"
)

logo.pack(
    pady=(30, 20)
)
new_chat_btn = ctk.CTkButton(
    sidebar,
    text="💬 New Chat",
    width=180,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 15),
    command=clear_chat
)

new_chat_btn.pack(pady=10)

save_btn = ctk.CTkButton(
    sidebar,
    text="💾 Save Chat",
    width=180,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 15),
    command=save_chat_history
)

save_btn.pack(pady=10)

history_btn = ctk.CTkButton(
    sidebar,
    text="📂 History",
    width=180,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 15)
)

history_btn.pack(pady=10)

settings_btn = ctk.CTkButton(
    sidebar,
    text="⚙️ Settings",
    width=180,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 15),
    command=open_settings
)

settings_btn.pack(pady=10)

about_btn = ctk.CTkButton(
    sidebar,
    text="ℹ️ About",
    width=180,
    height=45,
    corner_radius=15,
    font=("Segoe UI", 15),
    command=open_about
)
about_btn.pack(pady=10)
stats_btn = ctk.CTkButton(
    sidebar,
    text="📊 Statistics",
    width=180,
    height=45,
    corner_radius=15,
    font=("Segoe UI",15),
    command=open_statistics
)

stats_btn.pack(pady=10)
right_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

right_frame.pack(
    side="left",
    fill="both",
    expand=True
)
header = ctk.CTkFrame(
    right_frame,
    height=75,
    fg_color=PRIMARY,
    corner_radius=0
)

header.pack(
    fill="x"
)

header.pack_propagate(False)
title = ctk.CTkLabel(
    header,
    text="🤖 Smart ChatBot",
    font=("Segoe UI", 26, "bold"),
    text_color="white"
)

title.pack(
    side="left",
    padx=20
)

status = ctk.CTkLabel(
    header,
    text="🟢AI Online",
    font=("Segoe UI", 15),
    text_color="white"
)

status.pack(
    side="right",
    padx=20
)
def set_status(text):

    status.configure(text=text)

# Chat Area
chat_frame = ctk.CTkScrollableFrame(
    right_frame,
    corner_radius=10,
    fg_color="#1E293B"
)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)

# Welcome Message
welcome = ctk.CTkLabel(
    chat_frame,
    text="👋 Welcome to Smart ChatBot\n\nAsk me anything...",
    font=("Segoe UI", 18),
    justify="center"
)

welcome.pack(pady=30)
add_message("bot", "Hello! 👋")
add_message("bot", "I'm Smart ChatBot. How can I help you today?")

# Bottom Frame
bottom_frame = ctk.CTkFrame(
    right_frame,
    height=70
)
bottom_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

# Message Entry
message_entry = ctk.CTkEntry(
    bottom_frame,
    placeholder_text="Type your message here...",
    corner_radius=20,
    height=50,
    font=("Segoe UI", 15)
)

message_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(10, 5),
    pady=10
)

# Send Button
send_btn = ctk.CTkButton(
    bottom_frame,
    text="📤 Send",
    corner_radius=20,
    height=50,
    font=("Segoe UI",15,"bold"),
    width=120,
    command=send_message
)

send_btn.pack(
    side="right",
    padx=(5, 10),
    pady=10
)
message_entry.bind("<Return>", lambda event: send_message())
app.bind("<Escape>", lambda e: clear_chat())
from tkinter import messagebox


def on_close():

    if messagebox.askyesno("Exit","Do you really want to exit?"):
        app.destroy()


app.protocol("WM_DELETE_WINDOW", on_close)
app.mainloop()