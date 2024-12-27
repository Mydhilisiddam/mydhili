import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Sample pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there!"]),
    (r"what is your name\??", ["I am a chatbot. What's yours?"]),
    (r"how are you\??", ["I'm just a bot, but I'm doing well! How about you?"]),
    (r"what can you do\??", ["I can chat with you. Try asking me questions!"]),
    (r"bye|exit|quit", ["Goodbye! Have a great day!", "See you later!"]),
    (r"(.*)", ["I am not sure I understand, but I'm here to help!"]),
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Function to handle sending a message
def send_message():
    user_input = user_entry.get()
    if not user_input.strip():
        return
    chat_history.insert(tk.END, f"You: {user_input}\n")
    response = chatbot.respond(user_input)
    chat_history.insert(tk.END, f"Bot: {response}\n")
    user_entry.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Chatbot")

chat_history = scrolledtext.ScrolledText(root, state='disabled', wrap='word', width=50, height=20)
chat_history.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

user_entry = tk.Entry(root, width=40)
user_entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Run the main loop
root.mainloop()
