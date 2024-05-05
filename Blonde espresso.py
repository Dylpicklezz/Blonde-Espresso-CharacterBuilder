import tkinter as tk

def clear_text():
    text_box.delete(1.0, tk.END)

def create_text(button_text):
    clear_text()
    for line in button_text.split("\n"):
        text_box.insert(tk.END, line + "\n")

# Blonde Espresso theme colors
background_color = "#F5DEB3"  # Wheat
button_color = "#D2B48C"      # Tan
text_color = "#000000"         # Black

root = tk.Tk()
root.title("Blonde Espresso Build Maker !!!!Beta!!!!")
root.config(bg=background_color)

# Create a text box
text_box = tk.Text(root, height=10, width=50, bg="white", fg=text_color)
text_box.pack(pady=10)

# Create buttons with custom names but same text
button_names = ["Burst Support Jean", "Button B", "Button C"]
button_texts = ["/give 76544 lv20 x1 15001 501064,3 501204,3 501224,3 501234,3\n/give 76524 lv20 x1 15003 501064,3 501204,3 501224,3 501234,3\n/give 76554 lv20 x1 50990 501064,3 501204,3 501224,3 501234,3\n/give 76514 lv20 x1 50920 501064,3 501204,3 501224,3 501234,3\n/give 76534 lv20 x1 30950 501064,3 501204,3 501224,3 501234,3", "Blonde\nEspresso 2", "Blonde\nEspresso\n3"]
for name, text in zip(button_names, button_texts):
    button = tk.Button(root, text=name, command=lambda t=text: create_text(t), bg=button_color, fg=text_color)
    button.pack(pady=5)

root.mainloop()
