
def apply_tax(item_list, tax_rules, bill_data):
    total_tax = 0

    category_tax = tax_rules.get("category_tax", {})
    special_conditions = tax_rules.get("special_conditions", [])
    default_tax_percent = tax_rules.get("default_tax_percent", 0)

    for item in item_list:
        amount = item.get("total", 0)
        category = item.get("category")

        tax_percent = default_tax_percent

        if category in category_tax:
            tax_percent = category_tax[category]

        for condition in special_conditions:
            condition_category = condition.get("category")
            min_total = condition.get("min_total", 0)
            condition_percent = condition.get("percent")

            if condition_percent is None:
                continue

            if (condition_category is None or condition_category == category) and amount >= min_total:
                tax_percent = condition_percent

        item_tax = (amount * tax_percent) / 100
        item["tax"] = item_tax
        total_tax += item_tax

    bill_data["tax"] = total_tax
    return item_list, bill_data