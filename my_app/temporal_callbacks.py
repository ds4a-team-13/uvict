from dash.dependencies import Output, Input
from my_app.utils import *
import pandas as pd


###############################################################
# VARIABLES GLOBALES
###############################################################
df = pd.read_csv('data/news_categorized.csv')#, nrows=100)
df['fecha_publicacion']=pd.to_datetime(df['fecha_publicacion'])
###############################################################

lista_news_categoria_0 = []
lista_news_categoria_1 = []
lista_news_categoria_2 = []
lista_news_categoria_3 = []
tituloNotica = "Titulo noticia"
fechaNoticia = "Fecha noticia"
cuerpoNoticia = "Cuerpo noticia"
urlNoticia = ""
valor_lista_cat_0 = -1
valor_lista_cat_1 = -1
valor_lista_cat_2 = -1
valor_lista_cat_3 = -1

def register_callbacks(app):

  # Actualiza la lista de noticias de cada categoria
  # dependiendo del rango de fechas seleccionado
  @app.callback([
  Output('noticias_categoria_0', 'options'),
  Output('noticias_categoria_1', 'options'),
  Output('noticias_categoria_2', 'options'),
  Output('noticias_categoria_3', 'options')
  ],
  [
  Input('my-date-picker-range', 'start_date'),
  Input('my-date-picker-range', 'end_date')
  ])
  def actualiza_semanas(minimo, maximo):

      global lista_news_categoria_0
      global lista_news_categoria_1
      global lista_news_categoria_2
      global lista_news_categoria_3

      lista_news_categoria_0 = crear_listado_noticias(df, 0, minimo, maximo)
      lista_news_categoria_1 = crear_listado_noticias(df, 1, minimo, maximo)
      lista_news_categoria_2 = crear_listado_noticias(df, 2, minimo, maximo)
      lista_news_categoria_3 = crear_listado_noticias(df, 3, minimo, maximo)

      return lista_news_categoria_0,\
              lista_news_categoria_1,\
              lista_news_categoria_2,\
              lista_news_categoria_3

  # Caundo se cambie el valor de uno de los RadioItems
  # se rellena el visor de noticia con la info de la noticia correspondiente
  @app.callback([
  Output('Titulo noticia', 'children'),
  Output('fecha noticia', 'children'),
  Output('cuerpo noticia', 'children'),
  Output('vinculo noticia', 'children'),
  Output('vinculo noticia', 'href')],
  [
  Input('noticias_categoria_0', 'value'),
  Input('noticias_categoria_1', 'value'),
  Input('noticias_categoria_2', 'value'),
  Input('noticias_categoria_3', 'value')
  ])
  def activa_boton_c0(valor0, valor1, valor2, valor3):

      global tituloNotica
      global fechaNoticia
      global cuerpoNoticia
      global urlNoticia
      global valor_lista_cat_0
      global valor_lista_cat_1
      global valor_lista_cat_2
      global valor_lista_cat_3

      if valor0 != valor_lista_cat_0:
          valor = valor0
      elif valor1 != valor_lista_cat_1:
          valor = valor1
      elif valor1 != valor_lista_cat_2:
          valor = valor2
      elif valor1 != valor_lista_cat_3:
          valor = valor3
      else:
          valor = -1

      valor_lista_cat_0 = valor0
      valor_lista_cat_1 = valor1
      valor_lista_cat_2 = valor2
      valor_lista_cat_3 = valor3

      try:
          tituloNotica = df[df['ID']==valor].titulo
          fechaNoticia = df[df['ID']==valor].fecha_publicacion
          cuerpoNoticia = df[df['ID']==valor].cuerpo.values[0]
          urlNoticia = df[df['ID']==valor].url.values[0]
      except:
          tituloNotica = "Titulo noticia"
          fechaNoticia = "Fecha noticia"
          cuerpoNoticia = "Cuerpo noticia"
          urlNoticia = ""

      return tituloNotica, fechaNoticia, cuerpoNoticia, urlNoticia, urlNoticia
