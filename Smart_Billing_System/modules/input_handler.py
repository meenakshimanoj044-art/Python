
def add_items():
    items=[]
    while True:
        product_name=input("Enter the product name: ").strip()
        if not product_name :
            print("product name cannot be empty")
            continue
        product_category=input("Enter the category of the product: ").strip()
        if not product_category:
            print("product category cannot be empty")
            continue
        unit_type=input("Enter the unit type(Count/Weight/litre): ").lower()
        if(unit_type=="count"):
            while True:
                try:
                    quantity=int(input("Enter the count: "))
                    if quantity<=0:
                        print("Quantity must be positive.")
                        continue
                    break # got valid input
                except ValueError:
                    print("Invalid input. Enter a whole number.")

        elif(unit_type=="weight"):
            while True:
                try:
                    quantity=float(input("Enter the weight(in kg): "))
                    if quantity<=0:
                        print("Quantity must be positive.")
                        continue
                    break # got valid input
                except ValueError:
                    print("Invalid input. Enter a valid number.")

        elif(unit_type=="litre"):
            while True:
                try:
                    quantity=float(input("Enter the quantity in litres: "))
                    if quantity<=0:
                        print("Quantity must be positive")
                        continue
                    break
                except ValueError:
                    print("Invalid input.Enter valid input")
        else:
            print("Please enter a valid unit type")
            continue
        while True:
            try:
                price_per_unit=float(input("Enter the product price per unit: "))
                if(price_per_unit<=0):
                    print("Price per unit must be positive")
                    continue
                break
            except ValueError:
                print("Invalid Input. Enter a number")
                
        items.append({
            "name": product_name,
            "category":product_category,
            "unit_type": unit_type,
            "quantity": quantity,
            "price": price_per_unit
        })
        more=input("Do you want to enter more items y/n: ")
        if more.lower()=='n':
            break
    return items