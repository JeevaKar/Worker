import tkinter as tk
from selenium import webdriver

window = tk.Tk()

distractions_list = ["www.youtube.com", "www.facebook.com", "www.twitter.com"]
webbrowsers = ["Edge"]
close = True

def add_dist():
    link = distraction.get()
    for item in distractions_list:
        if item == link:
            break
    else:
        distractions_list.append(link)
        new_text = tk.Label(master=distractions, text=link)
        new_text.pack()

def close_tab():
    while True:
        if close == True:
            for webbrowser in webbrowsers:
                driver = webdriver.Edge()

distractions = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=1, padx=20, pady=20)
distractions.grid(row=1, column=1)

for distraction in distractions_list:
    new_text = tk.Label(master=distractions, text=distraction)
    new_text.pack()

add_distraction = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=1, padx=20, pady=20)
add_distraction.grid(row=2, column=1)

distraction = tk.Entry(master=add_distraction)
distraction.pack()
submit = tk.Button(master=add_distraction, text="submit", command=add_dist)
submit.pack()

window.mainloop()