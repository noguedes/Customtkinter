import tkinter 
import customtkinter # <- import customtkinter module 

root_tk = tkinter.Tk() # <- cretae the Tk window like you normally do
root_tk.geometry("400x240")
root_tk.title("Customtkinter test 01")

def  button_function():
    print("Customtkinter Test")

# use CTkButton instead of tkinter button 
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()