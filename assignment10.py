import tkinter as tk
import webbrowser as wb

def open_website():
    url = entry.get()
    print("entered website:", url)
    wb.open(url)

root = tk.Tk()
root.title("Web Browser")

label = tk.Label(root, text="Enter the URL:")
label.grid()
entry = tk.Entry(root, width=50)
entry.grid()

button = tk.Button(root, text="Open Website", command=open_website)
button.grid()

root.mainloop()
