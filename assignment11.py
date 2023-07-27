import tkinter as tk
import webbrowser as wb

def open_faq_page():
    selected_site = site_var.get()
    if selected_site == "geeksforgeeks":
        faq_url = "https://practice.geeksforgeeks.org/faq.php"
    elif selected_site == "YouTube":
        faq_url = "https://www.example.com/youtube-faq"
    else:
        faq_url = ""

    if faq_url:
        print("directing to:", faq_url)
        wb.open(faq_url)
    else:
        print("Please select a site from where you came to know about the course.")

root = tk.Tk()
root.title("-cousre enquiry-")
#course input
l1 = tk.Label(root, text="Enter the course to be enquired about:")
l1.grid()

entry = tk.Entry(root, width=50)
entry.grid()

l2 = tk.Label(root, text="Select the source where you found out about this:")
l2.grid()

site_var = tk.StringVar()
#radio button for web1
radio1 = tk.Radiobutton(root, text="geeksforgeeks", variable=site_var, value="geeksforgeeks")
radio1.grid()
#radio button for web2
radio2 = tk.Radiobutton(root, text="YouTube Ads", variable=site_var, value="YouTube Ads")
radio2.grid()
#submit button
submit_button = tk.Button(root, text="Submit", command=open_faq_page)
submit_button.grid()

root.mainloop()
