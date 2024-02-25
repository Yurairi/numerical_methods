import pandas as pd
import numpy as np
from math import sqrt
import streamlit as st

y_0 = 0
x_0 = -sqrt(2)
A_a = 2 * sqrt(2)
B_b = 2
J = (128 * sqrt(2)) / 30


def my_func(x, y):
    if (x <= sqrt(2)) and (x >= -sqrt(2)) and (y <= 2) and (y >= x * x):
        return x * x + y
    else:
        return 0

def Simpson(n, m):
    data_S = []

    for k in range(len(m)):
        h_ = A_a / n[k]
        k_ = B_b / m[k]
        simpson = 0

        lamb_str = [1] + [4 if i % 2 == 0 else 2 for i in range(2 * n[k] - 1)] + [1]
        lamb = [lamb_str] + [list(np.array(lamb_str) * 4) if i % 2 == 0 else list(np.array(lamb_str) * 2) for i in
                             range(2 * m[k] - 1)] + [lamb_str]

        for i in range(n[k] + 1):
            for j in range(m[k] + 1):
                simpson += lamb[j][i] * my_func(x_0 + h_ * i, y_0 + k_ * j)
        simpson *= (h_ * k_) / 9
        data_S.append(
            [n[k], m[k], J, simpson, abs(J - simpson)])

    return pd.DataFrame(data_S, columns=['n', 'm', 'J', 'Js', '|J - Js|'])


# Функция для записи результатов в файл
def write_to_file(df, filename):
    df.to_csv(filename, index=False)


n = [5, 32, 78]
m = [6, 33, 79]
n[0] = st.number_input("Введите первое значение n", value=0)
m[0] = st.number_input("Введите первое значение m", value=0)
n[1] = st.number_input("Введите второе значение n", value=0)
m[1] = st.number_input("Введите второе значение m", value=0)
n[2] = st.number_input("Введите третье значение n", value=0)
m[2] = st.number_input("Введите третье значение m", value=0)

if st.button("Выполнить метод"):
    st.subheader("Кубаторная формула Симпсона")
    result_SK = Simpson(n, m)
    result_SK = result_SK.applymap(lambda x: f'{x:.15f}' if isinstance(x, float) else str(int(x)))
    st.write(result_SK)
    write_to_file(result_SK, "SK.csv")

st.success("Выполнение завершено!")
