import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name="Dataset 📋")

####################### LOAD DATASET #############################
df = pd.read_csv("covid_19_clean_complete.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')
covid_clean_data =df.copy()
covid_clean_data = covid_clean_data.groupby(["Country/Region"]).tail(1)
covid_clean_data = covid_clean_data.drop(columns=['Province/State'])

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    dash_table.DataTable(data=covid_clean_data.to_dict('records'),
                         page_size=20,
                         style_cell={"background-color": "lightgrey", "border": "solid 1px white", "color": "black", "font-size": "11px", "text-align": "left"},
                         style_header={"background-color": "dodgerblue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "18px"},
                        ),
])