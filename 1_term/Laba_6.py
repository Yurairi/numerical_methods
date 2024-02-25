import pandas as pd
from math import sqrt
import streamlit as st

a = 3
b = 4
t4 = [-0.86113631, -0.33998104, 0.33998104, 0.86113631]
t8 = [-0.96028986, -0.79666648, -0.52553242, -0.18343464, 0.18343464, 0.52553242, 0.79666648, 0.96028986]
A4 = [0.34785484, 0.65214516, 0.65214516, 0.34785484]
A8 = [0.10122854, 0.22238104, 0.31370664, 0.36268378, 0.36268378, 0.31370664, 0.22238104, 0.10122854]

J = 16 / (3 * sqrt(5)) - (6 * sqrt(3) / (3 * sqrt(5)))


def my_func(x):
    return x / (sqrt(5 * x))

def Trapeze():
    data_T = []

    for n in range(1, 3):
        h = 1 / (n * 4)
        trapeze = 0
        for i in range(n * 4 + 1):
            if (i == 0) or (i == n * 4):
                trapeze += my_func(a + i * h) / 2
            else:
                trapeze += my_func(a + i * h)
        trapeze *= h
        data_T.append(
            [n * 4, J, trapeze, abs(J - trapeze)])

    return pd.DataFrame(data_T, columns=['n', 'J', 'Jtr', '|J - Jtr|'])

def Simpson():
    data_S = []

    for n in range(1, 3):
        h = 1 / (n * 4)
        simpson = 0
        for i in range(n * 4 + 1):
            if (i == n * 4) or (i == 0):
                simpson += my_func(a + i * h)
            elif (i % 2 == 1):
                simpson += 4 * my_func(a + i * h)
            elif (i % 2 == 0) and (i != 0) and (i != n * 4):
                simpson += 2 * my_func(a + i * h)


        simpson *= h / 3
        data_S.append(
            [n * 4, J, simpson, abs(J - simpson)])

    return pd.DataFrame(data_S, columns=['n', 'J', 'Js', '|J - Js|'])


def Gauss():
    data_G = []

    for n in range(1, 3):
        gauss = 0
        for i in range(n * 4):
            if(n * 4 == 4):
                gauss += A4[i] * (sqrt(0.5 * (7 + t4[i])) / sqrt(5))
            if(n * 4 == 8):
                gauss += A8[i] * (sqrt(0.5 * (7 + t8[i])) / sqrt(5))
        gauss *= 0.5
        data_G.append(
            [n * 4, J, gauss, abs(J - gauss)])

    return pd.DataFrame(data_G, columns=['n', 'J', 'Jg', '|J - Jg|'])


# Функция для записи результатов в файл
def write_to_file(df, filename):
    df.to_csv(filename, index=False)

# Выполнение формулы трапеции
st.subheader("Формула трапеции")
result_trapeze = Trapeze()
result_trapeze = result_trapeze.applymap(lambda x: f'{x:.12f}' if isinstance(x, float) else str(int(x)))
st.write(result_trapeze)
write_to_file(result_trapeze, "trapeze_result.csv")

# Выполнение формулы Симпсона
st.subheader("Квадратурная формула Симпсона")
result_simpson = Simpson()
result_simpson = result_simpson.applymap(lambda x: f'{x:.12f}' if isinstance(x, float) else str(int(x)))
st.write(result_simpson)
write_to_file(result_simpson, "simpson_result.csv")

# Выполнение формулы Гаусса
st.subheader("Квадратурная формула Гаусса")
result_gauss = Gauss()
result_gauss = result_gauss.applymap(lambda x: f'{x:.12f}' if isinstance(x, float) else str(int(x)))
st.write(result_gauss)
write_to_file(result_gauss, "gauss_results.csv")

st.success("Выполнение завершено!")
