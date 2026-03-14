import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction")

sqft = st.number_input("Square Feet")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
offers = st.number_input("Offers")

brick = st.selectbox("Brick House", ["Yes","No"])
neighborhood = st.selectbox("Neighborhood", ["East","North","West"])

brick = 1 if brick=="Yes" else 0

east = north = west = 0

if neighborhood == "East":
    east = 1
elif neighborhood == "North":
    north = 1
else:
    west = 1

if st.button("Predict Price"):

    data = pd.DataFrame([[sqft,bedrooms,bathrooms,offers,brick,east,north,west]],
    columns=['SqFt','Bedrooms','Bathrooms','Offers','Brick',
             'Neighborhood_East','Neighborhood_North','Neighborhood_West'])

    prediction = model.predict(data)

    st.success(f"Predicted Price: {prediction[0]}")