import webbrowser
import tkinter as tk
from tkinter import messagebox

class WebsiteOpener:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Website Opener")
        self.websites = []

        self.entry_label = tk.Label(self.root, text="Enter website URL:")
        self.entry_label.pack()

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()

        self.port_label = tk.Label(self.root, text="Enter port number (optional):")
        self.port_label.pack()

        self.port_entry = tk.Entry(self.root, width=10)
        self.port_entry.pack()

        self.add_button = tk.Button(self.root, text="Add Website", command=self.add_website)
        self.add_button.pack()

        self.open_button = tk.Button(self.root, text="Open Websites", command=self.open_websites)
        self.open_button.pack()

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()

    def add_website(self):
        website = self.entry.get()
        port = self.port_entry.get()
        if website:
            if port:
                self.websites.append(f"{website}:{port}")
            else:
                self.websites.append(website)
            self.listbox.insert(tk.END, self.websites[-1])
            self.entry.delete(0, tk.END)
            self.port_entry.delete(0, tk.END)

    def open_websites(self):
        for website in self.websites:
            if not website.startswith("http"):
                website = f"http://{website}"
            webbrowser.open(website)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WebsiteOpener()
    app.run()
