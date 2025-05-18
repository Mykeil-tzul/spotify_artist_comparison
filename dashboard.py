import pandas as pd
import streamlit as st
import altair as alt

# Load CSV
df = pd.read_csv("artist_comparison.csv")

# Title
st.title("🎧 Artist Track Popularity Dashboard")

# Dropdown to select artist
artist = st.selectbox("Choose an Artist", df["artist"].unique())

# Filter data
filtered = df[df["artist"] == artist]

# Show top tracks
st.write(f"🎵 Top Tracks for {artist}")
st.dataframe(filtered[["track", "popularity"]])

# Bar chart
chart = alt.Chart(filtered).mark_bar().encode(
    x='track',
    y=alt.Y('popularity', title='Popularity'),
    tooltip=['track', 'popularity']
).properties(
    title=f"{artist} Track Popularity",
    width=700
)

st.altair_chart(chart)