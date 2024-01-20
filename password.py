#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tkinter as tk
from tkinter import messagebox
import random
import string


# In[13]:


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer for password length.")
        return

    use_letters = use_letters_var.get()
    use_numbers = use_numbers_var.get()
    use_symbols = use_symbols_var.get()

    character_set = ""
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Please choose at least one character set.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))

    # Implement security rules if needed

    # Display the password in a message box
    messagebox.showinfo("Password Generated", "Generated Password:\n" + password)


# In[ ]:





# In[14]:


root = tk.Tk()
root.title("Password Generator")


# In[15]:


length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)


# In[16]:


length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)


# In[17]:


use_letters_var = tk.IntVar()
use_letters_check = tk.Checkbutton(root, text="Include Letters", variable=use_letters_var)
use_letters_check.grid(row=1, column=0, padx=10, pady=10)


# In[18]:


use_numbers_var = tk.IntVar()
use_numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=use_numbers_var)
use_numbers_check.grid(row=1, column=1, padx=10, pady=10)


# In[19]:


use_symbols_var = tk.IntVar()
use_symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=use_symbols_var)
use_symbols_check.grid(row=1, column=2, padx=10, pady=10)


# In[20]:


generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=3, pady=10)


# In[21]:


root.mainloop()


# In[ ]:




