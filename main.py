from flask import Flask, render_template, request

app = Flask(__name__)


def format_duration(months):
    years = months // 12
    remaining_months = months % 12
    if years > 0 and remaining_months > 0:
        return f"{years} year{'s' if years != 1 else ''} and {remaining_months} month{'s' if remaining_months != 1 else ''}"
    elif years > 0:
        return f"{years} year{'s' if years != 1 else ''}"
    else:
        return f"{remaining_months} month{'s' if remaining_months != 1 else ''}"


# ---------- Part A Calculation ----------
def calculate_part_a(annual_salary, portion_saved, total_cost):
    r = 0.04
    portion_down_payment = 0.25
    current_savings = 0.0
    monthly_salary = annual_salary / 12
    down_payment = total_cost * portion_down_payment

    months = 0
    while current_savings < down_payment:
        current_savings += current_savings * (r / 12)
        current_savings += portion_saved * monthly_salary
        months += 1

    return months


# ---------- Part B Calculation ----------
def calculate_part_b(annual_salary, portion_saved, total_cost, semi_raise):
    r = 0.04
    portion_down_payment = 0.25
    current_savings = 0.0
    monthly_salary = annual_salary / 12
    down_payment = total_cost * portion_down_payment

    months = 0
    while current_savings < down_payment:
        current_savings += current_savings * (r / 12)
        current_savings += portion_saved * monthly_salary
        months += 1

        if months % 6 == 0:
            monthly_salary *= (1 + semi_raise)

    return months


# ---------- Part C (Bisection Search) ----------
def calculate_part_c(starting_salary):
    total_cost = 1000000
    down_payment = 0.25 * total_cost
    semi_raise = 0.07
    r = 0.04

    def compute_savings(rate):
        annual_salary = starting_salary
        monthly_salary = annual_salary / 12
        current_savings = 0.0
        monthly_rate = rate / 10000

        for month in range(36):
            current_savings += current_savings * (r / 12)
            current_savings += monthly_rate * monthly_salary

            if (month + 1) % 6 == 0:
                monthly_salary *= (1 + semi_raise)

        return current_savings

    # check if impossible
    if compute_savings(10000) < down_payment - 100:
        return None, None

    low, high = 0, 10000
    steps = 0
    best_rate = None

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        saved = compute_savings(mid)

        if abs(saved - down_payment) <= 100:
            best_rate = mid / 10000
            return best_rate, steps

        if saved < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    return None, steps


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    mode = request.form.get("mode")

    if mode == "partA":
        annual_salary = float(request.form.get("annual_salary"))
        portion_saved = float(request.form.get("portion_saved"))
        total_cost = float(request.form.get("total_cost"))

        months = calculate_part_a(annual_salary, portion_saved, total_cost)
        duration = format_duration(months)
        return render_template("result.html", result=f"Part A: It will take {duration} to save for the down payment")

    elif mode == "partB":
        annual_salary = float(request.form.get("annual_salary"))
        portion_saved = float(request.form.get("portion_saved"))
        total_cost = float(request.form.get("total_cost"))
        semi_raise = float(request.form.get("semi_raise"))

        months = calculate_part_b(annual_salary, portion_saved, total_cost, semi_raise)
        duration = format_duration(months)
        return render_template("result.html", result=f"Part B: It will take {duration} to save for the down payment")

    elif mode == "partC":
        salary = float(request.form.get("salary"))

        best_rate, steps = calculate_part_c(salary)

        if best_rate is None:
            return render_template("result.html",
                                   result="Part C: Not possible to save for the down payment in 3 years")

        return render_template("result.html",
                               result=f"Part C: Best savings rate = {best_rate:.4f} ({best_rate*100:.2f}%), Found in {steps} steps")

    return "Invalid Request"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
