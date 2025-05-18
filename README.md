# 🎧 Spotify Artist Comparison Dashboard

An interactive data app that compares the **top tracks** of three music legends — **Kendrick Lamar, Drake, and J. Cole** — using real Spotify data. This project blends API engineering, data transformation, and front-end visualization into one clean experience.

👉 **Live Demo:**  
📊 [Streamlit Dashboard (Kendrick vs Drake vs J. Cole)](https://spotifyartistcomparison-bymt.streamlit.app/)

---

## 📊 What It Does

- 🔍 **Pulls top tracks** for each artist using the official Spotify API (via Spotipy)
- 💯 **Grabs Spotify popularity scores** (0–100) for each track
- 💾 **Saves clean data** into a `artist_comparison.csv` file
- 📈 **Visualizes track popularity** in a responsive Streamlit dashboard

---

## 💡 What Is Spotify "Popularity"?

Spotify assigns each track a **popularity score** from 0 to 100 based on:
- 📈 **Recent streaming volume**
- ⏱️ **Recency of plays**
- 🔁 **Overall listener engagement**

> A track with a score of 95+ means it’s heavily streamed and actively trending.

---

## 📂 Tech Stack

| Layer         | Tool/Library                 |
|--------------|------------------------------|
| 🎧 Data Source | [Spotify Web API](https://developer.spotify.com/documentation/web-api) |
| 🐍 Backend     | Python, Spotipy              |
| 🧮 Data Wrangling | Pandas                    |
| 📊 Visualization | Altair, Streamlit         |
| 🔄 Output File | CSV (for easy portability)  |

---

## 🧠 Why This Project Matters

This is more than just a playlist viewer. It's a **mini end-to-end data pipeline**:

✅ **Real-World APIs** (Spotify)  
✅ **ETL Flow** — Fetch, clean, save  
✅ **Data Viz for Storytelling**  
✅ **Frontend Skills** — Streamlit layout & interactivity

> Perfect for data roles in media, entertainment, or any team that loves storytelling with data.

---

## 🚀 How To Run It Locally

```bash
# 1. Clone the repo
git clone https://github.com/Mykeil-tzul/spotify_artist_comparison.git
cd spotify_artist_comparison

# 2. Create your .env file with Spotify API credentials
SPOTIPY_CLIENT_ID=your_id_here  
SPOTIPY_CLIENT_SECRET=your_secret_here  

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run dashboard.py
