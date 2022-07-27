# flake8: noqa E501

from dash import html

from dashboard.app.components.navigation import navigation
from dashboard.app.components.sidebar import sidebar


def main_wrapper(element, sidebar_context):
    return html.Div(
        [
            sidebar(sidebar_context),
            html.Div(
                [
                    # navigation(),
                    html.Div(
                        element,
                        className="container-fluid flex-grow-1 d-flex flex-column",
                    ),
                ],
                id="content-wrapper",
                className="d-flex flex-column",
            ),
        ],
        id="wrapper",
    )
