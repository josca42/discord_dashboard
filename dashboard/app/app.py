from dash import Dash

CSS = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
]
JS = [
    "https://code.jquery.com/jquery-3.5.1.slim.min.js",
    "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js",  # noqa: E501
]

app = Dash(
    __name__,
    external_scripts=JS,
    external_stylesheets=CSS,
    suppress_callback_exceptions=True,
)
server = app.server
