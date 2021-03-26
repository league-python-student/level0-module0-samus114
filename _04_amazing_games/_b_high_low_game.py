from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 101)

    # 2. Print out the random variable above
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        guess = simpledialog.askstring("", "i am thinking of a number between 1-100, you have 10 guesses")
        # 5. If the guess is correct
        if guess == str(random_num):
            # 6. Win. Use 'sys.exit(0)' to end the program
            sys.exit(0)
        # 7. if the guess is high
        elif guess >= str(random_num):
            # 8. Tell them it's too high
            messagebox.showinfo("", "that guess was too high")
        # 9. Else if the guess is low
        elif guess <= str(random_num):
            # 10. Tell them it's too low
            messagebox.showinfo("", "that was to low low low")
    #11. Outside of the loop, tell the user they lost
    messagebox.showerror("", "you lost")
    window.mainloop()
