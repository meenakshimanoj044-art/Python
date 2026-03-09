
def apply_discount(item_list,rules):
    quantity_discounts=rules.get("quantity_discounts",[])
    weight_discounts=rules.get("weight_discounts",[])
    for item in item_list:
        percent=0
        unit_type=item.get("unit_type","").lower()
        quantity=item.get("quantity",0)
        if(unit_type=="count"):
            for count_discount in quantity_discounts: 
                if(quantity>=count_discount.get("min_quantity",0)):
                    percent=max(percent,count_discount.get("percent",0))
        elif(unit_type=="weight"):
            for weight_discount in weight_discounts:
                if(quantity>=weight_discount.get("min_weight",0)):
                    percent=max(percent,weight_discount.get("percent",0))
        discount=item["total"]*(percent/100)
        item["unit_discount"]=discount
        item["total"]-=discount
    return item_list

def apply_category_discount(item_list,rules):
        for item in item_list:
            category_disc_percent=0
            category=item["category"].lower().replace(" ","_")
            if category in rules.get("category_discounts",{}):
                category_disc_percent=rules["category_discounts"][category]
                category_discount=item["total"]*(category_disc_percent/100)
                item["category_discount"] = category_discount
                item["total"]-=category_discount
        return item_list

def apply_combo_discounts(item_list,rules):
    cart_items=[item.get("name","").lower() for item in item_list]
    for combo_rule in rules.get("combo_discounts",[]):
        combo_items=combo_rule.get("items",[])
        discount_percent=combo_rule.get("discount_percent",0)
        if all(items in cart_items for items in combo_items):
            for item in item_list:
                if item["name"].lower() in combo_items:
                    item["combo_discount"]=item["total"]*(discount_percent/100)
                    item["total"]-=item["combo_discount"]
    return item_list

def total_discount(item_list,rules,bill_data):
    total_discount=0
    for item in item_list:
        unit_discount=item.get("unit_discount",0)
        category_discount=item.get("category_discount",0)
        combo_discount=item.get("combo_discount",0)
        total_discount+=unit_discount+category_discount+combo_discount
    bill_data["total_discount"]=total_discount
    return bill_data
    



