(# House Savings Calculator (MIT Problem Set style)

Small Flask + standalone Python scripts project that calculates how long it will take to save a down payment on a house. The repository contains three problem variants (Part A, Part B, Part C) implemented as separate scripts and a small Flask web UI for interactive use.

Contents
--------

- `main.py` — Flask web app that exposes a simple HTML form (`index.html`) and renders results to `result.html`.
- `Combined.py` — Command-line menu that lets you run Part A, Part B or Part C interactively.
- `PartB.py` — Script for Part B (savings with semi-annual raises).
- `PartC.py` — Script for Part C (bisection search for best savings rate to hit a 3-year target).
- `index.html`, `result.html`, `style.css` — Basic UI for the Flask app. Note: static CSS should be placed in a `static/` folder when running the Flask app.

Goals
-----

- Calculate the number of months needed to save for a down payment given salary and saving rate (Part A).
- Handle semi-annual raises (Part B).
- Find the optimal savings rate (as a fraction of salary) using bisection search so the down payment can be saved within 36 months (Part C).

Quickstart (Flask web UI)
-------------------------

1. Make sure you have Python 3.8+ installed. Create a virtualenv (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install Flask (if not already installed):

```bash
pip install Flask
```

3. Ensure the static files are in place:

- `style.css` should live in `static/style.css` (the project includes a `static/style.css` file in the workspace).

4. Run the app:

```bash
python3 main.py
```

5. Open your browser at `http://127.0.0.1:5001/`.

Command-line usage
------------------

Run the combined interactive script to choose which part to run (A, B or C):

```bash
python3 Combined.py
```

Or run the parts directly (if present):

```bash
python3 PartB.py
python3 PartC.py
```

Notes about behavior
--------------------

- Parts A/B compute a monthly loop: each month your savings grow by interest (r = 0.04 annual), then you add monthly saving (portion_saved * monthly_salary). Part B also increases salary every 6 months by the semi-annual raise fraction.
- Part C performs a bisection search over integer rates from 0 to 10000 (converted to 0.0–1.0 by dividing by 10000) to find a savings rate that reaches the down payment (25% of $1,000,000) within 36 months, within a $100 tolerance.

Output formatting
-----------------

- The Flask UI now displays durations in years and months (for example, "1 year and 3 months") instead of only month counts.

Troubleshooting
---------------

- If Flask reports static file not found for `style.css`, ensure it's placed at `static/style.css` relative to the project root.
- If you changed files and want a clean run, restart the Flask process.

Assumptions and small improvements added
---------------------------------------

- Minor input validation is recommended before deploying. The current scripts assume numeric input and may raise `ValueError` on invalid input.
- The Flask app binds to port 5001 in the project; change `app.run(..., port=...)` in `main.py` if you need a different port.

Example
-------

Using the Flask UI, choose Part A and enter:

- Annual Salary: `120000`
- Portion Saved: `0.1` (10%)
- Total Cost: `500000`

The app will calculate how long (in years and months) it will take to save the required down payment (25% of total cost).

If you'd like, I can:

- Add unit tests for the calculation functions.
- Harden input validation and provide friendly error messages.
- Add a small `requirements.txt` with pinned dependencies.

If you want me to write any of those, tell me which one to do next and I'll add it along with tests and run them.

