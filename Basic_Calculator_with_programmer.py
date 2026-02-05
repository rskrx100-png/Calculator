import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variable to store the expression
        self.expression = ""
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
    
    def create_display(self):
        """Create the display screen"""
        display_frame = tk.Frame(self.root, bg="lightgray", height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 24),
            borderwidth=2,
            relief=tk.SUNKEN,
            justify=tk.RIGHT
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "CE"]
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=("Arial", 18, "bold"),
                    height=2,
                    command=lambda text=btn_text: self.on_button_click(text)
                )
                
                # Grid configuration
                if btn_text == "0":
                    btn.grid(row=row_idx, column=col_idx, columnspan=2, sticky="nsew", padx=5, pady=5)
                elif btn_text == "C":
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
                elif btn_text == "CE":
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
                else:
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=5, pady=5)
                
                # Color coding
                if btn_text in ["/", "*", "-", "+"]:
                    btn.config(bg="orange", fg="white")
                elif btn_text == "=":
                    btn.config(bg="green", fg="white")
                elif btn_text in ["C", "CE"]:
                    btn.config(bg="red", fg="white")
                else:
                    btn.config(bg="lightblue")
        
        # Configure grid weights for resizing
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def programmer_calculation(self, expression):
        """Perform programmer calculations"""
        try:
            result = eval(expression)
            return result
        except:
            return None
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == "C":
            # Clear all
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "CE":
            # Clear last entry
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        elif char == "=":
            # Calculate result by calling programmer_calculation
            result = self.programmer_calculation(self.expression)
            if result is not None:
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            # Append to expression
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()