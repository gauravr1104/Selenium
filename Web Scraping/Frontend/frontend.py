import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from main import scrapping
st.title("Google Maps Scraper")

query = st.text_input("Enter a value:", "")

if st.button("Scrape"):
    if not query.strip():
        st.error("Please enter a valid search query.")
    else:
        with st.spinner("Scraping data... This may take a while."):
            try:
                scrapping(query)
                df = pd.read_csv("map_data.csv")
                st.success("Scraping completed successfully!")
                st.dataframe(df)

                # Provide download button for CSV
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='map_data.csv',
                    mime='text/csv',
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
