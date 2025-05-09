import streamlit as st
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

engine = create_engine("sqlite:///daily_log.db")

st.title("📝 Ежедневный опрос")

with st.form("daily_form"):
    date = st.date_input("Дата", datetime.today())
    mood = st.slider("Настроение", 0, 10, 5)
    energy = st.slider("Энергия", 0, 10, 5)
    wish_to_die = st.slider("Желание умереть", 0, 10, 5)
    notes = st.text_area("Комментарии")

    submitted = st.form_submit_button("Отправить")

    if submitted:
        df = pd.DataFrame([{
            "date": date,
            "mood": mood,
            "energy": energy,
            "wish_to_die": wish_to_die,
            "notes": notes,
            "timestamp": datetime.now()
        }])
        df.to_sql("daily_log", con=engine, if_exists="append", index=False)
        st.success("Ответ сохранён ✅")
