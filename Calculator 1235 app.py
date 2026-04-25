import streamlit as st
import pandas as pd

st.title("Калькулятор рассрочек без процентов")

# Ввод данных
total_price = st.number_input("Стоимость товара", value=700000, step=1000)
down_payment = st.number_input("Первоначальный взнос", value=0, step=1000)
months = st.number_input("Количество месяцев рассрочки", value=10, step=1)

# Сумма кредита
loan_amount = total_price - down_payment

# Ежемесячный платеж
monthly_payment = loan_amount / months
principal_per_month = monthly_payment  # полностью идёт на погашение долга

# График платежей
schedule = []
remaining = loan_amount

for month in range(1, months + 1):
    remaining -= principal_per_month
    schedule.append({
        "Месяц": month,
        "Платеж": monthly_payment,
        "Погашение долга": principal_per_month,
        "Остаток долга": max(remaining, 0)
    })

# Итоговые суммы
total_payment = sum(item["Платеж"] for item in schedule)

st.subheader("Результаты")
st.write(f"Сумма после первоначального взноса: {loan_amount:,.2f} руб.")
st.write(f"Общая сумма выплат: {total_payment:,.2f} руб.")
st.write(f"Ежемесячный платеж: {monthly_payment:,.2f} руб.")

# Таблица графика платежей
st.subheader("График платежей")
df_schedule = pd.DataFrame(schedule)
st.dataframe(df_schedule.style.format({
    "Платеж": "{:,.2f}",
    "Погашение долга": "{:,.2f}",
    "Остаток долга": "{:,.2f}"
}))