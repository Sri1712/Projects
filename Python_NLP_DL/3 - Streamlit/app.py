import streamlit as st
import pandas as pd
import numpy as np

## Title
st.title("Hello Streamlit")

#Display a text
st.write("Display a simple text")

#create a dataframe
df = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10)
})

#Display the dataframe
st.dataframe(df)

#Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)