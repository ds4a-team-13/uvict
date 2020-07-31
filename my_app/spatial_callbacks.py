from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

from datetime import datetime as dt
from unidecode import unidecode
from datetime import timedelta
from wordcloud import WordCloud
import geopandas as gpd
from io import BytesIO
import pandas as pd
import random, json
import base64
import dash
from dash.exceptions import PreventUpdate

import my_app.utils as utils

dptos_path = 'data/deptos.json'
gdf = gpd.read_file(dptos_path)
gdf['nombre'] = gdf['NOMBRE_DPT'].apply(unidecode).str.lower()
dptos_ids = {n: fid for i, n, fid in gdf[['nombre', 'DPTO']].itertuples()}



with open(dptos_path) as response:
    dptos = json.load(response)

colors = {'identity':'#eb3b5a', 'identity':'#fa8231', 
          'identity':'#20bf6b', 'identity':'#0fb9b1', 
          'identity':'#8854d0', 'identity':'#a5b1c2',
          'identity':'#2d98da', 'identity':'#f7b731',
          }

colors = {'identity':'#4b6584', 'identity':'#a5b1c2', 
          'identity':'#8854d0', 'identity':'#2d98da', 
          'identity':'#20bf6b', 'identity':'#f7b731',
          'identity':'#fa8231', 'identity':'#fc5c65',
          }

def register_callbacks(app):
  """
  @app.callback(
      [
        Output('date-picker', 'min_date_allowed'), 
        Output('date-picker', 'max_date_allowed'), 
        Output('date-picker', 'start_date'), 
        Output('date-picker', 'end_date'), 
        Output('date-picker', 'initial_visible_month'), 
      ],
      [Input('url', 'pathname')]
  )
  def load_date_picker(pathname):
      print('>> load_date_picker')
      query = '''select min(fecha_publicacion) as min_date, 
                 max(fecha_publicacion) as max_date from featuring_all LIMIT 1'''
      data = utils.db_get_df(query)
      data['min_date'] = pd.to_datetime(data['min_date'])
      data['max_date'] = pd.to_datetime(data['max_date'])
      
      data = data.iloc[0]
      initial_date = data['max_date'] - timedelta(days=10)
      
      return data['min_date'].date(),\
             data['max_date'].date(),\
             initial_date.date(),\
             data['max_date'].date(),\
             initial_date.date()
  """

  @app.callback(
      Output('spatial_data', 'data'), 
      [
        Input('date-picker', 'start_date'), 
        Input('date-picker', 'end_date'), 
        Input('class-picker', 'value'),
        Input('map-object', 'clickData'),
        Input('dptos_data', 'data'),
        Input('url', 'href')
      ]
  )
  def initialize_selected_dpt(start_date, end_date, category, clickData, dptosData, pathname):
    ctx = dash.callback_context
    data = {}
    print('>> seting data')
    print(ctx.triggered)
    
    triggers = [x['prop_id'] for x in ctx.triggered]
    
    data['start_date'] = start_date
    data['end_date']   = end_date
    data['category']   = category
    
    ctx_msg = json.dumps({
        'states': ctx.states,
        'triggered': ctx.triggered,
        'inputs': ctx.inputs
    }, indent=2)
    print(triggers)
    if "map-object.clickData" in triggers:
      idx = clickData['points'][0]['pointIndex']
      data['dpto_index'] = idx
    
    print(data)
    return data

  @app.callback(
      Output("wordscloud", "children"),
      [Input('spatial_data', 'data')],
	)
  def generate_wordcloud_callback(data):
    #return "Temporarily disabled"
    return generate_wordcloud(data)
  

  @app.callback(
      Output("map-object", "children"),
      [Input('spatial_data', 'data')],
	)
  def generate_map_callback(data):
    fig_map = generate_map(data)
    return fig_map


  @app.callback(
      Output("trends", "children"),
      [Input('spatial_data', 'data')],
	)
  def generate_trends_callback(data):
    where_cond = utils.generate_where_cond(data)
    query = f"""
              SELECT strftime('%Y-%m-%d', fecha_publicacion) as fecha,
                     category_bl as categoria,
                     count(1) as noticias
              FROM featuring_all
              {where_cond}
              GROUP BY strftime('%Y-%m-%d', fecha_publicacion), category_bl

            """

    data = utils.db_get_df(query)
    fig = px.line(data, x="fecha", y="noticias", color='categoria', color_discrete_map=colors)
    
    return dcc.Graph(figure=fig, config={'displayModeBar': False} )


  @app.callback(
    Output("categories", "children"),
    [Input('spatial_data', 'data')],
	)
  def generate_categories_callback(data):
    where_cond = utils.generate_where_cond(data)
    query = f"""
              SELECT category_bl as categoria,
                     count(1) as noticias
              FROM featuring_all
              {where_cond}
              GROUP BY strftime('%Y-%m-%d', fecha_publicacion), category_bl

            """
    data = utils.db_get_df(query)
    fig = px.pie(data, values="noticias", names="categoria", color_discrete_map=colors, title='Prueba')
    
    return dcc.Graph(figure=fig, config={'displayModeBar': False} )


  def generate_wordcloud(data):
    print('>> generate_wordcloud', data)
    where_cond = utils.generate_where_cond(data)
    query = f"""
              SELECT pre_clean_text, departamentos, url
              FROM featuring_all  
              {where_cond}
            """

    print(1)
    data = utils.db_get_df(query)
    print(2)
    common_words = utils.get_top_n_words(data['pre_clean_text'], 100, 2)
    print(4)

    frequencies = {x[0]:x[1] for x in common_words}
    print(5)
    wc = WordCloud(background_color='white', width=1200, height=600).generate_from_frequencies(frequencies=frequencies)
    print(6)
    
    wc_img = wc.to_image()
    print(7)
    with BytesIO() as buffer:
        wc_img.save(buffer, 'png')
        print(8)
        img2 = base64.b64encode(buffer.getvalue()).decode()

    print('<< generate_wordcloud')
    return html.Img(src="data:image/png;base64," + img2)
           
    
  def generate_map(data):
    print('>> generate_map')
    where_cond = utils.generate_where_cond(data)
    query = f"""
          SELECT fid, count(1) as noticias
          FROM featuring_all  
          {where_cond}
          GROUP BY fid
        """

    data = utils.db_get_df(query)
    
    token = "pk.eyJ1IjoiaGVybmFuZGNiIiwiYSI6ImNrZDI4MjVqazBqd3Uyc251bGdnZG03Z2gifQ.qxv2EjANpDl3-2y5Ohi4kA"
    fig = px.choropleth_mapbox(
              data,
              geojson=dptos, 
              locations='fid', 
              color='noticias', 
              featureidkey='properties.DPTO',
              color_continuous_scale="Viridis",
              range_color=(0, data['noticias'].quantile(.8)),
              zoom=4, 
              center = {"lat": 4.90, "lon": -74.16},
              opacity=0.5,
              labels={'noticias':'noticias'},
            )

    fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0}, 
        mapbox_style="light", 
        mapbox_accesstoken=token,
    )
    fig.update_layout(showlegend=True)
    """
    fig.update_layout({
      'plot_bgcolor': 'red',
      'paper_bgcolor': '#1e1e1e',
    })
    """
    
    
    print('<< generate_map')
    return dcc.Graph(figure=fig, config={'displayModeBar': False}  )


  def proccess_dptos(data):
    data = data[~data['departamentos'].fillna('').str.contains('\|')]
    data = data.dropna(subset=['departamentos'])

    data['departamentos'] = data['departamentos'].str.replace('guania','guainia')\
                                                .str.replace('bogota', 'cundinamarca')\
                                                .str.replace('guajira', 'la guajira')

    data['fid'] = data['departamentos'].apply(lambda x: dptos_ids.get(x, -1))
    data = data.groupby('departamentos').agg({'fid':'min', 'url':'size'})
    
    return data.sort_index()


