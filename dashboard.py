import streamlit as st
import pandas as pd
from datetime import datetime

# ตั้งค่าหน้า Dashboard
st.set_page_config(page_title="Shopee ROAS Dashboard", layout="wide")

# หัวข้อหน้า
st.title("📊 Shopee ROAS รายชั่วโมง")
st.caption(f"อัปเดตล่าสุด: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# ลิงก์ Google Sheets -> CSV
CSV_URL = "https://docs.google.com/spreadsheets/d/1Db2MuqmlTPNl11ujFpIeJCDhDeY0aqA3/export?format=csv&gid=1352923982"

# โหลดข้อมูลจาก Google Sheets
try:
    df = pd.read_csv(CSV_URL)
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"ไม่สามารถโหลดข้อมูลได้: {e}")
