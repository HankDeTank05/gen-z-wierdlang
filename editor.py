import tkinter as tk
from tkinter import filedialog

class SimpleCodeEditor:
    def __init__(self, root):
        root.title("Simple Code Editor")
        root.geometry("900x600")

        # Frame for line numbers + text
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        # Line numbers
        self.line_numbers = tk.Text(main_frame, width=4, padx=5, takefocus=0,
                                    border=0, background="lightgray", state="disabled")
        self.line_numbers.pack(side="left", fill="y")

        # Main text editor
        self.text = tk.Text(main_frame, wrap="none", undo=True)
        self.text.pack(side="right", fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.text)
        scrollbar.pack(side="right", fill="y")

        self.text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text.yview)

        # Menu
        menu = tk.Menu(root)
        root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)

        # Events
        self.text.bind("<KeyRelease>", self.update_line_numbers)
        self.text.bind("<MouseWheel>", self.update_line_numbers)

        self.file_path = None
        self.update_line_numbers()

    def update_line_numbers(self, event=None):
        lines = self.text.get("1.0", "end").split("\n")
        line_numbers_string = "\n".join(str(i+1) for i in range(len(lines)))

        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", "end")
        self.line_numbers.insert("1.0", line_numbers_string)
        self.line_numbers.config(state="disabled")

        # Sync scroll
        self.line_numbers.yview_moveto(self.text.yview()[0])

    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
        )

        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()

            self.text.delete("1.0", "end")
            self.text.insert("1.0", content)
            self.update_line_numbers()

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.text.get("1.0", "end-1c"))
        else:
            self.save_as()

    def save_as(self):
        self.file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Python Files", "*.py")]
        )

        if self.file_path:
            self.save_file()


root = tk.Tk()
SimpleCodeEditor(root)
root.mainloop()
