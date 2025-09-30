import streamlit as st
from helpers import read_api_endpoint, post_api_endpoint
import pandas as pd
from constants import ASSETS_PATH

iris_data = read_api_endpoint("/api")
df = pd.DataFrame(iris_data.json())

# TODO: try to predict a flower using post_api_endpoint and
# write out the result in streamlit



def layout():
    st.markdown("# Classify your iris flower")

    with st.form("iris_data"):
        sepal_length = st.number_input(
            "Sepal length (cm)", min_value=4.01, max_value=8.49, value=6.0, step=0.1
        )
        sepal_width = st.number_input(
            "Sepal width (cm)", min_value=1.81, max_value=4.99, value=2.5, step=0.1
        )
        petal_length = st.number_input(
            "Petal length (cm)", min_value=0.81, max_value=7.49, value=4.5, step=0.1
        )
        petal_width = st.number_input(
            "Petal width (cm)", min_value=0.01, max_value=2.99, value=1.2, step=0.1
        )

        submitted = st.form_submit_button("PREDICT FLOWER")

    if submitted:
        payload = {
            "SepalLengthCm": sepal_length,
            "SepalWidthCm": sepal_width,
            "PetalLengthCm": petal_length,
            "PetalWidthCm": petal_width,
        }

        response = post_api_endpoint(payload, endpoint="/api/predict")
        predicted_flower = response.json().get("predicted_flower")


        st.markdown(f"Predicted flower: {predicted_flower}")
        st.image(f"{ASSETS_PATH / predicted_flower}.jpg")

    print(f"{sepal_length = }")
    print(f"{submitted = }")

    st.markdown("## Raw data")
    st.dataframe(df)


if __name__ == "__main__":
    layout()
