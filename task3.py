import tkinter as tk
from tkinter import messagebox, scrolledtext
import lyricsgenius

# Initialize Genius API
GENIUS_API_TOKEN = "your_genius_api_token_here"  # Replace with your token
genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

def fetch_lyrics():
    song_title = title_var.get()
    artist_name = artist_var.get()

    if not song_title or not artist_name:
        messagebox.showwarning("Input Error", "Please enter both song title and artist name.")
        return

    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_text.delete("1.0", tk.END)
            lyrics_text.insert(tk.END, song.lyrics)
        else:
            messagebox.showerror("Not Found", "Lyrics not found. Please try another song.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the GUI
root = tk.Tk()
root.title("Lyrics Extractor")

# Input labels and entry fields
tk.Label(root, text="Song Title:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
title_var = tk.StringVar()
tk.Entry(root, textvariable=title_var, width=40).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Artist Name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
artist_var = tk.StringVar()
tk.Entry(root, textvariable=artist_var, width=40).grid(row=1, column=1, padx=10, pady=5)

# Fetch lyrics button
tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics).grid(row=2, column=0, columnspan=2, pady=10)

# Lyrics display
lyrics_text = scrolledtext.ScrolledText(root, wrap="word", width=50, height=20)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Run the main loop
root.mainloop()
