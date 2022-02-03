import pandas as pd
import plotly.express as px

df = pd.read_csv("chart.csv")
fig = px.line(df, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
fig.show()