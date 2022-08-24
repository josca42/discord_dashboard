# flake8: noqa E501
from time import sleep

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
from dash import dcc
import numpy as np
from datetime import datetime, timedelta

from dashboard.app.app import app
from dashboard.app.components.cards import card, grid_card, tab_card
from dashboard.app.components.wrappers import main_wrapper

from src.db import crud
from src.data.CONSTANTS import CHANNEL_ID2NAME
import plotly.graph_objects as go

pd.options.plotting.backend = "plotly"

CHANNEL_NAME2ID = {v: k for k, v in CHANNEL_ID2NAME.items()}
GRAPH_LAYOUT = {"margin": {"t": 10, "l": 20, "r": 20, "b": 20}}


def layout(sidebar_context):
    title = html.H2("")
    dropdown = dcc.Dropdown(
        list(CHANNEL_NAME2ID.keys()),
        list(CHANNEL_NAME2ID.keys()),
        id="channel_dropdown",
        multi=True,
    )
    fig_row1 = html.Div(
        [
            html.Div(
                grid_card(
                    "Daily content posted",
                    dcc.Graph(
                        id="ts-content-posted",
                        figure={"layout": GRAPH_LAYOUT, "data": []},
                        className="h-100",
                        style={"minHeight": "100px"},
                        responsive=True,
                    ),
                ),
                className="col-12 pt-2 pb-4",
            ),
        ],
        className="row flex-grow-1",
    )
    fig_row2 = html.Div(
        [
            html.Div(
                grid_card(
                    "Daily active users",
                    dcc.Graph(
                        id="ts-active-users",
                        figure={"layout": GRAPH_LAYOUT, "data": []},
                        className="h-100",
                        style={"minHeight": "100px"},
                        responsive=True,
                    ),
                ),
                className="col-12 pt-2 pb-4",
            ),
        ],
        className="row flex-grow-1",
    )

    return main_wrapper([title, dropdown, fig_row1, fig_row2], sidebar_context,)


@app.callback(
    [Output("ts-content-posted", "figure"), Output("ts-active-users", "figure")],
    [Input("channel_dropdown", "value")],
)
def update_event_map(channel_names):

    channel_ids = [CHANNEL_NAME2ID[name] for name in channel_names]

    df = crud.message.get_channel_messages(channel_ids)
    df = df.set_index("timestamp")

    df["content_len"] = df["content"].str.len()

    fig_content_posted = df.resample("D")["content_len"].sum().plot()
    fig_active_users = df.resample("D")["author"].nunique().plot()

    fig_layout = {
        "plot_bgcolor": "white",
        "xaxis": {"title": ""},
        "yaxis": {"title": ""},
        "showlegend": False,
    }
    fig_active_users.update_layout(fig_layout)
    fig_content_posted.update_layout(fig_layout)

    return fig_content_posted, fig_active_users


# def add_fig_annotations(fig, df):
#     def _get_y_vals(lecture_dates, s_content):
#         y = []
#         for lecture_date in lecture_dates:
#             y.append(s_content.loc[lecture_date])
#         return y

#     balaji_lecture = []
#     discord_meetup = []
#     lecture_date = datetime(2021, 12, 2)
#     for i in range(4 * 9):

#         if i <= 4 * 4:
#             balaji_lecture.append(lecture_date)
#         else:
#             discord_meetup.append(lecture_date)

#         lecture_date += timedelta(days=7)

#     fig.add_trace(
#         go.Scatter(
#             x=balaji_lecture,
#             y=_get_y_vals(balaji_lecture, df),
#             mode="markers",
#             name="Balaji lecture",
#             visible="legendonly",
#         )
#     )
#     fig.add_trace(
#         go.Scatter(
#             x=discord_meetup,
#             y=_get_y_vals(discord_meetup, df),
#             mode="markers",
#             name="Discord Meetup",
#             visible="legendonly",
#         )
#     )

