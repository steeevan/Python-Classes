import tkinter as tk
import math

def create_window():
    window = tk.Tk()
    window.title("Unit Converter")
    window.geometry("400x400")
    return window

def meters_to_kilometers(meters):
    return meters / 1000

def inches_to_feet(inches):
    return inches / 12

def grams_to_kilograms(grams):
    return grams / 1000

def pounds_to_ounces(pounds):
    return pounds * 16

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def setup_interface(window):
    tk.Label(window, text="Unit Converter", font=("Arial", 16)).pack(pady=10)

    # Input Field
    tk.Label(window, text="Enter value:").pack()
    value_entry = tk.Entry(window)
    value_entry.pack()

    # Dropdown Menu for Conversion Type
    conversion_type = tk.StringVar(window)
    conversion_type.set("Length")  # default value

    conversion_menu = tk.OptionMenu(window, conversion_type, "Length", "Weight", "Temperature")
    conversion_menu.pack(pady=10)

    # Button to Perform Conversion
    def perform_conversion():
        value = float(value_entry.get())
        conversion = conversion_type.get()

        if conversion == "Length":
            result = meters_to_kilometers(value)
            result_text = f"{value} meters = {result} kilometers"
        elif conversion == "Weight":
            result = grams_to_kilograms(value)
            result_text = f"{value} grams = {result} kilograms"
        elif conversion == "Temperature":
            result = celsius_to_fahrenheit(value)
            result_text = f"{value} Celsius = {result} Fahrenheit"
        
        result_label.config(text=result_text)

    tk.Button(window, text="Convert", command=perform_conversion).pack(pady=10)

    # Label to Display Result
    result_label = tk.Label(window, text="", font=("Arial", 14))
    result_label.pack(pady=10)


def main():
    window = create_window()
    setup_interface(window)
    window.mainloop()

if __name__ == "__main__":
    main()


