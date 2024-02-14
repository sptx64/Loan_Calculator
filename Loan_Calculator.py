import streamlit as st

def loan_calculator(annual_interest_rate, number_of_years, loan_amount, extra_payments, extra_payment_frequency, start_date):
    """
    Calculate the monthly payment, total payment, and total interest paid for a loan.

    Parameters:
        annual_interest_rate (float): The annual interest rate as a decimal.
        number_of_years (int): The number of years the loan will be repaid over.
        loan_amount (float): The total amount borrowed.
        extra_payments (float): The total amount of extra payments made during the loan term.
        extra_payment_frequency (int): The number of times per year extra payments are made.
        start_date (str): The date when the loan repayment begins.

    Returns:
        dict: A dictionary containing the monthly payment, total payment, and total interest paid.
    """
    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = number_of_years * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    total_payment = monthly_payment * number_of_payments
    total_interest_paid = total_payment - loan_amount

    if extra_payments > 0:
        extra_payments_per_month = extra_payments / extra_payment_frequency
        total_extra_payments = extra_payments_per_month * number_of_payments
        total_payment = loan_amount + total_extra_payments
        total_interest_paid = total_payment - loan_amount

    return {
        "monthly_payment": round(monthly_payment, 2),
        "total_payment": round(total_payment, 2),
        "total_interest_paid": round(total_interest_paid, 2)
    }

# Streamlit UI
st.title("Loan Calculator")

annual_interest_rate = st.number_input("Annual Interest Rate (%)", min_value=0.01, max_value=100.0, value=5.0, step=0.01)
number_of_years = st.number_input("Number of Years", min_value=1, max_value=100, value=5, step=1)
loan_amount = st.number_input("Loan Amount", min_value=1000, max_value=1000000, value=200000, step=1000)
extra_payments = st.number_input("Extra Payments (per year)", min_value=0, max_value=1000000, value=1000, step=100)
extra_payment_frequency = st.number_input("Extra Payment Frequency (per year)", min_value=1, max_value=12, value=12, step=1)
start_date = st.date_input("Start Date", value=None)

if st.button("Calculate"):
    result = loan_calculator(annual_interest_rate / 100, number_of_years, loan_amount, extra_payments, extra_payment_frequency, start_date)

    st.write("## Results")
    st.write("Monthly Payment:", result["monthly_payment"])
    st.write("Total Payment:", result["total_payment"])
    st.write("Total Interest Paid:", result["total_interest_paid"])