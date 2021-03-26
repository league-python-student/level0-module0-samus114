from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    num = random.randint(0, 3)
    # 2. Print your variable to the console
    print(num)
    # 3. Get the user to enter something that they think is awesome
    awesome = simpledialog.askstring("", "what do you find awesome?")
    # 4. If your variable is  0
    if num == 0:
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo("", awesome + " is AWESOME!")
    # 5. If your variable is  1
    elif num == 1:
        # -- tell the user whatever they entered is ok.
        messagebox.showinfo("", awesome + " is ok...")
    # 6. If your variable is  2
    elif num == 2:
        # -- tell the user whatever they entered is boring.
        messagebox.showinfo("", awesome + " is boring")
    # 7. If your variable is  3
    else:
        # -- invent your own message to give to the user (be nice).
        messagebox.showinfo("", " is acceptable")
    # Run the window's .mainloop() method
    window.mainloop()