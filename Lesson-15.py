import numpy as np
import pandas as pd
import matplotlib.pylot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplot import make_subplots

data = pd.read_csv("covid_data.csv")

data = data[
 [
    "Province_State",
    "Country_Region",
    "Last_Update",
    "Lat",
    "Long_,"
    "Confirmed",
    "Recovered",
    "Deaths",
    "Active",
 ]
]

data.columns = (
    "State",
    "Country",
    "Last_Update",
    "Lat",
    "Long_,"
    "Confirmed",
    "Recovered",
    "Deaths",
    "Active",

)

data["State"].fillna(value="", inplace=True)

top10_confirmed = pd.DataFrame(
    data.groupby("Country")
    ["Confirmed"].sum().nlargest(10).sort_values(ascending=False)
)

fig1 = px.scatter(
    top10_confirmed,
    x=top10_confirmed.index,
    y="Confirmed",
    size="Confirmed",
    size_max=120,
    color="Confirmed"
    title="Top 10 Countries By Confirmed Cases",
)
fig1.write_html("Fig1.html", auto_open=True)

top10_deaths = pd.DataFrame(
    data.groupby("Country")
["Deaths"].sum().nlargest(10).sort_values(ascending=False)
)
fig2 = px.bar(
    top10_deaths,
    x=top10_deaths.index,
    y="Deaths",
    height=600,
    color="Deaths",
    orientation="h",
    color_continuous_scale=["deepskyblue", "red"],
    title="Top 10 Death Cases Countries",
)
fig2.write_html("Fig2.html", auto_open=True)

top10_recovered = pd.DataFrame(
    data.groupby("Country")
    ["Recovered"].sum().nlargest(10).sort_values(ascending=False)
)
fig3 = px.bar(
    top10_recovered,
    x=top10_recovered.index,
    y="Recovered",
    height=600,
    color="Recovered",
    title = "Top 1- Recovered Cases Countries",
    color_continuous_scale=px.colors.sequential.Viridis,
)
fig3.write_html("Fif3.html", auto_open=True)

topstates_us = data["Country"] == "US"
topstates_us = data[topstates_us].nlargest(5, "Confirmed")

topstates_brazil = data["Country"] == "Brazil"
topstates_brazil = data[topstates_brazil].nlargest(5, "Confirmed")

topstates_india = data["Country"] == "India"
topstates_india = data[topstates_india].nlargest(5, "Confirmed")

topstates_russia = data["Country"] == "Russia"
topstates_russia = data[topstates_russia].nlargest(5, "Confirmed")

fig4 = go.figure(
    data=[
        go.bar(
            name="Confirmed Cases",
            x=topstates_us["Confirmed"],
            y=topstates_us["State"],
            orientation="h",
        ),
        go.Bar(
            name="Death Cases",
            x=topstates_us["Deaths"],
            y=topstates_us["State"],
            orientation="h",
        ),
    ]
)
fig4.update_layout(title="Most Affected States in USA", height=600)
