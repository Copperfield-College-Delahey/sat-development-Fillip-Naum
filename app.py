import customtkinter as ctk

app = ctk.CTk()
app.title("Inventory System")
app.geometry("1000x600")

frames = {}

def show_frame(name):
    for f in frames.values():
        f.grid_forget()
    frames[name].grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

topFrame = ctk.CTkFrame(app)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
ctk.CTkButton(topFrame, text="Inventory System", font=("Helvetica", 30) ,command=lambda: show_frame("main")).grid(row=0, column=1, padx=15, pady=15)

midFrame = ctk.CTkFrame(app)
midFrame.grid_columnconfigure((0,1,2), weight=1)
ctk.CTkButton(midFrame, text="Restock", font=("Helvetica", 25, "bold"), command=lambda: show_frame("restock")).grid(row=0, column=0, padx=80, pady=80, sticky="nsew")
ctk.CTkButton(midFrame, text="Current Inventory", font=("Helvetica", 25, "bold"), command=lambda: show_frame("inventory")).grid(row=0, column=1, padx=80, pady=80, sticky="nsew")
ctk.CTkButton(midFrame, text="Reports", font=("Helvetica", 25, "bold"), command=lambda: show_frame("reports")).grid(row=0, column=2, padx=80, pady=80, sticky="nsew")
frames["main"] = midFrame

inventory = ctk.CTkFrame(app)
ctk.CTkLabel(inventory, text="Current Inventory", font=("Helvetica", 24)).pack(pady=20)
ctk.CTkButton(inventory, text="Add New Inventory", fg_color="red").pack(pady=10)
frames["inventory"] = inventory

restock = ctk.CTkFrame(app)
ctk.CTkLabel(restock, text="Manual Restock", font=("Helvetica", 20), text_color="blue").pack(pady=10)
ctk.CTkLabel(restock, text="Automatic Restock", font=("Helvetica", 20), text_color="blue").pack(pady=10)
frames["restock"] = restock

reports = ctk.CTkFrame(app)
ctk.CTkLabel(reports, text="Reports", font=("Helvetica", 24)).pack(pady=10)
ctk.CTkLabel(reports, text="Item ID:").pack()
ctk.CTkEntry(reports).pack()
ctk.CTkLabel(reports, text="Item Name:").pack()
ctk.CTkEntry(reports).pack()
frames["reports"] = reports

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure((0, 1), weight=1)
show_frame("main")

app.mainloop()
