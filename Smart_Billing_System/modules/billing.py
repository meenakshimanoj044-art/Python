invoice_counter = 0  # starts at 0 every run

def generate_invoice_number():
    global invoice_counter
    invoice_counter += 1
    return f"INV-{invoice_counter:04d}"

def billing(item_list):
    subtotal = 0
    for item in item_list:
        quantity = float(item.get("quantity", 0))
        price = float(item.get("price", 0))
        items_total = quantity * price
        item["total"] = items_total
        subtotal += items_total
    invoice_no = generate_invoice_number()
    item_count = len(item_list)
    total_quantity = sum(float(item.get("quantity",0)) for item in item_list)
    bill_data = {
        "items": item_list,
        "invoice_no": invoice_no,
        "subtotal": subtotal,
        "item_count": item_count,
        "total_quantity": total_quantity,
        "tax": 0,
        "total_discount": 0,
        "total": subtotal,
    }
    return bill_data