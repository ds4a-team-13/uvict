from dash.dependencies import Output, Input
from my_app.utils import *

def register_callbacks(app):

    # Presenta la imagen del logo
    @app.callback(Output("logo", 'children'), [Input('none', 'children')])
    def image_logo(none):
        return html.Img(
          src=app.get_asset_url('logo 2.png'),
          style={
              "height":"150px",
              "width": "auto",
              "margin-bottom": "25px"
          }
        )

    @app.callback(Output('url', 'pathname'),
    [
    Input('boton_modelo', 'n_clicks'),
    Input('boton_revision', 'n_clicks'),
    Input('boton_visualizacion', 'n_clicks')
    ])
    def muestra_modelo(n1, n2, n3):
        if n1 and n1>0:
            return "/semantic", None, None, None
        elif n2 and n2>0:
            return "/temporal", None, None, None
        elif n3 and n3>0:
            return "/spatial", None, None, None
