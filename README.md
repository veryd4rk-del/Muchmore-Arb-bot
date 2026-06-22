# MuchMore Arbitrage Bot

Polymarket + Kalshi prediction market arbitrage scanner.

## Features
- Live market data from both platforms
- Synthetic arbitrage detection (YES on one + NO on the other)
- Filters for **$2+ estimated profit** opportunities
- Beautiful mobile-friendly Streamlit web app
- Easy to install on iPhone as a PWA

## Quick Deploy to Streamlit Cloud
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → Deploy `muchmore.py`

## Local Run
```bash
pip install -r requirements.txt
streamlit run muchmore.py
