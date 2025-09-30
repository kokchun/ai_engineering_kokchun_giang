import streamlit as st
from helpers import read_api_endpoint, post_api_endpoint
import pandas as pd

iris_data = read_api_endpoint("/api")
df = pd.DataFrame(iris_data.json())


def layout():
    st.markdown("# Classify your iris flower")

    with st.form("iris_data"):
        sepal_length = st.number_input(
            "Sepal length (cm)", min_value=4.01, max_value=8.49, value=6.0
        )

        submitted = st.form_submit_button("PREDICT FLOWER")

    print(f"{sepal_length = }")
    print(f"{submitted = }")

    st.markdown("## Raw data")
    st.dataframe(df)


if __name__ == "__main__":
    layout()
