import pandas as pd
import os

PRODUCTS_FILE = "products.csv"
WORKING_FILE = "inventory_working.csv"

# Load product catalog
if ox.path.exists(WORKING_FILE):
  inventory = pd.read_csv(WORKING_FILE)
  print("Loaded esisting inventory_working.csv - resuming count.")
else:
  inventory = pd.read_csv(PRODUCTS_FILE)
  inventory["Quantity"] = 0
  inventory.to_csv(WORKING_FILE, index=False)
  print("Started new inventory count.")

print("\nReady to scan.")
print("Commands:")
print(" export to save final csv")
print(" exit to quit safely\n")

while True:
  barcode = input("> ").strip()

  if barcode.lower() == "exit":
    inventory.to_csv(WORKING_FILE, index=False)
    print("Progress saved. Safe to exit.")
    break

  if barcode.lower() == "export":
    inventory.to_csv("inventory_final.csv", index=False)
    print("Exported inventory_final.csv")
    continue

  mask = inventory["SKU"].astype(str) == barcode

  if mask.any():
    inventory.loc[mask, "Quantity"] += 1
    inventory.to_csv(WORKING_FILE, index=False) #Auto saves
    qty = inventory.loc[mask, "Qunatity"].values[0]
    print(f"Scanned {barcode} quantity is now {qty}")
  else:
    print(f" Unknown barcode: {barcode}")

  
