import streamlit as st
import pandas as pd


def layout():
    st.markdown("# Really cool streamlit app")

    data = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [1, 4, 2, 5, 3]})

    st.line_chart(data.set_index("x"))


if __name__ == "__main__":
    print("hej från docker")
    layout()
