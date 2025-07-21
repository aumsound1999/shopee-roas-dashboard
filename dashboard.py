import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# รีเฟรชอัตโนมัติทุก 5 นาที (300,000 ms)
st_autorefresh(interval=300000, key="data_refresh")

# ตั้งค่า UI
st.set_page_config(page_title="Shopee ROAS Dashboard", layout="wide")
st.title("📊 Shopee ROAS รายชั่วโมง")
th_time = datetime.utcnow() + timedelta(hours=7)
st.caption(f"อัปเดตล่าสุด: {th_time.strftime('%Y-%m-%d %H:%M:%S')} (เวลาประเทศไทย)")


# ลิงก์ Google Sheets (.xlsx format)
EXCEL_URL = "https://docs.google.com/spreadsheets/d/1Db2MuqmlTPNl11ujFpIeJCDhDeY0aqA3/export?format=xlsx"

try:
    df = pd.read_excel(EXCEL_URL)
    #st.dataframe(df, use_container_width=True)
    st.dataframe(df, height=1000, use_container_width=True)
except Exception as e:
    st.error(f"ไม่สามารถโหลดข้อมูลได้: {e}")
    
