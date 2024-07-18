import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_extras.colored_header import colored_header 



#==========================================================================#
#                          Page Configs
#==========================================================================#

st.set_page_config(page_title="Home",
                   page_icon = "🏚️",
                   layout="wide"
                )


def main():
        st.markdown(f'<h2 style="color: firebrick; text-align: center">Welcome to the Food Desert Analysis App</h2>', unsafe_allow_html=True)
        st.markdown(f'<p style=" text-align: center;border-top: 2px solid  #1CCAE0; margin:0 290px"></p>', unsafe_allow_html=True)
        st.markdown(f'<h4 style="color: #00BFFF; text-align: center">This app helps to analyze food desert regions in Brooklyn.</h4>', unsafe_allow_html=True)

        st.markdown(
    """
    <style>
    .fullScreenImage {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 10%;
        height: 60vh;
        object-fit: contain; 

    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load and display the image
        st.image('https://images.pexels.com/photos/2706653/pexels-photo-2706653.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', use_column_width=True, caption='food desert regions in Brooklyn')




if __name__ == "__main__":
        main()  
