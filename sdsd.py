import streamlit as st
import pandas as pd
import time as ts
from datetime import time
import plotly.express as px

st.set_page_config(page_title="Interactive Data Science Dashboard", layout="wide")

# Sidebar Navigation
st.sidebar.title("🔀 Navigation")
page = st.sidebar.radio("Go to", ["Login", "Timer", "Dashboard","chat"])

# -------------------- LOGIN PAGE --------------------
if page == "Login":
    st.title("🔐 Login Page")
    st.image(r"C:\Users\kodat\Downloads\dashboard.jpg", width=300, caption="Welcome!")
    user_id = st.text_input("Enter ID")
    password = st.text_input("Enter Password", type="password")
    if user_id and password:
        st.success(f"Welcome, {user_id}!")
    else:
        st.info("Please enter both ID and password to proceed.")

# -------------------- TIMER PAGE --------------------
elif page == "Timer":
    st.title("⏱ Countdown Timer")

    val = st.time_input("Set Timer", value=time(0, 0, 0))

    def converter(value):
        m, s, ms = value.split(":")
        t_s = int(m) * 60 + int(s) + int(ms) / 1000
        return t_s

    if str(val) != "00:00:00":
        sec = converter(str(val))
        bar = st.progress(0)
        per = sec / 100
        pro_status = st.empty()
        for i in range(100):
            bar.progress(i + 1)
            pro_status.write(f"{i + 1}%")
            ts.sleep(per)
    else:
        st.warning("⚠️ Please set the timer.")

# -------------------- DASHBOARD PAGE --------------------
elif page == "Dashboard":
    st.title("📊 Data Science Dashboard")

    st.subheader("📂 Upload a CSV File")
    file = st.file_uploader("Choose a CSV file", type=["csv"])

    if file:
        df = pd.read_csv(file)
        st.success("✅ File Uploaded Successfully")

        st.subheader("📑 Raw Data")
        st.dataframe(df, use_container_width=True)

        # Chart options
        st.subheader("📈 Data Visualization")
        columns = df.select_dtypes(include=["number"]).columns.tolist()
        if len(columns) >= 2:
            x_axis = st.selectbox("X-Axis", options=columns)
            y_axis = st.selectbox("Y-Axis", options=columns, index=1)
            chart_type = st.radio("Chart Type", ["Bar", "Scatter", "Line", "Polar"])

            if chart_type == "Bar":
                fig = px.bar(df, x=x_axis, y=y_axis, color=x_axis)
            elif chart_type == "Scatter":
                fig = px.scatter(df, x=x_axis, y=y_axis, color=x_axis)
            elif chart_type == "Line":
                fig = px.line(df, x=x_axis, y=y_axis, color=x_axis)
            elif chart_type == "Polar":
                fig = px.bar_polar(df, r=y_axis, theta=x_axis, color=x_axis)

            st.plotly_chart(fig, use_container_width=True)

        # Gender filter
        if "gender" in df.columns:
            st.subheader("🚻 Gender Filter")
            gen = df["gender"].dropna().unique()
            selected_gender = st.selectbox("Select Gender", gen)
            if selected_gender:
                df_filtered = df[df["gender"] == selected_gender]
                st.write(f"Filtered Data for **{selected_gender}**:")
                st.dataframe(df_filtered)

    # Static Table
    st.subheader("📋 Sample Table")
    sample_df = pd.DataFrame({"col 1": [1, 2, 3], "col 2": [10, 20, 30]})
    col1, col2 = st.columns(2)
    with col1:
        st.table(sample_df)
    with col2:
        st.dataframe(sample_df)
elif page == "chat":
    st.markdown(
        """
<iframe class="chatbot-popup"
        src="https://www.chatbase.co/chatbot-iframe/AbakbSSL2ccqZllt_3WHO"
        allow="microphone;"
        frameborder="0"
        width="100%"
        height="500">
</iframe>
        """,
        unsafe_allow_html=True
    )