import pandas as pd 
import streamlit as st 
import plotly.express as px 
import seaborn as sns
import numpy as np 

st.title ("DEFENCE ANALYSIS")
#import csv file
df = pd.read_csv("defending.csv")

st.markdown("## Overview")
st.markdown("### First Ten Observation")
st.write(df.head(10))

st.markdown("Last Ten Observation")
st.write(df.tail(10))

st.markdown("### Description of Numeric Data Types")
st.write(df.describe())

st.markdown("### Summary  of Table")
st.write(df.shape)

st.markdown("##Univariate Analysis")

st.markdown("Clubs")
st.write(df["club"].describe())

st.markdown("Position")
st.write(df["position"].describe())

st.markdown("Players")
st.write(df["player_name"].describe())

st.markdown("Match Played")
st.write(df["match_played"].describe())

st.markdown("Total Won")
st.write(df["t_won"].describe())

st.markdown("Total Lost")
st.write(df["t_lost"].describe())
 
st.markdown("Bar Chart Representation")
goals = px.bar(df["player_name"], y = "player_name", title = "Total goals lost")
st.plotly_chart(goals, use_container_width = True)

st.markdown("Bivariate Analysis")
 
st.markdown("### Club Vs Total Match Played")
goals2 = px.bar(df["player_name"], x = "match_played", y = "t_won", title = "Distribution of Players vs Match played")
st.plotly_chart(goals2, use_container_width = True )
