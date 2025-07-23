#Gui setup
import customtkinter as ctk 


#Set Up Main Window
app =  ctk.CTk()
app.title("Inventory System")
app.geometry("1000x600")


app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=6)


#Top Frame
topFrame = ctk.CTkFrame(app, border_width=4)   
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
topFrame.grid_columnconfigure(1, weight=1)
topFrame.grid_columnconfigure(0, weight=0)
topFrame.grid_columnconfigure(0, weight=1)
topFrame.grid_rowconfigure(0, weight=1)

titleLabel = ctk.CTkLabel(topFrame, text="Inventory System", font= ("Helvetica", 30))
titleLabel.grid(row=0, column=1, sticky="nw", padx=15, pady=15)


#Middle Frame
midFrame = ctk.CTkFrame(app, border_width=2)
midFrame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
midFrame.grid_columnconfigure(0, weight=1)
midFrame.grid_columnconfigure(1, weight=1)
midFrame.grid_columnconfigure(2, weight=1)
midFrame.grid_rowconfigure(0, weight=1)

restockButton = ctk.CTkButton(midFrame, text="Restock", font = ("Helvetica", 25, "bold"))
restockButton.grid(row=0, column=0, sticky="nsew", padx= 15, pady=15)

currentInventoryButton = ctk.CTkButton(midFrame, text="Current Inventory",font = ("Helvetica", 25, "bold"))
currentInventoryButton.grid(row=0, column=1, sticky="nsew", padx= 15, pady=15)

reportsButton = ctk.CTkButton(midFrame, text="Reports", font = ("Helvetica", 25, "bold"))
reportsButton.grid(row=0, column=2, sticky="nsew", padx= 15, pady= 15)












app.mainloop()  
