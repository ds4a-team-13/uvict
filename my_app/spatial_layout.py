import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.express as px

import datetime as dt


categories = dbc.Select(
    id="class-picker",
    options=[
        {"label": "All", "value": -1},
        {"label": "Narcóticos", "value": 1},
        {"label": "Contrabando", "value": 2},
        {"label": "Grupos armados", "value": 3},
        {"label": "Delitos sexuales", "value": 4},
    ],
    value=-1,
)


options_bar = html.Div(
        id='options-bar',
         className='row',
         children=[
             html.Div(
                 className='col-2 align-middle',
                 children=['Rango de fechas:']
             ),
             html.Div(
                 className='col-4',
                 children=[dcc.DatePickerRange(
                             id='date-picker',
                             min_date_allowed=dt.date(2012,1,1),
                             max_date_allowed=dt.datetime.now().date(),
                             start_date=dt.date(2020, 5,1),
                             end_date=dt.date(2020, 6, 28),
                             initial_visible_month=dt.date(2020, 5, 1)
                             ),
                         ]
             ),
             html.Div(
                 className='col-2 align-middle',
                 children=['Agrupamiento:']
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

  options_bar,
  html.Div(
    className='row',
    children=[
      html.H3(id='section-title', className='spatialTitle'),
      #html.P('A continuación usted puede ...', className='col-12'),
      html.Div(
        className='col-6 container',
        children=[
          html.Div(className='plotContainer', children=[
            html.H4('¿Cuántas noticias se publican cada día?', id="trends-title"),
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
            html.H4('¿En que departamentos se publican más noticias?'),
            dcc.Loading(
              id="loading-3",
              className='loader',
              type="default",
              children=html.Div(
                dcc.Graph(
                  id='map-object', 
                  config={'displayModeBar': False}
                  )
              )
            ),
          ])
        ]
      ),

      html.Div(
        className='col-12 container',
        children=[
          html.Div(className='plotContainer', children=[
            html.H4('¿Cuáles son las palabras más usadas en esas noticias?'),
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

