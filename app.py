
from flask import Flask, render_template, request
from budget import calculate_budget

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    if request.method == "POST":
        try:
            weekly_income = float(request.form["income"])
            weekly_expenses = float(request.form["expenses"])
            expected_savings = float(request.form["goal"])
            weekly_savings = float(request.form["weekly_savings"])

            # Validate that inputs are not negative numbers.
            if weekly_income < 0 or weekly_expenses < 0 or expected_savings < 0 or weekly_savings < 0:
                message = "Please enter positive numbers only."
            else:
                message = calculate_budget(weekly_income, weekly_expenses, expected_savings, weekly_savings)
        # Error if input can't be transformed into a float.
        except ValueError:
            message = "Please enter valid numbers."

    return render_template("index.html", results=message)


if __name__ == "__main__":
    app.run(debug=False)
