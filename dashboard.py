import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh
from st_aggrid import AgGrid, GridOptionsBuilder

# รีเฟรชอัตโนมัติทุก 5 นาที (300,000 ms)
st_autorefresh(interval=300000, key="data_refresh")

# ตั้งค่า UI
st.set_page_config(page_title="Shopee ROAS Dashboard", layout="wide")
st.title("📊 Shopee ROAS รายชั่วโมง")

# แสดงเวลาล่าสุด (เวลาไทย)
th_time = datetime.utcnow() + timedelta(hours=7)
st.caption(f"🕒 อัปเดตล่าสุด: {th_time.strftime('%Y-%m-%d %H:%M:%S')} (เวลาประเทศไทย)")

# ลิงก์ Google Sheets (.xlsx format)
#EXCEL_URL = "https://docs.google.com/spreadsheets/d/1Db2MuqmITPNI11ujFpJeJCDhDeY0aqA3/export?format=xlsx"
EXCEL_URL = "https://docs.google.com/spreadsheets/d/1dQcv31UYWHoiDquNT2-vKROyvSww_k59/export?format=xlsx"

# โหลดและแสดงข้อมูล
try:
    df = pd.read_excel(EXCEL_URL)

    # กำหนด Grid Options
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(resizable=True, filter=True, sortable=True)
    gb.configure_grid_options(domLayout='normal')

    # ตรึงคอลัมน์ (คอลัมน์แรกด้านซ้าย)
    first_col = df.columns[0]
    gb.configure_column(first_col, pinned='left')

    grid_options = gb.build()

    # แสดงตาราง
    AgGrid(df, gridOptions=grid_options, height=800, theme="balham")

except Exception as e:
    st.error(f"ไม่สามารถโหลดข้อมูลได้: {e}")

