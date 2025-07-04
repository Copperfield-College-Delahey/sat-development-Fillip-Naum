#Gui setup
import customtkinter as ctk 



app =  ctk.CTk()
app.title("Inventory System")
app.geometry("1000x600")


app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)


topFrame = ctk.CTkFrame(app, border_width=4)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
titleLabel = ctk.CTkLabel(topFrame, text="Inventory System", font=("Arial", 32))




app.mainloop()  
