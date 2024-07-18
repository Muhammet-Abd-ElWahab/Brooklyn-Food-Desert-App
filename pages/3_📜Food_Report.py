import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_extras.colored_header import colored_header 
import plotly.express as px
import pandas as pd
from shapely import wkt
import base64
import streamlit as st
import folium
from streamlit_folium import st_folium
import json

st.set_page_config(page_title="Food Reports",
                   page_icon = "📊",
                   layout="wide"
                )
