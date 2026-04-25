import streamlit as st
import pandas as pd

st.title("Калькулятор рассрочек с равными платежами (аннуитет)")

# Ввод данных
total_price = st.number_input("Стоимость товара", value=105000, step=1000)
down_payment = st.number_input("Первоначальный взнос", value=20000, step=1000)
months = st.number_input("Количество месяцев рассрочки", value=6, step=1)
monthly_rate = st.number_input("Месячный процент (например, 5 для 5%)", value=5.0) / 100

# Сумма кредита
loan_amount = total_price - down_payment

# Расчет аннуитетного платежа
if monthly_rate == 0:
    monthly_payment = loan_amount / months
else:
    monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

# График платежей
remaining = loan_amount
schedule = []

for month in range(1, months + 1):
    interest = remaining * monthly_rate
    principal = monthly_payment - interest
    remaining -= principal
    schedule.append({
        "Месяц": month,
        "Платеж": monthly_payment,
        "Основной долг": principal,
        "Проценты": interest,
        "Остаток долга": max(remaining, 0)
    })

# Итоговые суммы
total_payment = sum(item["Платеж"] for item in schedule)
total_interest = sum(item["Проценты"] for item in schedule)

st.subheader("Результаты")
st.write(f"Сумма после первоначального взноса: {loan_amount:,.2f} руб.")
st.write(f"Общая сумма выплат: {total_payment:,.2f} руб.")
st.write(f"Общая сумма процентов: {total_interest:,.2f} руб.")
st.write(f"Ежемесячный платеж: {monthly_payment:,.2f} руб.")

# Таблица графика платежей
st.subheader("График платежей")
df_schedule = pd.DataFrame(schedule)
st.dataframe(df_schedule.style.format({
    "Платеж": "{:,.2f}",
    "Основной долг": "{:,.2f}",
    "Проценты": "{:,.2f}",
    "Остаток долга": "{:,.2f}"
}))