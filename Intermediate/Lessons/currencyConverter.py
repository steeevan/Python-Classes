import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Currency Converter")

        # Predefined exchange rates relative to USD
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.75,
            'INR': 74.35,
            'AUD': 1.35,
            'CAD': 1.25,
            'JPY': 110.0,
            'CNY': 6.47,
            'MXN': 20.15
        }

        # Labels and Entry fields
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(column=0, row=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(column=1, row=0, padx=10, pady=10)

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.grid(column=0, row=1, padx=10, pady=10)
        self.from_currency_combobox = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.from_currency_combobox.grid(column=1, row=1, padx=10, pady=10)

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.grid(column=0, row=2, padx=10, pady=10)
        self.to_currency_combobox = ttk.Combobox(root, values=list(self.exchange_rates.keys()))
        self.to_currency_combobox.grid(column=1, row=2, padx=10, pady=10)

        # Convert Button
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.grid(column=0, row=3, columnspan=2, pady=20)

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(column=0, row=4, columnspan=2, pady=10)

    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()

            if from_currency and to_currency:
                converted_amount = amount * self.exchange_rates[to_currency] /
