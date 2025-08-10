import customtkinter as ctk

app = ctk.CTk()
app.title("Inventory System")
app.geometry("1000x600")

frames = {}

def show_frame(name):
    for f in frames.values():
        f.grid_forget()
    frames[name].grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

#def save(save):
def save():
    values = []
    for field in labels:
        value = entry_labels[field].get()
        values.append(value)
        entry_labels[field].delete(0,"end")

    formatted = " | ".join(values)
    inventory_display.insert("end", formatted + "\n") 
    inventory_display.see("end")



#Top Frame
topFrame = ctk.CTkFrame(app)
topFrame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
ctk.CTkButton(topFrame, text="Inventory System", font=("Helvetica", 30) ,command=lambda: show_frame("main")).grid(row=0, column=2, padx=15, pady=15)

#Mid Frame/Main Window
midFrame = ctk.CTkFrame(app)
midFrame.grid_columnconfigure((0,1,2), weight=1)
ctk.CTkButton(midFrame, text="Restock", font=("Helvetica", 25, "bold"), command=lambda: show_frame("restock")).grid(row=0, column=0, padx=80, pady=80, sticky="nsew")
ctk.CTkButton(midFrame, text="Current Inventory", font=("Helvetica", 25, "bold"), command=lambda: show_frame("inventory")).grid(row=0, column=1, padx=80, pady=80, sticky="nsew")
ctk.CTkButton(midFrame, text="Reports", font=("Helvetica", 25, "bold"), command=lambda: show_frame("reports")).grid(row=0, column=2, padx=80, pady=80, sticky="nsew")
frames["main"] = midFrame


#Inventory Window
inventory = ctk.CTkFrame(app)
labels = [
    "ItemId", "ItemName", "Quantity", "PricePerUnit",
    "DataAdded", "SupplierName", "ItemColour", "ItemDescription"
]
entry_labels = {}

for i, label in enumerate(labels):
    ctk.CTkLabel(inventory, text=label + ":").grid(row=i, column=0, sticky="e", padx=10, pady=5)
    entry=ctk.CTkEntry(inventory, width=300)
    entry.grid(row=i, column=1, sticky="w", padx=10, pady=5)
    entry_labels[label] = entry

ctk.CTkButton(inventory, text="Save", fg_color="red").grid(row=len(labels), column=0, columnspan=2, pady=15)
frames["inventory"]=inventory

inventory_display = ctk.CTkTextbox(inventory, width=400, height=400)
inventory_display.grid(row=0, column=2, rowspan=len(labels)+1, padx=10, pady=10, sticky="nsew")
inventory_display.insert("end", "Saved Inventory Entries:\n")

frames["inventory"] = inventory


#Restock Window
restock = ctk.CTkFrame(app)
ctk.CTkLabel(restock, text="Manual Restock", font=("Helvetica", 20), text_color="blue").pack(pady=10)
ctk.CTkLabel(restock, text="Automatic Restock", font=("Helvetica", 20), text_color="blue").pack(pady=10)
frames["restock"] = restock

#Reports Window
reports = ctk.CTkFrame(app)
ctk.CTkLabel(reports, text="Reports", font=("Helvetica", 24)).pack(pady=10)
ctk.CTkLabel(reports, text="Item ID:").pack()
ctk.CTkEntry(reports).pack()
ctk.CTkLabel(reports, text="Item Name:").pack()
ctk.CTkEntry(reports).pack()
frames["reports"] = reports

#Final Window Setup
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure((0, 1), weight=1)
show_frame("main")

app.mainloop()
