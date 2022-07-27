# flake8: noqa E501

from dash import dcc
from dash import html
import base64


def sidebar(sidebar_context):
    return html.Ul(
        [
            logo_item("dashboard/app/assets/integral.png", 20, 20),
            html.Hr(className="sidebar-divider my-0"),
            *(
                [
                    sidebar_item(elem["title"], elem["icon"], elem["href"])
                    for elem in sidebar_context
                ]
            ),
            html.Hr(className="sidebar-divider d-none d-md-block"),
            html.Div(
                html.Button(className="rounded-circle border-0", id="sidebarToggle"),
                className="text-center d-none d-md-inline",
            ),
        ],
        className="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion",
    )


def logo_item(image_filename, height, width):

    encoded_image = base64.b64encode(open(image_filename, "rb").read())
    return dcc.Link(
        [
            html.Div(
                html.Img(
                    src="data:image/png;base64,{}".format(encoded_image.decode()),
                    style={"height": f"{height}%", "width": f"{width}%",},
                ),
            ),
        ],
        className="sidebar-brand d-flex align-items-center justify-content-center",
        href="/",
    )


def sidebar_item(title, icon, href, active=False):
    class_name = "nav-item" + (" active" if active else "")
    return html.Li(
        dcc.Link(
            [html.I(className=icon), html.Span(title)], className="nav-link", href=href,
        ),
        className=class_name,
    )
