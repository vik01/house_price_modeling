import streamlit as st
import pandas as pd
import numpy as np

st.subheader('Please Input Your Dream Home Specifications')
sqft = st.number_input("Property Area (Square Feet)", min_value=1)
bed = st.number_input("Number of Bedrooms", min_value=1)
bath=st.number_input("Number of Bathroms", min_value=1)

gen_predictions = st.button('Generate Predicted Cost')

if gen_predictions:
    predicted_price = sqft*100 +bed*400+bath*200 # replace with final prediction model
    st.subheader('Estimated Cost of your Dream Home: '+"$"+f'{round(predicted_price):,}')
    #st.divider()

    if sqft>1000:
        predicted_price_sqft = (sqft-500)*100 +bed*400+bath*200
        percent_saved_sqft = (predicted_price_sqft-predicted_price)/predicted_price *100
        st.metric(label="Estimated Cost of a Smaller Property Size", value=f"${(predicted_price_sqft):,}", delta= f"{percent_saved_sqft:.2f}%", delta_color='inverse')
        st.text(f'By looking at a smaller property with {sqft-500} square feet, you can save: ${(predicted_price-predicted_price_sqft):,}')

    if bed>1:
        predicted_price_bed = sqft*100 +(bed-1)*400+bath*200
        percent_saved_bed = (predicted_price_bed-predicted_price)/predicted_price *100
        st.metric(label="Estimated Cost of a Property with Fewer Bedrooms", value=f"${(predicted_price_bed):,}", delta= f"{percent_saved_bed:.2f}%", delta_color='inverse')
        st.text(f'By looking at a property with {bed-1} bedrooms, you can save: ${(predicted_price-predicted_price_bed):,}')
    
    if bath>1:
        predicted_price_bath = sqft*100 +bed*400+(bath-1)*200
        percent_saved_bath = (predicted_price_bath-predicted_price)/predicted_price *100
        st.metric(label="Estimated Cost of a Property with Fewer Bathrooms", value=f"${(predicted_price_bath):,}", delta= f"{percent_saved_bath:.2f}%", delta_color='inverse')
        st.text(f'By looking at a property with {bath-1} Bathrooms, you can save: ${(predicted_price-predicted_price_bath):,}')