import tkinter as tk  # Import the tkinter module for GUI
from tkinter import ttk, messagebox  # Import additional tkinter modules

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Currency Converter")  # Set the window title

        # Dictionary of exchange rates relative to USD
        self.exchange_rates = {
            "USD": 1.0,
            "EUR": 0.9,
            "GBP": 0.76,
            "INR": 83.94,
            "AUD": 1.47,
            "CAD": 1.35,
            "JPY": 144.26,
            "CNY": 7.13,
            "MXN": 19.69,
            "CHF": 0.93,
            "NZD": 1.62,
            "ZAR": 18.55
        }

        # Amount label
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)
        # Amount Entry field
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)
        # From Currency label
        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.grid(column=0, row=1, padx=10, pady=10)
        # Dropdown (Combobox) for selecting the "from" currency
        self.from_currency_combobox = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.from_currency_combobox.grid(column=1, row=1, padx=10, pady=10)
        self.from_currency_combobox.set("USD")  # Default selection
        # To Currency label
        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.grid(column=0, row=2, padx=10, pady=10)
        # Dropdown (Combobox) for selecting the "to" currency
        self.to_currency_combobox = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.to_currency_combobox.grid(column=1, row=2, padx=10, pady=10)
        self.to_currency_combobox.set('EUR')  # Default selection
        # Convert button
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=3, columnspan=2, pady=10)
        # Result label
        self.result_label = tk.Label(root, text="X")
        self.result_label.grid(column=0, row=4, columnspan=2, pady=10)

    # Function to perform the currency conversion
    def convert_currency(self):
        try:
            # Retrieve the amount and currency selections from the user input
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()

            # If the selected currencies are the same, display the amount as is
            if from_currency == to_currency:
                self.result_label.config(text=f'Amount in {to_currency}: {amount:.2f}')
                return

            # Conversion logic
            if from_currency and to_currency:
                # Convert the amount to USD
                amount_in_usd = amount / self.exchange_rates[from_currency]
                # Convert the USD amount to the target currency
                converted_amount = amount_in_usd * self.exchange_rates[to_currency]

                # Update the result label with the converted amount
                self.result_label.config(text=f'Amount in {to_currency}: {converted_amount:.2f}')
            else:
                messagebox.showerror("Input Error", "Please enter an amount and select both currencies.")
            
        except ValueError:
            messagebox.showerror("Input Error", "Invalid amount. Please enter a numerical value.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = CurrencyConverterApp(root)  # Initialize the CurrencyConverterApp class
    root.mainloop()  # Start the main event loop
