import dash
from dash import html

dash.register_page(__name__, path='/', name="Introduction 😃")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("COVID-19 Dataset Overview"),
        "A new coronavirus designated 2019-nCoV was first identified in Wuhan, the capital of China's Hubei province.",
        html.Br(),html.Br(),
        "People developed pneumonia without a clear cause and for which existing vaccines or treatments were not effective.",
        html.Br(), html.Br(),
        "The virus has shown evidence of human-to-human transmission.",
        html.Br(), html.Br(),
        "Transmission rate (rate of infection) appeared to escalate in mid-January 2020.",
        html.Br(), html.Br(),
        "As of 30 January 2020, approximately 8,243 cases have been confirmed.",

    
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("Country/Region: "), "Country/Region",
        html.Br(),
        html.B("Lat: "), "Latitude of the location",
        html.Br(),
        html.B("Long: "), "Longitude of the location",
        html.Br(),
        html.B("Date: "), "Date of cumulative report",
        html.Br(),
        html.B("Confirmed: "), "Cumulative number of confirmed cases till this day",
        html.Br(),
        html.B("Deaths: "), "Cumulative number of deaths till this day",
        html.Br(),
        html.B("Recovered: "), "Cumulative number of recovered cases till this day",
        html.Br(),
        html.B("Active: "), "Active",
        html.Br(),
        html.B("WHO Region: "), "WHO Region",
    ])
], className="bg-light p-4 m-2")