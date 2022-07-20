"""Instantiate a Dash app."""
import dash
from dash import dash_table
from dash import dcc
from dash import html

from .data import create_dataframe
import plotly.express as px

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/",
    )

    # Load DataFrame
    df = create_dataframe()

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure={
                    "data": [
                        {'x': df["Metrics_60s"], 'y': df["Average_60s"], 'type': 'bar', 'name': '60 sec', },
                        {'x': df["Metrics_60m"], 'y': df["Average_60m"], 'type': 'bar', 'name': '60 min', },
                    ],
                    "layout": {
                        "title": "Dashboard Redis",
                        "height": 500,
                        "padding": 150,
                    },
                },
            ),
            create_data_table(df),
        ],
        id="dash-container",
    )
    return dash_app.server


def create_data_table(df):
    #Create Dash datatable from Pandas DataFrame.
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        page_size=200,
    )
    return table