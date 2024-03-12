import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/Country_state', name="Country_state 📈")

####################### DATASET #############################
df = pd.read_csv("covid_19_clean_complete.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')
covid_clean_data =df.copy()
covid_clean_data = covid_clean_data.drop(columns=['Province/State'])

####################### BAR CHART #############################
def create_bar_chart(country):
    country_data = covid_clean_data[covid_clean_data["Country/Region"] == country].iloc[100:,:]
    country_data["Date"] = pd.to_datetime(country_data["Date"], format="%Y-%m-%d")
    return px.bar(data_frame=country_data, x=["Confirmed", "Deaths", "Recovered", "Active"],y="Date",
                  height=600)


####################### WIDGETS #############################
countries = covid_clean_data["Country/Region"].unique()
country_dropdown = dcc.Dropdown(id="country_dropdown", options=[{"label": c, "value": c} for c in countries], 
                                value="US", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "Select Country", country_dropdown, 
    dcc.Graph(id="bar_chart")
])

####################### CALLBACKS ###############################
@callback(Output("bar_chart", "figure"), [Input("country_dropdown", "value")])
def update_bar_chart(country):
    return create_bar_chart(country)
