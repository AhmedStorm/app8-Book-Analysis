import streamlit as st
from glob import glob
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

filepaths = sorted([x for x in glob('diary/*.txt')])
dates = [os.path.basename(x).split(".txt")[0] for x in filepaths]
analyzer = SentimentIntensityAnalyzer()
positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
        scores = analyzer.polarity_scores(content)
        positivity.append(scores["pos"])
        negativity.append(scores["neg"])

st.header("Tone Diary")
st.subheader("Positivity")
pos_plot = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(pos_plot)
st.subheader("Negativity")
neg_plot = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(neg_plot)
