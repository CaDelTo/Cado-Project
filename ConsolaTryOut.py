import tkinter as tk
from tkinter import simpledialog

def main():
    root = tk.Tk()
    root.withdraw()
    value = simpledialog.askstring("Entrada", "Ingresa un valor:")
    root = tk.Tk()
    root.withdraw()
    value = simpledialog.askstring("Entrada", "Ingresa un valor:")
    if value is not None:
        print("Valor ingresado:", value)
    else:
        print("Ningún valor ingresado.")

if __name__ == "__main__":
    main()
