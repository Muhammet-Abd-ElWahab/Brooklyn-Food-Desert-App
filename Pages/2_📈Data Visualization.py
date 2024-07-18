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

#==========================================================================#
#                          Page Configs
#==========================================================================#

st.set_page_config(page_title="Data Disualization",
                   page_icon = "📊",
                   layout="wide"
                )



# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv('LILAZones_geo.csv')
    data['geometry'] = data['geometry'].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(data, geometry='geometry')
    gdf.set_crs(epsg=4326, inplace=True)  # Set CRS to WGS84
    return gdf





def main():
    map_type = st.tabs(["LILA & Non-LILA Zones","Supermarket Coverage Ratio","Fast Food Coverage Ratio" ])
    gdf = load_data()
    with map_type[0]:
            st.header("LILA & Non-LILA Zones")

            search_query = st.sidebar.selectbox(
                "Search for NTA Name:",
                options=["All"] + gdf['NTA Name'].unique().tolist()
            )
            
            if search_query != "All":
                filtered_gdf = gdf[gdf['NTA Name'] == search_query]
                if not filtered_gdf.empty:
                    row = filtered_gdf.iloc[0]
                    st.sidebar.subheader(f"Details for {row['NTA Name']}")
                    st.sidebar.write(f"**Food Index:** {row['Food Index']}")
                    st.sidebar.write(f"**Median Family Income:** {row[' Median Family Income ']}")
                    st.sidebar.write(f"**Poverty Rate:** {row['Education below high school diploma (Poverty Rate)']}")
                    st.sidebar.write(f"**SNAP Benefits:** {row['SNAP Benefits %']}")
            else:
                filtered_gdf = gdf
            options = st.radio("select", ["Single year", "Range"], label_visibility="hidden")
            if options == "Single year":
                # Input for a single year
                col1, col2, col3 = st.columns(3)
                with col1:
                    year = st.selectbox("Select a year:", ["All", 2010,2011,2012,2013,2014,2015,2016,2017])
                    st.write(f"Selected year: {year}")
            else:
                # Slider for a range of years
                col1, col2, col3 = st.columns(3)
                with col1:
                    start_year, end_year = st.slider(
                        "Select a range of years:",
                        min_value=2010,
                        max_value=2017,
                        value=(2010, 2017)
                    )
                    st.write(f"Selected range: {start_year} - {end_year}")
            # year = st.slider("Select a year", min_value=2010,max_value=2024, step=1, value=(2010,2024))
            m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
            folium.GeoJson(
                filtered_gdf,
                style_function=lambda feature: {
                    'fillColor': 'red',
                    'color': 'red',
                    'weight': 1,
                    'fillOpacity': 0.6,
                },
                tooltip=folium.GeoJsonTooltip(
                    fields=['NTA Name', 'Food Index', ' Median Family Income ', 'Education below high school diploma (Poverty Rate)', 'SNAP Benefits %'],
                    aliases=['NTA Name:', 'Food Index:', 'Median Family Income:', 'Poverty Rate:', 'SNAP Benefits:'],
                    localize=True
                )
            ).add_to(m)
            st_folium(m, width=800, height=600)

            # Share App button with Gmail link
            share_text = "Check out this Food Desert Analysis App!"
            app_link = "https://samplefooddesert01.streamlit.app/"
            mailto_link = f"mailto:?subject=Food Desert Analysis App&body={share_text}%0A{app_link}"
            st.sidebar.markdown(f'<a href="{mailto_link}" target="_blank"><button style="background-color:green;color:white;border:none;padding:10px 20px;text-align:center;text-decoration:none;display:inline-block;font-size:16px;margin:4px 2px;cursor:pointer;">Share App via Email</button></a>', unsafe_allow_html=True)

            # Download CSV button
            csv = gdf.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="LILAZones_geo.csv"><button style="background-color:blue;color:white;border:none;padding:10px 20px;text-align:center;text-decoration:none;display:inline-block;font-size:16px;margin:4px 2px;cursor:pointer;">Download CSV</button></a>'
            st.sidebar.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
     main()








