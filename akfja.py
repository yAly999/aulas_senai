import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Minha primeira janela")
    root.geometry("800x600")
    root.resizable(True, True)

    label = ttk.Label(root, text="jogo do dino", font=("TkDefaultFont", 50))
    label.pack(pady=100)

    btn = ttk.Button(root, text="fechar", command=root.destroy) 
    btn.pack(anchor="s", pady=15)
    btn.geometry("200x200")

    root.mainloop()

if __name__ == "__main__":
    main()