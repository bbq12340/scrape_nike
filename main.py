try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
from nike_scrape import scrape

root = tk.Tk()
root.title("NIKE scraper")
root.geometry("400x400")

s_label = tk.Label(text="search")
s_label.pack(pady=5)

q = tk.StringVar()
query = tk.Entry(root, textvariable=q)
query.pack()


item_label = tk.Label(text="min item")
item_label.pack(pady=5)

i = tk.IntVar()
quantity = tk.Entry(root, textvariable=i)
quantity.pack()

def handle_click():
    keyword = query.get().strip("")
    value = int(quantity.get())
    try:
        scrape(keyword, value)
        tk.messagebox.showinfo("info", "process is finished")
    except ValueError:
        tk.messagebox.showerror("error", "something went wrong")


btn = tk.Button(root, text="search", command=handle_click)
btn.pack()

root.mainloop()
