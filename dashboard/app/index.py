import re

from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dashboard.app import views
from dashboard.app.app import app, server  # noqa: F401


app.layout = html.Div(
    [
        dcc.Location(id="urlNoRefresh"),
        dcc.Location(id="urlRefresh", refresh=True),
        html.Div(id="content"),
    ]
)
sidebar_context = [
    {"title": "Links", "href": "/links", "icon": "fa-solid fa-link"},
    {"title": "Health", "href": "/health", "icon": "fa-solid fa-heart-pulse"},
]


@app.callback(Output("content", "children"), [Input("urlNoRefresh", "pathname")])
def route(pathname):
    if pathname == "/":
        return views.links.layout(sidebar_context)
    elif pathname == "/links":
        return views.links.layout(sidebar_context)
    else:
        pass
    return views.error.layout(sidebar_context)


if __name__ == "__main__":
    app.run_server(debug=True)
