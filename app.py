#Gui setup
import customtkinter as ctk 



app =  ctk.CTk()
app.Title("Inventory System")
app.geometry("1000x600")


app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight1)
app.grid_rowconfigure(0, weight=1)


app.mainloop()  
