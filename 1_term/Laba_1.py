import pandas as pd
import streamlit as st

# Метод простых итераций
def Simple_iteration(x_0, y_0, z_0, eps):
    data_SI = []


    k = 0
    current_x = x_0
    current_y = y_0
    current_z = z_0
    while True:
        new_x = 0.6 + 0.2 * current_y + 0.2 * current_z
        new_y = 0.125 + 0.75 * current_x + 0.125 * current_z
        new_z = 0.9 - 0.2 * current_x + 0.3 * current_y

        exiter = abs(new_x - current_x) + abs(new_y - current_y) + abs(new_z - current_z)

        k = k + 1
        data_SI.append([k, current_x, new_x, abs(new_x - current_x), current_y, new_y, abs(new_y - current_y), current_z, new_z,
                        abs(new_z - current_z), exiter, eps])

        if exiter <= eps:
            break

        current_x = new_x
        current_y = new_y
        current_z = new_z

    return pd.DataFrame(data_SI, columns=['k+1', 'x_k', 'x_k+1', '|x_(k+1) - x_k|', 'y_k', 'y_k+1', '|y_(k+1) - y_k|',
                                          'z_k', 'z_k+1', '|z_(k+1) - z_k|',
                                          'Sum', 'eps'])


# Метод Зейделя
def Zeidel(x_0, y_0, z_0, eps):
    data_Zeidel = []

    k = 0
    current_x = x_0
    current_y = y_0
    current_z = z_0
    while True:
        new_x = 0.6 + 0.2 * current_y + 0.2 * current_z
        new_y = 0.125 + 0.75 * new_x + 0.125 * current_z
        new_z = 0.9 - 0.2 * new_x + 0.3 * new_y

        exiter = abs(new_x - current_x) + abs(new_y - current_y) + abs(new_z - current_z)

        k = k + 1
        data_Zeidel.append([k, current_x, new_x, abs(new_x - current_x), current_y, new_y, abs(new_y - current_y), current_z, new_z,
                        abs(new_z - current_z), exiter, eps])

        if exiter <= eps:
            break

        current_x = new_x
        current_y = new_y
        current_z = new_z
    return pd.DataFrame(data_Zeidel, columns=['k+1', 'x_k', 'x_k+1', '|x_(k+1) - x_k|', 'y_k', 'y_k+1', '|y_(k+1) - y_k|',
                                          'z_k', 'z_k+1', '|z_(k+1) - z_k|',
                                          'Sum', 'eps '])


# Метод релаксации
def Relaxation(x_0, y_0, z_0, eps):
    data_relax = []

    k = 0
    current_x = x_0
    current_y = y_0
    current_z = z_0
    while True:
        R_x = 0.6 - current_x + 0.2 * current_y + 0.2 * current_z
        R_y = 0.125 - current_y + 0.75 * current_x + 0.125 * current_z
        R_z = 0.9 - current_z - 0.2 * current_x + 0.3 * current_y

        R_max = max(abs(R_x), abs(R_y), abs(R_z))

        data_relax.append([k, current_x, current_y, current_z, R_x, R_y, R_z, R_max, eps])

        if R_max == abs(R_x):
            current_x += R_x
        elif R_max == abs(R_y):
            current_y += R_y
        elif R_max == abs(R_z):
            current_z += R_z
        k = k + 1

        if (abs(R_x) <= eps) and (abs(R_y) <= eps) and (abs(R_z) <= eps):
            break

    return pd.DataFrame(data_relax, columns=['k', 'x_k', 'y_k', 'z_k', 'R_x', 'R_y', 'R_z', 'max|R_k|', 'eps'])


# Функция для записи результатов в файл
def write_to_file(df, filename):
    df.to_csv(filename, index=False)

st.title("ИТЕРАЦИОННЫЕ МЕТОДЫ РЕШЕНИЯ СИСТЕМ ЛИНЕЙНЫХ АЛГЕБРАИЧЕСКИХ УРАВНЕНИЙ")

x1_0 = st.number_input("Введите начальное значение x_0 для первой таблицы", value=0.0)
y1_0 = st.number_input("Введите начальное значение y_0 для первой таблицы", value=0.0)
z1_0 = st.number_input("Введите начальное значение z_0 для первой таблицы", value=0.0)

x2_0 = st.number_input("Введите начальное значение x_0 для второй таблицы", value=0.0)
y2_0 = st.number_input("Введите начальное значение y_0 для второй таблицы", value=0.0)
z2_0 = st.number_input("Введите начальное значение z_0 для второй таблицы", value=0.0)

if st.button("Выполнить методы"):
    # Выполнение метода простых итераций
    st.subheader("Метод простых итераций для первого набора начальных значений")
    result_simple = Simple_iteration(x1_0, y1_0, z1_0, 0.001)
    result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_simple)
    write_to_file(result_simple, "simple_iteration_results.csv")
    result_simple = Simple_iteration(x1_0, y1_0, z1_0, 0.00001)
    result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_simple)
    write_to_file(result_simple, "simple_iteration_results.csv")

    st.subheader("Метод простых итераций для второго набора начальных значений")
    result_simple = Simple_iteration(x2_0, y2_0, z2_0, 0.001)
    result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_simple)
    write_to_file(result_simple, "simple_iteration_results.csv")
    result_simple = Simple_iteration(x2_0, y2_0, z2_0, 0.00001)
    result_simple = result_simple.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_simple)
    write_to_file(result_simple, "simple_iteration_results.csv")

    # Выполнение метода Зейделя
    st.subheader("Метод Зейделя для первого набора начальных значений")
    result_zeidel = Zeidel(x1_0, y1_0, z1_0, 0.001)
    result_zeidel = result_zeidel.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_zeidel)
    write_to_file(result_zeidel, "seidel_results.csv")
    result_zeidel = Zeidel(x1_0, y1_0, z1_0, 0.00001)
    result_zeidel = result_zeidel.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_zeidel)
    write_to_file(result_zeidel, "seidel_results.csv")

    st.subheader("Метод Зейделя для второго набора начальных значений")
    result_zeidel = Zeidel(x2_0, y2_0, z2_0, 0.001)
    result_zeidel = result_zeidel.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_zeidel)
    write_to_file(result_zeidel, "zeidel_results.csv")
    result_zeidel = Zeidel(x2_0, y2_0, z2_0, 0.00001)
    result_zeidel = result_zeidel.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_zeidel)
    write_to_file(result_zeidel, "zeidel_results.csv")

    # Выполнение метода релаксации
    st.subheader("Метод релаксации для первого набора начальных значений")
    result_relaxation = Relaxation(x1_0, y1_0, z1_0, 0.001)
    result_relaxation = result_relaxation.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_relaxation)
    write_to_file(result_relaxation, "relaxation_results.csv")
    result_relaxation = Relaxation(x1_0, y1_0, z1_0, 0.00001)
    result_relaxation = result_relaxation.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_relaxation)
    write_to_file(result_relaxation, "relaxation_results.csv")

    st.subheader("Метод релаксации для второго набора начальных значений")
    result_relaxation = Relaxation(x2_0, y2_0, z2_0, 0.001)
    result_relaxation = result_relaxation.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_relaxation)
    write_to_file(result_relaxation, "relaxation_results.csv")
    result_relaxation = Relaxation(x2_0, y2_0, z2_0, 0.00001)
    result_relaxation = result_relaxation.applymap(lambda x: f'{x:.9f}' if isinstance(x, float) else str(int(x)))
    st.write(result_relaxation)
    write_to_file(result_relaxation, "relaxation_results.csv")

    st.success("Выполнение завершено!")

