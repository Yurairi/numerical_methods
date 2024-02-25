import pandas as pd
from math import exp, sqrt
import streamlit as st


def Simple_iteration(x_0, y_0, eps):
    data_SI = []

    n = 0
    current_x = x_0
    current_y = y_0
    while True:
        alfa = (2 * sqrt(current_x) * current_y) / (4 - current_y)
        betta = sqrt(current_x) / (current_y - 4)
        gamma = 4 / (current_y - 4)
        delta = 1 / (2 * (4 - current_y))

        f_1 = sqrt(current_x) + current_y -4
        f_2 = 8 * sqrt(current_x) + current_y * current_y - 20

        new_x = current_x + alfa * f_1 + betta * f_2
        new_y = current_y + gamma * f_1 + delta * f_2

        if new_x < 0:
            st.error('Отрицательный корень!', icon="🚨")
            break

        exiter_x = abs(new_x - current_x)
        exiter_y = abs(new_y - current_y)
        exiter_f_1 = abs(sqrt(new_x) + new_y - 4)
        exiter_f_2 = abs(8 * sqrt(new_x) + new_y * new_y - 20)

        n = n + 1
        data_SI.append(
            [n, current_x, new_x, exiter_x, current_y, new_y, exiter_y, exiter_f_1, exiter_f_2])

        if (exiter_x <= eps) and (exiter_y <= eps) and (exiter_f_1 <= eps) and (exiter_f_2 <= eps):
            break

        current_x = new_x
        current_y = new_y

    return pd.DataFrame(data_SI, columns=['k+1', 'x_k', 'x_k+1', '|x_k+1 - x_k|', 'y_k',
                                          'y_k+1', '|y_k+1 - y_k|', '|f1_k+1|', '|f2_k+1|'])


def Newton(x_0, y_0, eps):
    data_SI = []

    n = 0
    current_x = x_0
    current_y = y_0
    while True:
        det_1 = (2 * current_y * sqrt(current_x)) / (current_y - 4)
        det_2 = sqrt(current_x) / (4 - current_y)
        det_3 = 4 / (4 - current_y)
        det_4 = 1 / (2 * (current_y - 4))

        f_1 = sqrt(current_x) + current_y - 4
        f_2 = 8 * sqrt(current_x) + current_y * current_y - 20

        new_x = current_x - (det_1 * f_1 + det_2 * f_2)
        new_y = current_y - (det_3 * f_1 + det_4 * f_2)

        if new_x < 0:
            st.error('Отрицательный корень!', icon="🚨")
            break

        exiter_x = abs(new_x - current_x)
        exiter_y = abs(new_y - current_y)
        exiter_f_1 = abs(sqrt(new_x) + new_y - 4)
        exiter_f_2 = abs(8 * sqrt(new_x) + new_y * new_y - 20)

        n = n + 1
        data_SI.append(
            [n, current_x, new_x, exiter_x, current_y, new_y, exiter_y, exiter_f_1, exiter_f_2])

        if (exiter_x <= eps) and (exiter_y <= eps) and (exiter_f_1 <= eps) and (exiter_f_2 <= eps):
            break

        current_x = new_x
        current_y = new_y

    return pd.DataFrame(data_SI, columns=['k+1', 'x_k', 'x_k+1', '|x_k+1 - x_k|', 'y_k',
                                          'y_k+1', '|y_k+1 - y_k|', '|f1_k+1|', '|f2_k+1|'])


def Mod_Newton(x_0, y_0, eps):
    data_SI = []

    n = 0
    current_x = x_0
    current_y = y_0

    det_1 = (2 * current_y * sqrt(current_x) )/ (current_y - 4)
    det_2 = sqrt(current_x) / (4 - current_y)
    det_3 = 4 / (4 - current_y)
    det_4 = 1 / (2 * (current_y - 4))
    while True:
        f_1 = sqrt(current_x) + current_y - 4
        f_2 = 8 * sqrt(current_x) + current_y * current_y - 20

        new_x = current_x - (det_1 * f_1 + det_2 * f_2)
        new_y = current_y - (det_3 * f_1 + det_4 * f_2)

        if new_x < 0:
            st.error('Отрицательный корень!', icon="🚨")
            break

        exiter_x = abs(new_x - current_x)
        exiter_y = abs(new_y - current_y)
        exiter_f_1 = abs(sqrt(new_x) + new_y - 4)
        exiter_f_2 = abs(8 * sqrt(new_x) + new_y * new_y - 20)

        n = n + 1
        data_SI.append(
            [n, current_x, new_x, exiter_x, current_y, new_y, exiter_y, exiter_f_1, exiter_f_2])

        if (exiter_x <= eps) and (exiter_y <= eps) and (exiter_f_1 <= eps) and (exiter_f_2 <= eps):
            break

        current_x = new_x
        current_y = new_y

    return pd.DataFrame(data_SI, columns=['k+1', 'x_k', 'x_k+1', '|x_k+1 - x_k|', 'y_k',
                                          'y_k+1', '|y_k+1 - y_k|', '|f1_k+1|', '|f2_k+1|'])


# Функция для записи результатов в файл
def write_to_file(df, filename):
    df.to_csv(filename, index=False)

x_0 = st.number_input("Введите начальное значение x_0 (x_0 > 0)", value=0.0)
y_0 = st.number_input("Введите начальное значение y_0 (y != 4)", value=0.0)

if(x_0 <= 0) or (y_0 == 4):
    st.error('Неверные значения', icon="🚨")
else:
    if st.button("Выполнить методы"):
        # Выполнение метода простых итераций
        st.subheader("Метод простых итераций для eps = 0.001")
        result_simple = Simple_iteration(x_0, y_0, 0.001)
        result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_simple)
        write_to_file(result_simple, "simple_iteration_results.csv")
        st.subheader("Метод простых итераций для eps = 0.00001")
        result_simple = Simple_iteration(x_0, y_0, 0.00001)
        result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_simple)
        write_to_file(result_simple, "simple_iteration_results.csv")

        # Выполнение метода Ньютона
        st.subheader("Метод Ньютона для eps = 0.001")
        result_newton = Newton(x_0, y_0, 0.001)
        result_newton = result_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_newton)
        write_to_file(result_newton, "newton_results.csv")
        st.subheader("Метод Ньютона для eps = 0.00001")
        result_newton = Newton(x_0, y_0, 0.00001)
        result_newton = result_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_newton)
        write_to_file(result_newton, "newton_results.csv")

        # Выполнение модифицированного метода Ньютона
        st.subheader("Модифицированный метод Ньютона для eps = 0.001")
        result_mod_newton = Mod_Newton(x_0, y_0, 0.001)
        result_mod_newton = result_mod_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_mod_newton)
        write_to_file(result_mod_newton, "mod_newton_results.csv")
        st.subheader("Модифицированный метод Ньютона для eps = 0.00001")
        result_mod_newton = Mod_Newton(x_0, y_0, 0.00001)
        result_mod_newton = result_mod_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_mod_newton)
        write_to_file(result_mod_newton, "mod_newton_results.csv")

    st.success("Выполнение завершено!")
