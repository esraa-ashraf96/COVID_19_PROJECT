import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/map', name="Map 🌍")

            ####################### DATASET #############################
df = pd.read_csv("covid_19_clean_complete.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Date"] = df["Date"].dt.strftime('%Y-%m-%d')
covid_clean_data =df.copy()
covid_clean_data = covid_clean_data.drop(columns=['Province/State'])


            ####################### MAP #############################
def create_map(Date):
    data_at_specific_date = covid_clean_data[covid_clean_data["Date"] == Date]
    fig = px.choropleth(data_at_specific_date, 
                        locations="Country/Region",
                        locationmode="country names",
                        color="Confirmed",
                        hover_name="Country/Region",
                        hover_data=["Confirmed", "Active", "Deaths"],
                        title="COVID-19 Global Map",
                        color_continuous_scale=px.colors.sequential.Blues)
    return fig

            ####################### WIDGETS #############################
Date = covid_clean_data["Date"].unique()
date_dropdown = dcc.Dropdown(id="date_dropdown", options=[{"label": c, "value": c} for c in Date], 
                                value="2020-07-27", clearable=False)

            ####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    "Select Date", date_dropdown,
    dcc.Graph(id="map")
])

            ####################### CALLBACKS ###############################
@callback(Output("map", "figure"), [Input("date_dropdown", "value")])
def update_map(Date):
    return create_map(Date)

