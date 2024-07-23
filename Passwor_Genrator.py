import tkinter as tk
import string
import random

def generate_password():
    try:
        t = int(entry_digit.get())
        rep_allowed = entry_rep.get().lower() == 'yes'
        l = []
        while len(l) < t:
            r1 = string.ascii_letters
            r2 = string.digits
            r3 = string.punctuation
            if rep_allowed:
                c = random.choice(r1 + r2 + r3)
            else:
                #The set(r1) | set(r2) | set(r3) part combines these three sets into a single set by taking the union of their elements. This ensures that we have a pool of characters containing letters, digits, and punctuation.
#list(set(...)) converts the combined set back into a list. This step is necessary because random.choice() expects a sequence (like a list) as its argument.
#Finally, c = random.choice(...) selects a random character from the combined list of characters.
                c = random.choice(list(set(r1) | set(r2) | set(r3)))
            l.append(c)
            password=''.join(l)

##The join() method is used to concatenate the characters in the list l into a single string.
##The empty string '' is used as the separator between the characters. This means that each character in the list will be joined together without any spaces or other characters in between.
##l is a list of characters (presumably representing the generated password).
##The join() method is used to concatenate the characters in the list l into a single string.
#The empty string '' is used as the separator between the characters. This means that each character in the list will be joined together without any spaces or other characters in between.        

        password_label.config(text="Generated Password: " + password)
    except ValueError:
        password_label.config(text="Invalid input")

window = tk.Tk()
window.geometry("500x500")
window.title("Password Generator")

lbl = tk.Label(window, text="How Many Digits")
lbl.grid(row=0, column=0)
entry_digit = tk.Entry(window)
entry_digit.grid(row=0, column=1)

lbl1 = tk.Label(window, text="Repetition Allowed (yes/no)")
lbl1.grid(row=1, column=0)
entry_rep = tk.Entry(window)
entry_rep.grid(row=1, column=1)

button = tk.Button(window, text="Generate", command=generate_password)
button.grid(row=2, column=1)

password_label = tk.Label(window, text="")
password_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
