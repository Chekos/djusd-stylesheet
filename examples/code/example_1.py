import altair as alt
import pandas as pd

data = pd.DataFrame({
    'school': ['Birch Lane', 'Chávez', 'Fairfield', 'Korematsu', 'Montgomery', 'North Davis', 'Patwin', 'Pioneer', 'Willet'],
    'value': [28, 55, 43, 91, 81, 53, 19, 87, 52]
})

colors = alt.Scale(domain=['Birch Lane', 'Chávez', 'Fairfield', 'Korematsu', 'Montgomery', 'North Davis', 'Patwin', 'Pioneer', 'Willet'],
                  range=['#185594', '#A51E22', '#4A443F', '#15A85C', '#E21E26', '#185594', '#4D3091', '#068945', '#1C4421'])
chart = alt.Chart(data).mark_bar().encode(
    x='school',
    y='value',
    color = alt.Color('school', scale = colors),
    tooltip = ['value', 'school']
).properties(
    height = 400,
    width = 600,
)
chart.savechart(fp = "../images/example_1.html")