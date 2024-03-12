import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/relationship', name="Relationship 📈")

####################### DATASET #############################
df = pd.read_csv("covid_19_clean_complete.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')
covid_clean_data =df.copy()
covid_clean_data = covid_clean_data.drop(columns=['Province/State'])
####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="Country/Region", y_axis="Confirmed"):
    return px.scatter(data_frame=covid_clean_data, x=x_axis, y=y_axis, color=y_axis, height=600)

####################### WIDGETS #############################
columnsx = ["Country/Region","Date"]
columnsy = ["Confirmed","Deaths","Recovered","Active"]

x_axis = dcc.Dropdown(id="x_axis", options=columnsx, value="Country/Region", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columnsy, value="Confirmed", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)

