"""
analysis.py
------------------------------------------------------------
Analyzing Customer Orders Using Python
Course-End Project 1

Implements every task from the problem statement using core
Python data structures: lists, tuples, dictionaries and sets,
combined with loops and conditionals.

This module has NO web-framework dependency, so it can also be
run directly on the command line:

    python analysis.py
------------------------------------------------------------
"""

from collections import defaultdict

# ============================================================
# TASK 1: Store customer orders
# ============================================================

# 1a. A list of customer names
customer_names = [
    "Aarav", "Diya", "Kabir", "Meera", "Rohan", "Isha"
]

# 1b. Each order stored as a tuple: (customer_name, product, price, category)
orders = [
    ("Aarav", "Laptop", 55000, "Electronics"),
    ("Aarav", "Wireless Mouse", 800, "Electronics"),
    ("Aarav", "T-Shirt", 600, "Clothing"),
    ("Diya", "Smartphone", 25000, "Electronics"),
    ("Diya", "Jeans", 1500, "Clothing"),
    ("Diya", "Cushion Cover", 400, "Home Essentials"),
    ("Kabir", "Bluetooth Speaker", 2200, "Electronics"),
    ("Kabir", "Cooking Pan", 900, "Home Essentials"),
    ("Meera", "Jacket", 2500, "Clothing"),
    ("Meera", "Bedsheet Set", 1200, "Home Essentials"),
    ("Meera", "Table Lamp", 750, "Home Essentials"),
    ("Rohan", "Headphones", 1800, "Electronics"),
    ("Rohan", "Sneakers", 3200, "Clothing"),
    ("Isha", "Notebook Set", 250, "Home Essentials"),
    ("Isha", "Kurti", 950, "Clothing"),
]

# 1c. Dictionary: customer name -> list of ordered products
customer_orders = defaultdict(list)
for name, product, price, category in orders:
    customer_orders[name].append(product)
customer_orders = dict(customer_orders)


# ============================================================
# TASK 2: Classify products by category
# ============================================================

# 2a. Dictionary mapping each product to its category
product_category_map = {product: category for _, product, _, category in orders}

# 2b. Set of unique product categories
unique_categories = {category for _, _, _, category in orders}


def get_unique_categories():
    """Return the set of unique product categories."""
    return unique_categories


# ============================================================
# TASK 3: Analyze customer orders
# ============================================================

def calculate_customer_totals():
    """Loop through orders and calculate each customer's total spend."""
    totals = defaultdict(float)
    for name, product, price, category in orders:
        totals[name] += price
    return dict(totals)


def classify_customer_usd_equivalent(total_spent, high=10000, moderate=5000):
    """
    Classify a customer based on total purchase value.

    The original brief uses USD thresholds ($100 / $50). Since the sample
    dataset uses INR-scale prices, the thresholds are scaled proportionally
    (high > 10,000 / moderate 5,000-10,000 / low < 5,000) and documented in
    the accompanying Writeup PDF. Change `high` / `moderate` to switch back
    to literal $100 / $50 if you plug in USD-priced data.
    """
    if total_spent > high:
        return "High-Value Buyer"
    elif total_spent >= moderate:
        return "Moderate Buyer"
    else:
        return "Low-Value Buyer"


def get_customer_classifications():
    """Return {customer: (total_spent, classification)} for every customer."""
    totals = calculate_customer_totals()
    result = {}
    for name in customer_names:
        total = totals.get(name, 0)
        result[name] = (total, classify_customer_usd_equivalent(total))
    return result


# ============================================================
# TASK 4: Generate business insights
# ============================================================

def revenue_per_category():
    """Total revenue per product category, stored in a dictionary."""
    revenue = defaultdict(float)
    for _, _, price, category in orders:
        revenue[category] += price
    return dict(revenue)


def unique_products():
    """Extract unique products purchased, using a set."""
    return {product for _, product, _, _ in orders}


def customers_who_bought_electronics():
    """List comprehension: customers who purchased Electronics."""
    return list({name for name, _, _, category in orders if category == "Electronics"})


def top_n_customers(n=3):
    """Identify the top-N highest spending customers using sorting."""
    totals = calculate_customer_totals()
    return sorted(totals.items(), key=lambda item: item[1], reverse=True)[:n]


# ============================================================
# TASK 5: Organize and display data
# ============================================================

def customers_per_category():
    """Dictionary mapping category -> set of customers who bought from it."""
    mapping = defaultdict(set)
    for name, _, _, category in orders:
        mapping[category].add(name)
    return dict(mapping)


def customers_with_multiple_categories():
    """Set operations: customers who purchased from more than one category."""
    cat_map = customers_per_category()
    customer_category_count = defaultdict(set)
    for category, names in cat_map.items():
        for name in names:
            customer_category_count[name].add(category)
    return {name for name, cats in customer_category_count.items() if len(cats) > 1}


def customers_electronics_and_clothing():
    """Set intersection: customers who bought BOTH Electronics and Clothing."""
    cat_map = customers_per_category()
    electronics_buyers = cat_map.get("Electronics", set())
    clothing_buyers = cat_map.get("Clothing", set())
    return electronics_buyers & clothing_buyers


def print_summary_report():
    """Console/report version of the full analysis (Task 5 requirement)."""
    lines = []
    lines.append("=" * 60)
    lines.append("CUSTOMER ORDER ANALYSIS REPORT")
    lines.append("=" * 60)

    lines.append("\n--- Available Product Categories ---")
    lines.append(", ".join(sorted(unique_categories)))

    lines.append("\n--- Customer Summary ---")
    classifications = get_customer_classifications()
    for name, (total, tag) in classifications.items():
        lines.append(f"{name:10s} | Total Spent: Rs.{total:>8,.0f} | {tag}")

    lines.append("\n--- Revenue per Category ---")
    for category, revenue in revenue_per_category().items():
        lines.append(f"{category:16s}: Rs.{revenue:,.0f}")

    lines.append("\n--- Unique Products Purchased ---")
    lines.append(", ".join(sorted(unique_products())))

    lines.append("\n--- Customers Who Bought Electronics ---")
    lines.append(", ".join(sorted(customers_who_bought_electronics())))

    lines.append("\n--- Top 3 Highest-Spending Customers ---")
    for rank, (name, total) in enumerate(top_n_customers(3), start=1):
        lines.append(f"{rank}. {name} - Rs.{total:,.0f}")

    lines.append("\n--- Customers Who Bought From Multiple Categories ---")
    lines.append(", ".join(sorted(customers_with_multiple_categories())))

    lines.append("\n--- Customers Who Bought BOTH Electronics & Clothing ---")
    both = customers_electronics_and_clothing()
    lines.append(", ".join(sorted(both)) if both else "None")

    lines.append("=" * 60)
    return "\n".join(lines)


if __name__ == "__main__":
    print(print_summary_report())
