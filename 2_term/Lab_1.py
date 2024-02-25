import pandas as pd
import numpy as np
from math import exp, sqrt
import streamlit as st

x_0 = 0
x_n = 1
y_0 = 2.2

def Prec_Y(x_i):
    return 0.2 * exp(pow(x_i, 3) / 3) + 2


def Eiler_Form(n):
    data_EF = []

    h = (x_n - x_0) / n
    current_x = x_0
    current_y = y_0
    data_EF.append(
        [x_0, y_0, y_0, 0])
    for i in range (n):
        new_x = current_x + h
        new_y = current_y + h * pow(current_x, 2) * (current_y - 2)

        prec_y = Prec_Y(new_x)

        data_EF.append(
            [new_x, prec_y, new_y, abs(new_y - prec_y)])

        current_x = new_x
        current_y = new_y

    return pd.DataFrame(data_EF, columns=['x', 'y', 'yE', '|уE - y|'])


def RK(current_x, current_y, h):
    K_1 = h * (current_y - 2) * pow(current_x, 2)
    K_2 = h * pow((current_x + h * 0.5), 2) * (current_y + K_1 * 0.5 - 2)
    K_3 = h * pow((current_x + h * 0.5), 2) * (current_y + K_2 * 0.5 - 2)
    K_4 = h * pow((current_x + h), 2) * (current_y + K_3 - 2)

    return current_y + (1 / 6) * (K_1 + 2 * K_2 + 2 * K_3 + K_4)


def R_K_Form(n):
    data_RK = []

    h = (x_n - x_0) / n
    current_x = x_0
    current_y = y_0
    data_RK.append(
        [x_0, y_0, y_0, 0])
    for i in range (n):
        new_x = current_x + h
        new_y = RK(current_x, current_y, h)

        prec_y = Prec_Y(new_x)

        data_RK.append(
            [new_x, prec_y, new_y, abs(new_y - prec_y)])

        current_x = new_x
        current_y = new_y

    return pd.DataFrame(data_RK, columns=['x', 'y', 'yRK', '|уRK - y|'])


def Adams(k, h):
    x, y = np.zeros(50), np.zeros(50)
    x[0], y[0] = 0, 2.2

    for i in range(1, 4):
        x[i] = x[i - 1] + h
        y[i] = RK(x[i - 1], y[i - 1], h)

    if k > 3:
        for i in range(4, k + 1):
            x[i] = x[i - 1] + h
            y[i] = y[i - 1] + (h / 24) * (55 * pow(x[i - 1], 2) * (y[i - 1] - 2) - 59 * pow(x[i - 2], 2) \
            * (y[i - 2] - 2) + 37 * pow(x[i - 3], 2) * (y[i - 3] - 2) - 9 \
            * pow(x[i - 4], 2) * (y[i - 4] - 2))

    return y[k]


def Adams_Form(n):

    data_AF = []

    h = (x_n - x_0) / n

    for i in range (n + 1):
        new_x = x_0 + i * h
        new_y = Adams(i, h)

        prec_y = Prec_Y(new_x)

        data_AF.append(
            [new_x, prec_y, new_y, abs(new_y - prec_y)])

    return pd.DataFrame(data_AF, columns=['x', 'y', 'yAF', '|уAF - y|'])


# Выполнение метода простых итераций
st.subheader("Метод Эйлера для n = 10")
result_Eiler = Eiler_Form(10)
result_Eiler = result_Eiler.applymap(lambda x: f'{x:.13f}' if isinstance(x, float) else str(int(x)))
st.write(result_Eiler)
st.subheader("Метод Эйлера для n = 20")
result_Eiler = Eiler_Form(20)
result_Eiler = result_Eiler.applymap(lambda x: f'{x:.13f}' if isinstance(x, float) else str(int(x)))
st.write(result_Eiler)
st.subheader("Метод Рунге-Кутта для n = 10")
result_RK = R_K_Form(10)
result_RK = result_RK.applymap(lambda x: f'{x:.13f}' if isinstance(x, float) else str(int(x)))
st.write(result_RK)
st.subheader("Метод Рунге-Кутта для n = 20")
result_RK = R_K_Form(20)
result_RK = result_RK.applymap(lambda x: f'{x:.13f}' if isinstance(x, float) else str(int(x)))
st.write(result_RK)
st.subheader("Метод Адамса для n = 10")
result_AD = Adams_Form(10)
result_AD = result_AD.applymap(lambda x: f'{x:.13f}' if isinstance(x, float) else str(x))
st.write(result_AD)
st.subheader("Метод Адамса для n = 20")
result_AD = Adams_Form(20)
result_AD = result_AD.applymap(lambda x: f'{x:.13}' if isinstance(x, float) else str(x))
st.write(result_AD)


def f(x, y):
  return pow(x, 2) * (y - 2)

def y_true(x):
  return 0.2 * exp(pow(x, 3) / 3) + 2

def coefficients(x0, y0, h):
    k1 = h * f(x0, y0)
    k2 = h * f(x0 + h / 2, y0 + k1 / 2)
    k3 = h * f(x0 + h / 2, y0 + k2 / 2)
    k4 = h * f(x0 + h, y0 + k3)
    y1 = y0 + ((k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return y1

def runge_kutta_2h(n, b, a, err):
    x = np.zeros(10000)
    y = np.zeros(10000)
    y1 = np.zeros(10000)
    error = err
    i = 1
    x[0] = a
    y[0] = 2.2
    h = (b - a) / n
    print("\nШаг h =", h)
    print("\nEps =", error)
    results = []
    results.append([f"{x[0]:.9f}", f"{y_true(x[0]):.13f}", f"{y[0]:.13f}", "", "", f"{abs(y[0] - y_true(x[0])):.13f}", f"{h:.13f}"])

    x[1] = x[0] + h
    y[1] = coefficients(x[0], y[0], h)
    error1 = abs(y[1] - y_true(x[1]))
    results.append([f"{x[1]:.9f}", f"{y_true(x[1]):.13f}", f"{y[1]:.13f}", "", "", f"{error1:.13f}", f"{h:.13f}"])

    while x[i] < b:
        if x[i] < b:
            x[i + 1] = x[i] + h
            if abs(x[i + 1]) < 0.0000001:
                x[i + 1] = 0

            y[i + 1] = coefficients(x[i], y[i], h)
            y1[i + 1] = coefficients(x[i], y[i], 2 * h)
            # print(x[i])
            if abs(y1[i + 1] - y[i + 1]) > error:
                results.append([f"{x[i + 1]:.9f}", f"{y_true(x[i + 1]):.13f}", f"{y[i + 1]:.13f}", f"{y1[i + 1]:.13f}",
                                f"{abs(y1[i + 1] - y[i + 1]):.13f}", f"{abs(y[i + 1] - y_true(x[i + 1])):.13f}", f"{h:.13f}"])
                h = h / 2
                results.append(["", f"Шаг h = {h:.9f}", '', '', '', '', ''])
                if i == 1:
                    results.append([f"{x[i - 1]:.9f}", f"{y_true(x[i - 1]):.13f}", f"{y[i - 1]:.13f}", "", "",
                                    f"{abs(y[i - 1] - y_true(x[i - 1])):.13f}", f"{h:.13f}"])
                else:
                    results.append([f"{x[i - 1]:.9f}", f"{y_true(x[i - 1]):.13f}", f"{y[i - 1]:.13f}", f"{y1[i - 1]:.13f}",
                                    f"{abs(y1[i - 1] - y[i - 1]):.13f}", f"{abs(y[i - 1] - y_true(x[i - 1])):.13f}", f"{h:.13f}"])
                x[i] = x[i - 1] + h
                y[i] = coefficients(x[i - 1], y[i - 1], h)
                results.append([f"{x[i]:.9f}", f"{y_true(x[i]):.13f}", f"{y[i]:.13f}", "", "", f"{abs(y[i] - y_true(x[i])):.13f}", f"{h:.13f}"])
            else:
                results.append([f"{x[i + 1]:.9f}", f"{y_true(x[i + 1]):.13f}", f"{y[i + 1]:.13f}", f"{y1[i + 1]:.13f}",
                                f"{abs(y1[i + 1] - y[i + 1]):.13f}", f"{abs(y[i + 1] - y_true(x[i + 1])):.13f}", f"{h:.13f}"])
                x[i + 2] = x[i + 1] + h
                y[i + 2] = coefficients(x[i + 1], y[i + 1], h)
                y1[i + 2] = coefficients(x[i + 1], y[i + 1], 2 * h)
                error1 = abs(y[i + 2] - y_true(x[i + 2]))
                if x[i + 2] < b:
                    results.append([f"{x[i + 2]:.9f}", f"{y_true(x[i + 2]):.13f}", f"{y[i + 2]:.13f}", "", "", f"{error1:.13f}", f"{h:.13f}"])
                i = i + 2

    df1 = pd.DataFrame(results, columns=["x", "y", "y_r_k", "y_r_k_2h", "|y_r_k_2h - y_r_k|", "|y - y_r_k|", "|h|"])
    st.table(df1)

st.subheader("Метод Рунге-Кутта с переменным шагом при n = 10")
st.subheader("е = 0.02")
runge_kutta_2h(10, x_n, x_0, 0.02)
st.subheader("Метод Рунге-Кутта с переменным шагом при n = 20")
st.subheader("е = 0.01")
runge_kutta_2h(20, x_n, x_0, 0.01)