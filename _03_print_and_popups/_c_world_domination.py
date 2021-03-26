from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    writeCode = simpledialog.askstring("", "Can you write code?(yes or no?)")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if(writeCode == "yes"):
        messagebox.showinfo("", "you will rule the world!")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        messagebox.showerror("", "sign up for league classes")
    # Run the window's .mainloop() method
    window.mainloop()