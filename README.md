# Analyzing Customer Orders Using Python — Course-End Project 1

A Python project that analyzes customer orders using core data structures
(lists, tuples, dictionaries, sets) and control flow (loops, conditionals)
to classify customers, break down revenue by product category, and surface
business insights — with an interactive dashboard you can run on `localhost`.

## Project Structure

```
project/
├── analysis.py          # Core logic: all 5 project tasks (framework-free)
├── app.py                # Flask web app – runs the dashboard on localhost
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html          # Dashboard HTML template
├── static/                  # (reserved for CSS/JS assets)
└── README.md                 # This file
```

## Requirements

- Python 3.9 or newer
- pip (Python package manager)

## Installation Guide

1. **Clone / extract the project** to a folder of your choice and open a
   terminal inside it.

2. **(Recommended) Create a virtual environment**

   Windows:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS / Linux:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

## Running the Project

### Option A — Run the console analysis (no server)

```
python analysis.py
```

This prints the full text report (categories, customer classification,
revenue per category, top spenders, set-based insights) straight to the
terminal.

### Option B — Run the web dashboard on localhost

```
python app.py
```

You should see output similar to:

```
 * Serving Flask app 'app'
 * Running on http://127.0.0.1:5000
```

Now open your browser and go to:

```
http://127.0.0.1:5000/
```

You'll see the interactive dashboard with:
- Total customers, orders, revenue and category KPIs
- Customer spend table with High / Moderate / Low-value badges
- Full order list
- Revenue-per-category bar chart
- Top 3 highest-spending customers
- Electronics buyers, multi-category shoppers, and customers who bought
  both Electronics and Clothing (set operations)

A plain-text version of the same report is available at:

```
http://127.0.0.1:5000/report
```

Press `CTRL + C` in the terminal to stop the server.

## Notes on Classification Thresholds

The original brief classifies customers as High-Value (> $100), Moderate
($50–$100), or Low-Value (< $50). The sample dataset in this project uses
INR-scale prices for realism, so the thresholds are scaled proportionally
(High > ₹10,000, Moderate ₹5,000–₹10,000, Low < ₹5,000). You can change
these thresholds, or the underlying `orders` list, directly in
`analysis.py` — everything else (dashboard, report) recalculates
automatically.

## Customizing the Dataset

All sample data lives at the top of `analysis.py` in the `orders` list —
each entry is a tuple of `(customer_name, product, price, category)`. Add,
remove, or edit tuples there to analyze your own data; no other file needs
to change.

## Tech Stack

- Python 3 (lists, tuples, dictionaries, sets, loops, conditionals,
  list comprehensions, `sorted()`, set operations)
- Flask (lightweight web framework for the localhost dashboard)
- Jinja2 templating (bundled with Flask) for rendering the HTML dashboard
