import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")
        self.root.geometry("800x600")

        # Create a text area
        self.text_area = tk.Text(self.root, undo=True, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"))
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"))

        # Search menu
        self.search_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Search", menu=self.search_menu)
        self.search_menu.add_command(label="Find", command=self.find_text)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    def exit_app(self):
        self.root.quit()

    def find_text(self):
        self.search_toplevel = tk.Toplevel(self.root)
        self.search_toplevel.title("Find Text")
        self.search_toplevel.geometry("300x50")
        
        self.search_label = tk.Label(self.search_toplevel, text="Find:")
        self.search_label.pack(side=tk.LEFT, padx=10)
        
        self.search_entry = tk.Entry(self.search_toplevel, width=20)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        
        self.search_button = tk.Button(self.search_toplevel, text="Find", command=self.search)
        self.search_button.pack(side=tk.LEFT, padx=10)

    def search(self):
        self.text_area.tag_remove("highlight", '1.0', tk.END)
        search_text = self.search_entry.get()
        if search_text:
            start_pos = '1.0'
            while True:
                start_pos = self.text_area.search(search_text, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_text)}c"
                self.text_area.tag_add("highlight", start_pos, end_pos)
                start_pos = end_pos
            self.text_area.tag_config("highlight", background="yellow", foreground="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
