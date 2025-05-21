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

- **API Key Security:** I accidentally pushed my `.env` file with API credentials in an early commit. I resolved it by updating `.gitignore`, removing sensitive data from history, and pushing a clean version.

- **Data Normalization:** The audio features returned by the API had varying scales. I normalized and selected only the most relevant metrics to ensure accurate comparisons across different tracks and artists.

- **Visualization:** Choosing the right type of chart to represent the data was challenging. I experimented with several chart types before settling on interactive bar charts using Altair for clarity and user engagement.

- **Streamlit UI Design:** Keeping the dashboard clean and easy to use while still delivering insights required UI tweaks. I focused on simplicity and tested usability for smooth artist comparisons.


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

