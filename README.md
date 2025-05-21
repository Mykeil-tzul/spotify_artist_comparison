# 🎧 Spotify Artist Comparison Dashboard

A clean, interactive Streamlit app that compares the **top tracks** of Kendrick Lamar, Drake, and J. Cole using the **Spotify API**. Built from scratch using Python, this project shows off **API integration**, **data transformation**, and **data visualization** in one polished experience.

🌐 **Live Demo**: [spotifyartistcomparison-bymt.streamlit.app](https://spotifyartistcomparison-bymt.streamlit.app/)

---

## 📊 What It Does

- 🔍 Pulls top 10 tracks for each artist via Spotify API
- 📈 Tracks include **popularity scores** (0–100) using Spotify’s internal algorithm
- 💾 Saves a clean CSV (`artist_comparison.csv`) for future analysis
- 📊 Visualizes track popularity in an interactive Streamlit dashboard

---

## 💡 What is Spotify Popularity?

> **Popularity** is a score from **0 to 100** based on a track’s:
> - Total streams
> - Recency
> - Ongoing listener engagement

Higher scores = more streams or trending tracks on Spotify.

---

## ⚙️ Tech Stack

- **Python** 🐍
- `spotipy` – Spotify Web API wrapper
- `pandas` – Data loading and manipulation
- `Streamlit` – Web dashboard UI
- `Altair` – Interactive charts

---

## 🧠 Why This Project Matters

- 🚀 Real-world **ETL flow**: extract data, transform it, load it into a dashboard
- 🎨 Showcases **frontend + backend** with Python only
- 📁 Great for **portfolio** to stand out to recruiters and tech teams

---

## 🧠 Challenges Faced

- **API Authentication:** Initially, I struggled with setting up Spotify's OAuth flow. After consulting the documentation and community forums, I successfully implemented the Client Credentials Flow.

- **Data Normalization:** The audio features returned by the API had varying scales. I normalized the data to ensure accurate comparisons across different metrics.

- **Visualization:** Choosing the right type of chart to represent the data was challenging. I experimented with various chart types before settling on interactive bar charts for clarity.

---

## 🚀 How to Run It

```bash
# 1. Clone this repo
git clone https://github.com/Mykeil-tzul/spotify_artist_comparison.git
cd spotify_artist_comparison

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file with:
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret

# 5. Run the app
streamlit run dashboard.py


---

🔒 This project securely loads credentials using a `.env` file, which is never tracked by Git.

---

## 📁 Folder Structure

spotify_artist_comparison/
│
├── fetch_artist_data.py # ETL script to pull and save top tracks
├── dashboard.py # Streamlit UI
├── artist_comparison.csv # Cleaned output data
├── .env # Spotify credentials (not pushed)
├── requirements.txt # Project dependencies
└── README.md # This file

---

## 💼 Author

Built with 🔥 by [@Mykeil-tzul](https://github.com/Mykeil-tzul) — **data engineer in the making & former hooper blending tech + music + data**.  

