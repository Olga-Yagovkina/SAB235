import plotly.express as px
import pandas as pd

# Создание DataFrame с данными
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [4, 7, 1, 5, 10]}

df = pd.DataFrame(data)

# Построение радарного графика с Plotly Express
fig = px.line_polar(df, r='Value', theta='Category', line_close=True)

# Настройка внешнего вида графика
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]  # Задаем диапазон для радиальной оси
        )
    )
)

# Отображение графика
fig.show()