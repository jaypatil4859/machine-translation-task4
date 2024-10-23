import tkinter as tk
from tkinter import messagebox
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

def load_translations(french_file, tamil_file):
    with open(french_file, 'r', encoding='utf-8') as file:
        french_sentences = file.read().strip().split('\n')
    with open(tamil_file, 'r', encoding='utf-8') as file:
        tamil_sentences = file.read().strip().split('\n')
    return dict(zip(french_sentences, tamil_sentences))

def suggest_similar_words(word, word_list):
    from difflib import get_close_matches
    return get_close_matches(word, word_list)

def translate_to_tamil(sentence, french_to_tamil, french_sentences, wrong_words):
    tamil_translation = french_to_tamil.get(sentence)
    if tamil_translation:
        return f"Tamil Translation: {tamil_translation}", ""
    else:
        suggestions = suggest_similar_words(sentence, french_sentences)
        wrong_words.append(sentence)
        if len(wrong_words) > 1:
            return f"Word not found. Wrong words so far: {wrong_words}. Suggestions: {suggestions}", "Error"
        return f"Word not found. Suggestions: {suggestions}", "Error"

def on_translate_click():
    sentence = entry.get()
    french_to_tamil = load_translations("data4/french.txt", "data4/tamil.txt")
    wrong_words = []
    tamil, error = translate_to_tamil(sentence, french_to_tamil, list(french_to_tamil.keys()), wrong_words)
    if error:
        messagebox.showerror("Error", tamil)
    else:
        tamil_label.config(text=tamil)

# Load model (example file path)
model = load_model("french_to_tamil_model.h5")

# GUI setup
root = tk.Tk()
root.title("Translator GUI")
tk.Label(root, text="Enter a French word:").grid(row=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)
tk.Button(root, text="Translate", command=on_translate_click).grid(row=1, columnspan=2)
tamil_label = tk.Label(root, text="")
tamil_label.grid(row=2, columnspan=2)
root.mainloop()


