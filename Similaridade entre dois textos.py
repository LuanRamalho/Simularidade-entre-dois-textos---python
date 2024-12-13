import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_similarity(text1, text2):
    # Tokenize the input texts (split them into words)
    tokens1 = text1.split()
    tokens2 = text2.split()

    # Create sets from the tokens to remove duplicates
    set1 = set(tokens1)
    set2 = set(tokens2)

    # Calculate the intersection and union of the sets
    intersection = set1 & set2
    union = set1 | set2

    # Handle empty union case
    if not union:
        return 0

    # Calculate the Jaccard similarity
    similarity = (len(intersection) / len(union)) * 100

    return similarity

def on_calculate():
    text1 = text1_input.get("1.0", tk.END).strip()
    text2 = text2_input.get("1.0", tk.END).strip()

    if not text1 or not text2:
        messagebox.showwarning("Input Error", "Por favor, insira os dois textos.")
        return

    similarity = calculate_similarity(text1, text2)
    result_label.config(text=f"Similaridade: {similarity:.2f}%")

# Create the main application window
root = tk.Tk()
root.title("Similaridade de Textos")
root.geometry("500x600")
root.configure(bg="#f69f40")

# Create a container frame
container = tk.Frame(root, bg="#1e2e2d", padx=20, pady=20)
container.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

# Title
title_label = tk.Label(container, text="Similaridade de Textos", font=("Poppins", 20, "bold"), fg="#f69f40", bg="#1e2e2d")
title_label.pack(pady=(0, 20))

# Text input 1
text1_label = tk.Label(container, text="Entre com o primeiro texto:", font=("Poppins", 12), fg="#a0a0a0", bg="#1e2e2d")
text1_label.pack(anchor="w")
text1_input = tk.Text(container, height=6, bg="#354342", fg="#ffffff", font=("Poppins", 12), wrap=tk.WORD, bd=0, padx=10, pady=10)
text1_input.pack(fill=tk.BOTH, pady=(5, 15))

# Text input 2
text2_label = tk.Label(container, text="Entre com o segundo texto:", font=("Poppins", 12), fg="#a0a0a0", bg="#1e2e2d")
text2_label.pack(anchor="w")
text2_input = tk.Text(container, height=6, bg="#354342", fg="#ffffff", font=("Poppins", 12), wrap=tk.WORD, bd=0, padx=10, pady=10)
text2_input.pack(fill=tk.BOTH, pady=(5, 15))

# Calculate button
calculate_button = tk.Button(
    container,
    text="Calcular Similaridade",
    command=on_calculate,
    bg="#f69f40",
    fg="#1e2e2d",
    font=("Poppins", 12, "bold"),
    bd=0,
    padx=20,
    pady=10,
    activebackground="#f78b30",
    activeforeground="#1e2e2d",
)
calculate_button.pack(pady=20)

# Result label
result_label = tk.Label(container, text="Similaridade: --", font=("Poppins", 16, "bold"), fg="#ffffff", bg="#1e2e2d")
result_label.pack()

# Run the application
root.mainloop()
