import pandas as pd
import streamlit as st

y_0 = 40.658979854425
y_1 = 40.672397585932
y_2 = 40.685813170873
y_3 = 40.699226610577
y_4 = 40.712637906371
y_5 = 40.726047059579

delta_1_y_0 = 0.013417731507
delta_2_y_0 = -0.000002146566
delta_3_y_0 = 0.000000001329
delta_4_y_0 = -0.000000000002
delta_5_y_0 = -0.000000000001

delta_1_y_4 = 0.013409153208
delta_2_y_3 = -0.000002142586
delta_3_y_2 = 0.000000001324
delta_4_y_1 = -0.000000000003

h = 0.01

data_nods = [20, 20.01, 20.02, 20.03, 20.04, 20.05]

def First_Newton_Interpolation(x_00, x_11, x_22):
    data_FNIF = []

    for i in range (1, 4):
        if i == 1:
            x_0 = x_00
        if i == 2:
            x_0 = x_11
        if i == 3:
            x_0 = x_22
        func = 5.5 * pow((4 + x_0 * x_0), 1 / 3)

        q = (x_0 - 20) / h
        IP_5 = y_0 + delta_1_y_0 * q + delta_2_y_0 * (q * (q - 1)) / 2 + delta_3_y_0 * \
              (q * (q - 1) * (q - 2)) / (2 * 3) + delta_4_y_0 * (q * (q - 1) * (q - 2) * (q - 3)) / (2 * 3 * 4) * \
              delta_5_y_0 * (q * (q - 1) * (q - 2) * (q - 3) * (q - 4)) / (2 * 3 * 4 * 5)

        err = abs(IP_5 - func)

        data_FNIF.append( [x_0, func, IP_5, err, q])

    return pd.DataFrame(data_FNIF, columns=['x', 'y(x)', 'IP_5(x)', '|y(x)-IP_5(x)|', 'q'])


def Second_Newton_Interpolation(x_00, x_11, x_22):
    data_SNIF = []

    for i in range (1, 4):
        if i == 1:
            x_0 = x_00
        if i == 2:
            x_0 = x_11
        if i == 3:
            x_0 = x_22
        func = 5.5 * pow((4 + x_0 * x_0), 1 / 3)

        t = (x_0 - 20.05) / 0.01
        IIP_5 = y_5 + delta_1_y_4 * t + delta_2_y_3 * (t * (t - 1)) / 2 + delta_3_y_2 * \
               (t * (t - 1) * (t - 2)) / (2 * 3) + delta_4_y_1 * (t * (t - 1) * (t - 2) * (t - 3)) / (2 * 3 * 4) * \
               delta_5_y_0 * (t * (t - 1) * (t - 2) * (t - 3) * (t - 4)) / (2 * 3 * 4 * 5)

        err = abs(IIP_5 - func)

        data_SNIF.append([x_0, func, IIP_5, err, t])

    return pd.DataFrame(data_SNIF, columns=['x', 'y(x)', 'IIP_5(x)', '|y(x)-IIP_5(x)|', 't'])


def LaGrange_Interpolation(x_00, x_11, x_22):
    data_LI = []

    for i in range (1, 4):
        if i == 1:
            x_0 = x_00
        if i == 2:
            x_0 = x_11
        if i == 3:
            x_0 = x_22

        func = 5.5 * pow((4 + x_0 * x_0), 1 / 3)

        c_0 = -3388248321.2020833333
        c_1 = 16946832327.4716666666
        c_2 = -33904844309.0608333333
        c_3 = 33916022175.4808333333
        c_4 = -16963599127.654583333
        c_5 = 3393837254.9649166666


        L_5 = c_0 * (x_0 - 20.01) * (x_0 - 20.02) * (x_0 - 20.03) * (x_0 - 20.04) * (x_0 - 20.05) + \
              c_1 * (x_0 - 20.00) * (x_0 - 20.02) * (x_0 - 20.03) * (x_0 - 20.04) * (x_0 - 20.05) + \
              c_2 * (x_0 - 20.00) * (x_0 - 20.01) * (x_0 - 20.03) * (x_0 - 20.04) * (x_0 - 20.05) + \
              c_3 * (x_0 - 20.00) * (x_0 - 20.01) * (x_0 - 20.02) * (x_0 - 20.04) * (x_0 - 20.05) + \
              c_4 * (x_0 - 20.00) * (x_0 - 20.01) * (x_0 - 20.02) * (x_0 - 20.03) * (x_0 - 20.05) + \
              c_5 * (x_0 - 20.00) * (x_0 - 20.01) * (x_0 - 20.02) * (x_0 - 20.03) * (x_0 - 20.04)

        err = abs(L_5 - func)

        data_LI.append([x_0, func, L_5, err])

    return pd.DataFrame(data_LI, columns=['x', 'y(x)', 'L_5(x)', '|y(x)-L_5(x)|'])


def Dif_First_Newton_Interpolation(x_00, x_11, x_22):
    data_DFNI = []

    for i in range (1, 4):
        if i == 1:
            x_0 = x_00
        if i == 2:
            x_0 = x_11
        if i == 3:
            x_0 = x_22

        dif_func = 11 / 3 * (x_0 / pow((4 + x_0 * x_0), 2 / 3))

        x_ = 20
        for i in range (0, 5):
            if(x_0 >= data_nods[i] ) and (x_0 <= data_nods[i + 1]):
                if(x_0 <= data_nods[i] + h / 2):
                    x_ = data_nods[i]
                else:
                    x_ = data_nods[i + 1]

        q = (x_0 - x_) / h

        D_IP_5 = 1 / h * (delta_1_y_0 + ((2 * q - 1) / 2) * delta_2_y_0 + ((3 * pow(q, 2) - 6 * q + 2) / (3 * 2)) *
                          delta_3_y_0 + ((4 * pow(q, 3) - 18 * pow(q, 2) + 22 * q - 6) / (4 * 3 * 2)) * delta_4_y_0 +
                          delta_5_y_0 * ((5 * pow(q, 4) - 40 * pow(q, 3) + 105 * pow(q, 2) - 100 * q + 24) / (5 * 4 * 3 * 2)))

        err = abs(D_IP_5 - dif_func)

        data_DFNI.append([x_0, dif_func, x_, D_IP_5, err, q])

    return pd.DataFrame(data_DFNI, columns=['x', "y'(x)", 'x~', "(IP_5(x))'", "|y'(x)-(IP_5(x))'|", 'q'])


def Dif_Second_Newton_Interpolation(x_00, x_11, x_22):
    data_DSNI = []

    for i in range (1, 4):
        if i == 1:
            x_0 = x_00
        if i == 2:
            x_0 = x_11
        if i == 3:
            x_0 = x_22

        dif_func = 11 / 3 * (x_0 / pow((4 + x_0 * x_0), 2 / 3))

        x_ = 20.05
        for i in range(0, 5):
            if (x_0 >= data_nods[i]) and (x_0 <= data_nods[i + 1]):
                if (x_0 < data_nods[i] + h / 2):
                    x_ = data_nods[i]
                else:
                    x_ = data_nods[i + 1]

        t = (x_0 - x_) / h

        D_IIP_5 = 1 / h * (delta_1_y_4 + ((2 * t + 1) / 2) * delta_2_y_3 + ((3 * pow(t, 2) + 6 * t + 2) / (3 * 2)) *
                          delta_3_y_2 + ((4 * pow(t, 3) + 18 * pow(t, 2) + 22 * t + 6) / (4 * 3 * 2)) * delta_4_y_1 +
                          delta_5_y_0 * (
                                      (5 * pow(t, 4) + 40 * pow(t, 3) + 105 * pow(t, 2) + 100 * t + 24) / (5 * 4 * 3 * 2)))

        err = abs(D_IIP_5 - dif_func)

        data_DSNI.append([x_0, dif_func, x_, D_IIP_5, err, t])

    return pd.DataFrame(data_DSNI, columns=['x', "y'(x)", 'x~', "(IIP_5(x))'", "|y'(x)-(IIP_5(x))'|", 't'])


# Функция для записи результатов в файл
def write_to_file(df, filename):
    df.to_csv(filename, index=False)


x_0 = st.number_input("Введите начальное значение 20 <= x_0 <= 20.05", value=0.00, format="%.11f")
x_12 = st.number_input("Введите второе начальное значение 20 <= x_0 <= 20.05", value=0.00, format="%.11f")
x_22 = st.number_input("Введите третье начальное значение 20 <= x_0 <= 20.05", value=0.00, format="%.11f")

if((x_0 < 20) or (x_0 > 20.05)) or ((x_12 < 20) or (x_12 > 20.05)) or ((x_22 < 20) or (x_22 > 20.05)):
    st.error('Неверные значения', icon="🚨")
else:
    if st.button("Выполнить методы"):
        # Выполнение I Интерполяционной формулы Ньютона
        st.subheader("I Интерполяционная формула Ньютона")
        result_FNI = First_Newton_Interpolation(x_0, x_12, x_22)
        result_FNI = result_FNI.applymap(lambda x: f'{x:.15f}' if isinstance(x, float) else str(int(x)))
        st.write(result_FNI)
        write_to_file(result_FNI, "FNI.csv")

        # Выполнение II Интерполяционной формулы Ньютона
        st.subheader("II Интерполяционная формула Ньютона")
        result_SNI = Second_Newton_Interpolation(x_0, x_12, x_22)
        result_SNI = result_SNI.applymap(lambda x: f'{x:.15f}' if isinstance(x, float) else str(int(x)))
        st.write(result_SNI)
        write_to_file(result_SNI, "SNI.csv")

        # Выполнение Интерполяционной формулы ЛаГранжа
        st.subheader("Интерполяционная формула ЛаГранжа")
        result_LI = LaGrange_Interpolation(x_0, x_12, x_22)
        result_LI = result_LI.applymap(lambda x: f'{x:.15f}' if isinstance(x, float) else str(int(x)))
        st.write(result_LI)
        write_to_file(result_LI, "LI.csv")

        # Выполнение численного дифферинцирования по I Интерполяционной формуле Ньютона
        st.subheader("Численное дифферинцирование по I Интерполяционной формуле Ньютона")
        result_DFNI = Dif_First_Newton_Interpolation(x_0, x_12, x_22)
        result_DFNI = result_DFNI.applymap(lambda x: f'{x:.11f}' if isinstance(x, float) else str(int(x)))
        st.write(result_DFNI)
        write_to_file(result_DFNI, "DFNI.csv")

        # Выполнение численного дифферинцирования по II Интерполяционной формуле Ньютона
        st.subheader("Численное дифферинцирование по II Интерполяционной формуле Ньютона")
        result_DSNI = Dif_Second_Newton_Interpolation(x_0, x_12, x_22)
        result_DSNI = result_DSNI.applymap(lambda x: f'{x:.11f}' if isinstance(x, float) else str(int(x)))
        st.write(result_DSNI)
        write_to_file(result_DSNI, "DSNI.csv")

        st.success("Выполнение завершено!")
