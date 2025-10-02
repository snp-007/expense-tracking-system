import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab

def show_footer():
    copyright_text = "© 2025 SNP. All rights reserved."
    footer_html = f"""
    <style>
    .footer {{
        position: fixed;
        right: 10px;
        bottom: 10px;
        font-size: 12px;
        color: #888;
        opacity: 0.7;
        z-index: 100;
    }}
    </style>
    <div class="footer">{copyright_text}</div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

st.title("Track Your Expenses")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()

show_footer()