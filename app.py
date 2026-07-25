"""
app.py
------------------------------------------------------------
Flask web application for "Analyzing Customer Orders Using Python"

Run locally with:
    python app.py

Then open:
    http://127.0.0.1:5000/
------------------------------------------------------------
"""

from flask import Flask, render_template
import analysis as core

app = Flask(__name__)


@app.route("/")
def dashboard():
    classifications = core.get_customer_classifications()
    revenue = core.revenue_per_category()
    top_customers = core.top_n_customers(3)
    electronics_buyers = sorted(core.customers_who_bought_electronics())
    multi_category_customers = sorted(core.customers_with_multiple_categories())
    both_buyers = sorted(core.customers_electronics_and_clothing())
    unique_products = sorted(core.unique_products())
    unique_categories = sorted(core.get_unique_categories())

    total_revenue = sum(revenue.values())

    return render_template(
        "index.html",
        orders=core.orders,
        classifications=classifications,
        revenue=revenue,
        total_revenue=total_revenue,
        top_customers=top_customers,
        electronics_buyers=electronics_buyers,
        multi_category_customers=multi_category_customers,
        both_buyers=both_buyers,
        unique_products=unique_products,
        unique_categories=unique_categories,
        product_category_map=core.product_category_map,
    )


@app.route("/report")
def report():
    """Plain-text version of the full report (mirrors console output)."""
    return "<pre>" + core.print_summary_report() + "</pre>"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
