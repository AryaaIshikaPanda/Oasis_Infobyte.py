#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END


# In[2]:


class SimpleChatApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Simple Chat App")

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10)

        self.entry = Entry(root, width=50)
        self.entry.pack(pady=10)

        send_button = Button(root, text="Send", command=self.send_message)
        send_button.pack()

    def send_message(self):
        message = self.entry.get()
        self.text_area.insert(tk.END, "You: " + message + '\n')
        self.entry.delete(0, END)
        self.receive_message("Friend", "Friend: " + message)

    def receive_message(self, sender, message):
        self.text_area.insert(tk.END, message + '\n')


# In[3]:


root = tk.Tk()
chat_app = SimpleChatApp()
root.mainloop()


# In[ ]:




