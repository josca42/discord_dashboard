# flake8: noqa E501
from dash import dcc
from dash import html
from dashboard.app.app import app
from dash.dependencies import Input, Output
import dash
from dash import dcc
from datetime import datetime, timedelta


def navigation():
    return html.Nav(
        [
            # html.Ul(
            #     [
            #         html.Div(className="topbar-divider d-none d-sm-block"),
            #         html.Li(
            #             [
            #                 html.A(
            #                     [
            #                         html.I(
            #                             className="fas fa-flag fa-sm fa-fw me-2 text-gray-400",
            #                         ),
            #                         html.Span(
            #                             "DK",
            #                             className="mr-2 d-none d-lg-inline text-gray-600 small",
            #                             id="country",
            #                         ),
            #                     ],
            #                     className="nav-link dropdown-toggle",
            #                     href="#",
            #                     id="userDropdown",
            #                     role="button",
            #                     **{
            #                         "data-bs-toggle": "dropdown",
            #                         "aria-haspopup": "true",
            #                         "aria-expanded": "false",
            #                     },
            #                 ),
            #                 html.Div(
            #                     [
            #                         html.Button(
            #                             [
            #                                 html.I(
            #                                     className="fas fa-flag fa-sm fa-fw me-2 text-gray-400"
            #                                 ),
            #                                 "DK",
            #                             ],
            #                             className="dropdown-item",
            #                             id="country-denmark",
            #                         ),
            #                         html.Div(className="dropdown-divider"),
            #                         html.Button(
            #                             [
            #                                 html.I(
            #                                     className="fas fa-flag fa-sm fa-fw me-2 text-gray-400"
            #                                 ),
            #                                 "NL",
            #                             ],
            #                             className="dropdown-item",
            #                             id="country-netherlands",
            #                         ),
            #                     ],
            #                     className="dropdown-menu dropdown-menu-right shadow animated--grow-in",
            #                     **{"aria-labelledby": "userDropdown"},
            #                 ),
            #             ],
            #             className="nav-item dropdown no-arrow",
            #         ),
            #     ],
            #     className="navbar-nav ms-auto",
            # ),
        ],
        className="navbar navbar-expand navbar-light bg-white topbar mb-2 static-top shadow",
    )


# @app.callback(
#     Output("country", "children"),
#     [
#         Input("country-denmark", "n_clicks"),
#         Input("country-netherlands", "n_clicks"),
#     ],
# )
# def load_cards(btn1, btn2):
#     changed_id = [p["prop_id"] for p in dash.callback_context.triggered][0]
#     if changed_id == ".":
#         return "DK"
#     elif changed_id == "country-netherlands.n_clicks":
#         return "NL"
#     elif changed_id == "country-denmark.n_clicks":
#         return "DK"
#     else:
#         return "Error"
