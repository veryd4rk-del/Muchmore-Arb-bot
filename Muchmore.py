import streamlit as st
import pandas as pd
from prediction_bot import fetch_polymarket_markets, fetch_kalshi_markets, find_arbitrage_opps

st.set_page_config(
    page_title="MuchMore Arb",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🚀 MuchMore Arbitrage")
st.markdown("**Polymarket + Kalshi** — Real-time $2+ synthetic arbitrage scanner")

col1, col2 = st.columns([1, 4])
with col1:
    if st.button("🔄 Refresh & Scan", type="primary", use_container_width=True):
        with st.spinner("Fetching live markets from both platforms..."):
            poly = fetch_polymarket_markets(100)
            kalshi = fetch_kalshi_markets(100)
            
            st.subheader(f"📈 Polymarket: {len(poly)} markets")
            st.subheader(f"📈 Kalshi: {len(kalshi)} markets")
            
            opps = find_arbitrage_opps(poly, kalshi, min_profit_per_dollar=0.015)
            
            if opps:
                st.success(f"🎯 Found {len(opps)} opportunities with **$2+** potential!")
                df = pd.DataFrame(opps)
                st.dataframe(df, use_container_width=True, height=500)
                
                for opp in opps[:8]:
                    with st.expander(f"💰 ~${opp['est_profit_on_100']} on $100 | Similarity: {opp['similarity']}"):
                        st.write(f"**Polymarket**: {opp['poly_yes']} — {opp['poly_q']}")
                        st.write(f"**Kalshi**: {opp['kal_yes']} — {opp['kal_q']}")
            else:
                st.info("No strong $2+ opportunities right now.")

st.caption("📱 **iPhone Tip**: Open in Safari → Share → 'Add to Home Screen' for app-like experience")
st.caption("⚠️ Monitoring / Dry-run only • Always verify events manually before trading")
