import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px

import datetime as dt




content = dbc.Container(children=[

  dcc.Store(id='spatial_data'),
  dcc.Store(id='dptos_data'),

  html.H2(id='section-title'),

  html.Div(
    className='row',
    children=[
      #options_bar,
      html.Div(
        className='col-6 container',
        children=[
          html.Div(className='plotContainer', children=[
            html.H4('Publicaciones por periodo de tiempo', id="trends-title"),
            dcc.Loading(
              id="loading-1",
              className='loader',
              type="default",
              children=html.Div(id='trends')
            ),
          ]),
        ]
      ),
      
      html.Div(
        className='col-6 container',
        children=[
          html.Div(className='plotContainer', id='mapContainer', children=[
            html.H4('Cantidad de noticias por departamento'),
            dcc.Loading(
              id="loading-3",
              className='loader',
              type="default",
              children=html.Div(id='map-object',)
            ),
          ])
        ]
      ),

      html.Div(
        className='col-12 container',
        children=[
          html.Div(className='plotContainer', children=[
            html.H4('Cantidad de noticias por departamento'),
            dcc.Loading(
              id="loading-4",
              className='loader',
              type="default",
              children=html.Div(id='wordscloud',)
            ),
          ]),
        ]
      ),
        
      
    ]
  )

  
])

"""
  dcc.Store(id='spatial_data'),
  dcc.Store(id='dptos_data'),

  html.Div(className="row", children=[
    html.Div(className="col-1"),
    html.Div(id='date-picker-container', className="col-5", children=[
      html.P('Rango de fechas:'),
      dcc.DatePickerRange(id='date-picker'),
    ]),
    html.Div(id='class-picker-container', className="col-5", children=[
      dbc.Label("Clase"),
      dcc.Dropdown(id="class-picker"),
    ]),
    html.Div(className="col-1"),
  ]),

  html.Div(id="main-container", className="row", children=[
    html.Div(className="col-1"),
    html.Div(className="col-5", children=[
      dcc.Graph(id='map-object',)
    ]),
    html.Div(className="col-5", id='wordscloud'),
    html.Div(className="col-1"),
  ]),
"""