from dash.dependencies import Output, Input
import dash_html_components as html

def register_callbacks(app):

    # Presenta la imagen del logo
    @app.callback(Output("logo2", 'children'), [Input('none2', 'children')])
    def image_logo(none):
        return html.Img(
          src=app.get_asset_url('logo 2.png'),
          style={
              "height":"250px",
              "width":"auto",
              "margin-bottom":"15px"
          }
        )

    # @app.callback(Output('url', 'pathname'),
    # [
    # Input('boton_modelo', 'n_clicks'),
    # Input('boton_revision', 'n_clicks'),
    # Input('boton_visualizacion', 'n_clicks')
    # ])
    # def muestra_modelo(n1, n2, n3):
    #     if n1 and n1>0:
    #         return "/semantic"
    #     elif n2 and n2>0:
    #         return "/temporal"
    #     elif n3 and n3>0:
    #         return "/spatial"
