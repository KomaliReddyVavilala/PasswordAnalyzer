import tkinter as tk
from tkinter import messagebox
from password_analyzer import analyze_password
from wordlist_generator import generate_wordlist

def analyze():
    password = entry_password.get()
    analyze_password(password)

def generate():
    keywords = entry_keywords.get().split()
    years = entry_years.get().split()
    generate_wordlist(keywords, years, "custom_wordlist.txt")
    messagebox.showinfo("Success", "Wordlist generated!")

app = tk.Tk()
app.title("Password Tool")

# Password Analyzer
tk.Label(app, text="Password Analyzer").pack()
entry_password = tk.Entry(app, width=30)
entry_password.pack()
tk.Button(app, text="Analyze", command=analyze).pack()

# Wordlist Generator
tk.Label(app, text="\nWordlist Generator").pack()
tk.Label(app, text="Keywords (space-separated):").pack()
entry_keywords = tk.Entry(app, width=30)
entry_keywords.pack()
tk.Label(app, text="Years (space-separated):").pack()
entry_years = tk.Entry(app, width=30)
entry_years.pack()
tk.Button(app, text="Generate Wordlist", command=generate).pack()

app.mainloop()
