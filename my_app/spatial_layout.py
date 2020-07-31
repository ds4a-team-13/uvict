import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px

import datetime as dt

categories = dbc.Select(
    id="class-picker",
    options=[
        {"label": "All", "value": -1},
        {"label": "Conflicto armado", "value": 1},
        {"label": "Tráfico", "value": 2},
        {"label": "Categoría 3", "value": 3},
        {"label": "Eventos de tránsito", "value": 4},
    ],
    value=-1,
)

options_bar = html.Div(
        id='options-bar',
        className='row',
        children=[
            html.Div(
                className='col-2 align-middle',
                children=['Dates range:']
            ),
            html.Div(
                className='col-4',
                children=[dcc.DatePickerRange(
                            id='date-picker',
                            min_date_allowed=dt.datetime(2012,1,1),
                            max_date_allowed=dt.datetime.now(),
                            start_date=dt.datetime(2020,1,1),
                            end_date=dt.datetime(2020, 6, 28),
                            initial_visible_month=dt.datetime(2020, 6, 28)
                            ),
                        ]
            ),
            html.Div(
                className='col-2 align-middle',
                children=['Category:']
            ),
            html.Div(
                className='col-4',
                children=[categories]
            ),
            
        ]
    )

content = dbc.Container(children=[

  dcc.Store(id='spatial_data'),
  dcc.Store(id='dptos_data'),

  html.Div(
    className='row',
    children=[
      options_bar,
      html.Div(
        className='col-6 container',
        children=[
          html.Div(className='plotContainer', children=[
            html.H4('Publicaciones por periodo de tiempo'),
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
        className='col-4 container',
        style={'display':'None'},
        children=[
          html.Div(className='plotContainer', children=[
            html.H4('Publicaciones por category'),
            dcc.Loading(
              id="loading-2",
              className='loader',
              type="default",
              children=html.Div(id='categories',)
            ),
          ])
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