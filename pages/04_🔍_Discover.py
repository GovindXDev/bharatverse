import streamlit as st
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from streamlit_app.search_module import search_page
from streamlit_app.utils.main_styling import load_custom_css


def main():
    st.set_page_config(
        page_title="Discover - BharatVerse",
        page_icon="🔍",
        layout="wide"
    )
    load_custom_css()
    search_page()


if __name__ == "__main__":
    main()
