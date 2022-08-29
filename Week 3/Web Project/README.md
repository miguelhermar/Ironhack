<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Project: API & Web Data Scraping and Web Data Pipeline (Art Theft FBI)
*Miguel Ángel Hernández Márquez*

*Agosto 2022, México, 26 de agosto*

## Contenido
- [Descripción del proyecto y librerías utilizadas](#descripción-del-proyecto-y-librerías-utilizadas)
- [API info](#api-info)
- [Insights sobre la API](#insights-sobre-la-api)
- [Web Scraping](#web-scraping)

## Descripción del proyecto y librerías utilizadas
El objetivo del proyecto es recolectar los datos de la API del FBI sobre las piezas más robadas (art theft) y posteriormente realizar
un web scraping para encontrar los lugares donde estas piezas han estado y en que año se han hecho o se han replicado. Las librerías utilizadas en este proyecto son las siguientes:

- Requests: para hacer la solicitud HTTP de la url de la API.
- Pandas: con el objetivo de estructurar los datos obtenidos en un dataframe y poder realizar un análisis básico de la información.
- Beautiful Soup: para extraer los datos de los archivos HTML de las páginas web donde se hizo web scraping.
- Re: con el fin de obtener información específica al hacer web scraping de diferentes páginas web. 
    
## API info
Los datos de la API incluyen delitos relacionados con el arte y la propiedad cultural, tales como robo, fraude, saqueo y tráfico a través de fronteras estatales e internacionales. Los datos obtenidos por cada pieza de arte incluyen el material del que está hecho, título, categoría del crimen, medidas, descripción, entre otros.

## Insights sobre la API
Se empieza por hacer un breve análisis de los datos que se obtienen de la API. En este caso, se hizo un agrupamiento por categoría crimen, título y autor. Posteriormente, con el fin de obtener resultados más precisos se considera el agrupamiento tanto por título, autor y categorías. De esta manera, el resultado fue diferente a los previos, ya que se encontró que las mismas piezas del mismo autor habían sido robadas en varias ocasiones.
  

## Web Scraping
Con estos últimos resultados, se realizó un web scraping de las top 3 piezas más robadas junto con sus autores en diferentes páginas web, con el objetivo de conocer alguno de los lugares donde se encontraban estas piezas, así como el año en que se han hicieron la original o la réplica. Estos fueron los resultados:
1. Tyree Guyton: Faces in the Hood Series (Alabama, USA)
2. Salvador Dalí: Lincoln in Dalivision (Miami, USA y Figueres, España)
3. Claudius Ptolomeus: Cosmographia (Buckinghamshire, United Kingdom)
