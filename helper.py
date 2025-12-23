import pandas as pd
# Load product catalog
products = pd.read_csv("products.csv")

# Add quantity column if not present (change to add quantity counted column)
if "Quantity" not in products.columns:
  products["Quantity"] = 0

print("Ready to scan. Type or scan a barcode and press Enter.")
print("Type 'export' to save CSV, 'exit' to quit.")

while True:
  barcode = input("> ").strip()

  if barcode.lower() == "exit":
    break

  if barcode.lowere() == "export":
    products.to_csv("inventory_count.csv", index=False)
    print("Inveontory exported to inventory_count.csv")
    continue

  if barcode in products["SKU"].astype(str).values:
    products.loc[products["SKU"].astype(str) == barcode, "Quantity"] += 1
    qty = products.loc[products["SKU"].astype(str) == barcode, "Quantity"].values[0]
    print(f"Scanned {barcode} quantity now {qty}")

  else:
    print(f"Unknown barcode: {barcode}")
