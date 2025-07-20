import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Shopee ROAS Dashboard", layout="wide")

st.title("📊 Shopee ROAS รายชั่วโมง")
st.caption(fอัปเดตล่าสุด {datetime.now().strftime('%Y-%m-%d %H%M%S')})

EXCEL_FILE = sale_roai.xlsx

if os.path.exists(EXCEL_FILE)
    df = pd.read_excel(EXCEL_FILE)
    st.dataframe(df, use_container_width=True)
else
    st.warning(fไม่พบไฟล์ `{EXCEL_FILE}` ในโฟลเดอร์ปัจจุบัน)
