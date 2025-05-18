# 🎧 Spotify Artist Comparison Dashboard

This project compares the **top tracks and popularity** of artists like **Kendrick Lamar**, **Drake**, and **J. Cole** using Spotify’s API — all visualized in a clean, interactive Streamlit app.

---

## 📊 What It Does

- 🔍 Pulls top tracks for each artist using `spotipy`
- 🎯 Tracks include popularity scores (0–100) based on Spotify’s internal algorithm
- 📁 Saves clean data to `artist_comparison.csv`
- 📈 Visualizes track popularity in a web-based dashboard

---

## 💡 What is Popularity?

> Spotify’s **popularity score** is a value from **0–100** that reflects a track’s streaming numbers and recency. A higher score means the track is trending or heavily streamed.

---

## 📂 Tech Stack

- **Python** 🐍
- **Spotipy** for Spotify API calls
- **Streamlit** for dashboard UI
- **Pandas** for data handling
- **Altair** for interactive charts

---

## 🧠 Why This Project Matters

This project is a perfect blend of:

- 💼 **Real-world API work** (Spotify API)
- 🎨 **Frontend dashboard** (Streamlit + Altair)
- 📦 **Data engineering flow** (ETL: Extract, Transform, Load)

It’s simple but powerful — perfect for showing off full data flow and frontend skills to recruiters.

---

## 🚀 How to Run It

```bash
# Install dependencies
pip install -r requirements.txt

# Load Spotify credentials in .env

# Run the dashboard
streamlit run dashboard.py

