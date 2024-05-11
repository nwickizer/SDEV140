from tkinter import *
from tkinter import messagebox
 

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x400")

start_btn_img = PhotoImage(file="start button.png")
quit_btn_img = PhotoImage(file="quit button.png")

def start_game():
    # hide main menu and start game
    main_menu_frame.grid_forget()
    game_frame.grid(row=0, column=0)
    create_game_grid()

def exit_game():
    # close application
    root.destroy()

def reset():
    # show main menu and reset game
    main_menu_frame.grid(row=0, column=0)
    game_frame.grid_forget()

def create_game_grid():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    
    # buttons
    b1 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

    b4 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

    b7 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(game_frame, text=" ", font=("Arial", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

    # grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

# main menu frame
main_menu_frame = Frame(root)
main_menu_frame.grid(row=0, column=0)

# start game button in main menu
start_game_button = Button(main_menu_frame, image=start_btn_img, font=("Arial", 18), command=start_game)
start_game_button.grid(row=0, column=0, pady=20)

# exit button in main menu
exit_button = Button(main_menu_frame, image=quit_btn_img, font=("Arial", 18), command=exit_game)
exit_button.grid(row=1, column=0)

# game frame
game_frame = Frame(root)

# disable buttons
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

# check for winner  
def winchecker():
    global winner
    winner = False
    
# check if X won
 
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()  
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()    
    
# X diagonals

    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()  
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X wins the game!")
        disable_all_buttons()  

# check if O won

    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()  
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()
        
# O diagonals
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons()  
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O wins the game!")
        disable_all_buttons() 

def b_click(b):
    global clicked, count
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        winchecker()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        winchecker()
    else:
        messagebox.showerror("Tic-Tac-Toe", "Box is already filled")


# menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# options menu
options_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset", command=reset)


# display the main menu
main_menu_frame.grid(row=0, column=0)


# display the main menu
main_menu_frame.grid(row=0, column=0)

root.mainloop()

