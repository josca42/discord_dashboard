# flake8: noqa E501
from time import sleep

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import dash_table
import numpy as np

from dashboard.app.app import app
from dashboard.app.components.cards import card, grid_card, tab_card
from dashboard.app.components.wrappers import main_wrapper

from src.db import crud

table_cols_format = [
    {"id": "channel", "name": "channel"},
    {"id": "reactions", "name": "reactions"},
    {"id": "message_markdown", "name": "description", "presentation": "markdown"},
    {"id": "url_markdown", "name": "link", "presentation": "markdown"},
    {"id": "timestamp", "name": "timestamp"},
]


def layout(sidebar_context):

    tables = html.Div(
        [
            html.Div(
                tab_card(
                    None,
                    id="links",
                    elements=[
                        {"label": "Hot", "value": "hot"},
                        {"label": "New", "value": "new"},
                        {"label": "Max", "value": "max"},
                        {"label": "All", "value": "all"},
                    ],
                    value="hot",
                ),
                className="col-12 pt-2 pb-2",
            ),
        ],
        className="row flex-grow-1",
    )
    return main_wrapper([tables], sidebar_context,)


@app.callback(
    Output("linksBody", "children"), [Input("links", "value")],
)
def update_event_map(list_type):

    df = crud.link.get_multi()

    if list_type == "new":
        df = df.sort_values(by="timestamp", ascending=False).head(50)
    if list_type == "hot":
        df["hot_score"] = calc_hot_score(df)
        df = df.sort_values(by="hot_score", ascending=False).head(50)
    if list_type == "max":
        df = df.sort_values(by="reactions", ascending=False).head(50)
    if list_type == "all":
        pass

    df["link"] = (
        "https://discord.com/channels/"
        + df["guild_id"].astype(str)
        + "/"
        + df["channel_id"].astype(str)
        + "/"
        + df["message_id"].astype(str)
    )

    channel_id2name = {941211554689450064: "writers", 902967453183778836: "lectures"}
    df["channel"] = df["channel_id"].map(channel_id2name)

    df["message_markdown"] = (
        "["
        + df["content"].str[:100].str.replace(r"[()\n]", "", regex=True)
        + "]("
        + df["link"]
        + ")"
    )
    df["url_markdown"] = "[" + df["url"] + "](" + df["url"] + ")"

    if list_type == "new":
        df["timestamp"] = df["timestamp"].dt.strftime("%H:%M %d-%m-%Y")
    elif list_type in ["hot", "max"]:
        df["timestamp"] = df["timestamp"].dt.strftime("%d-%m-%Y")
    else:
        pass

    return dash_table.DataTable(
        id="link-table",
        data=df.to_dict("records"),
        columns=table_cols_format,
        tooltip_data=[
            {"message_markdown": {"value": content, "type": "markdown"}}
            for content in df["content"]
        ],
        style_as_list_view=True,
        style_cell={
            "textAlign": "left",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
            "backgroundColor": "white",
            "font-family": "Kanit ExtraLight",
            # "width": "100px",
            "maxWidth": "150px",
            # "minWidth": "100px",
        },
        style_cell_conditional=[
            {"if": {"column_id": "timestamp"}, "textAlign": "center"}
        ],
        filter_action="native" if list_type == "all" else "none",
        sort_action="native" if list_type == "all" else "none",
        style_header={
            "backgroundColor": "#f8f8ff",
            "font-family": "Kanit Light",
            "font-weight": "bold",
        },
        style_table={
            # "height": 900,
            "overflowX": "scroll",
            "overflowY": "auto",
        },
        tooltip_delay=0,
        tooltip_duration=None,
    )


def calc_hot_score(df):
    decay_constant = 0.3
    days_old = (pd.Timestamp.now() - df["timestamp"]).dt.days
    weights = np.exp(-1 * days_old * decay_constant)
    return df["reactions"] * weights
