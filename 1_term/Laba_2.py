import pandas as pd
from math import exp
import streamlit as st


def Simple_iteration(x_0, eps):
    data_SI = []

    n = 0
    c = 1
    current_x = x_0
    while True:
        new_x = current_x + c * (exp(-1 * current_x) - current_x + 2)
        func = exp(-1 * new_x) - new_x + 2

        exiter_x = abs(new_x - current_x)
        exiter_func = abs(func)

        n = n + 1
        data_SI.append(
            [n, current_x, new_x, abs(new_x - current_x), exiter_func, eps])

        if (exiter_x <= eps) and (exiter_func <= eps):
            break

        current_x = new_x

    return pd.DataFrame(data_SI, columns=['n+1', 'x_n', 'x_n+1', '|x_(n+1) - x_n|', '|f(x_(n+1))|', 'eps'])


def Newton(x_0, eps):
    data_M = []

    n = 0
    current_x = x_0
    while True and (((exp(-1 * x_0) - x_0 + 2) * exp(-x_0)) > 0):
        new_x = current_x - (exp(-current_x) - current_x + 2) / (-exp(-current_x) - 1)
        func = exp(-1 * new_x) - new_x + 2

        exiter_x = abs(new_x - current_x)
        exiter_func = abs(func)

        n = n + 1
        data_M.append(
            [n, current_x, new_x, abs(new_x - current_x), exiter_func, eps])

        if (exiter_x <= eps) and (exiter_func <= eps):
            break

        current_x = new_x

    return pd.DataFrame(data_M, columns=['n+1', 'x_n', 'x_n+1', '|x_(n+1) - x_n|', '|f(x_(n+1))|', 'eps'])


def Mod_Newton(x_0, eps):
    data_MN = []

    n = 0
    current_x = x_0
    while True and (((exp(-1 * x_0) - x_0 + 2) * exp(-x_0)) > 0):
        new_x = current_x - (exp(-current_x) - current_x + 2) / (-exp(-x_0) - 1)
        func = exp(-1 * new_x) - new_x + 2

        exiter_x = abs(new_x - current_x)
        exiter_func = abs(func)

        n = n + 1
        data_MN.append(
            [n, current_x, new_x, abs(new_x - current_x), exiter_func, eps])

        if (exiter_x <= eps) and (exiter_func <= eps):
            break

        current_x = new_x

    return pd.DataFrame(data_MN, columns=['n+1', 'x_n', 'x_n+1', '|x_(n+1) - x_n|', '|f(x_(n+1))|', 'eps'])


# Функция для записи результатов в файл
def write_to_file(df, filename):
    df.to_csv(filename, index=False)

x_0 = st.number_input("Введите начальное значение x_0", value=0.0)

if st.button("Выполнить методы"):
    # Выполнение метода простых итераций
    st.subheader("Метод простых итераций")
    result_simple = Simple_iteration(x_0, 0.001)
    result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_simple)
    write_to_file(result_simple, "simple_iteration_results.csv")
    result_simple = Simple_iteration(x_0, 0.00001)
    result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_simple)
    write_to_file(result_simple, "simple_iteration_results.csv")


    if (((exp(-1 * x_0) - x_0 + 2) * exp(-x_0)) > 0):
        # Выполнение метода Ньютона
        st.subheader("Метод Ньютона")
        result_newton = Newton(x_0, 0.001)
        result_newton = result_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_newton)
        write_to_file(result_newton, "newton_results.csv")
        result_newton = Newton(x_0, 0.00001)
        result_newton = result_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_newton)
        write_to_file(result_newton, "newton_results.csv")

        # Выполнение модифицированного метода Ньютона
        st.subheader("Модифицированный метод Ньютона")
        result_mod_newton = Mod_Newton(x_0, 0.001)
        result_mod_newton = result_mod_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_mod_newton)
        write_to_file(result_mod_newton, "mod_newton_results.csv")
        result_mod_newton = Mod_Newton(x_0, 0.00001)
        result_mod_newton = result_mod_newton.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
        st.write(result_mod_newton)
        write_to_file(result_mod_newton, "mod_newton_results.csv")
    else:
        st.error('Не выполняется достаточное условие сходимости метода Ньютона!', icon="🚨")
        st.error('Не выполняется достаточное условие сходимости модифицированного метода Ньютона!', icon="🚨")

    st.success("Выполнение завершено!")
