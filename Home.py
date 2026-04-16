import streamlit as st
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from core.service_manager import get_service_manager
from core.error_handler import error_boundary, safe_import


def main():
    """Main application function"""
    st.set_page_config(
        page_title="BharatVerse - Cultural Heritage Platform",
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Initialize service manager
    get_service_manager()

    # Apply styling
    with error_boundary("Failed to load styling", show_error=False):
        styling_module = safe_import("streamlit_app.utils.main_styling")
        if styling_module:
            styling_module.load_custom_css()

    # Modern gradient header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute; top: -50%; left: -20%; width: 60%; height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            border-radius: 50%;
        "></div>
        <h1 style="
            color: white;
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            position: relative;
        ">
            🏛️ BharatVerse
        </h1>
        <h2 style="
            color: rgba(255,255,255,0.95);
            font-size: 1.5rem;
            font-weight: 300;
            margin-bottom: 0;
            position: relative;
        ">
            Preserving India's Cultural Heritage
        </h2>
        <p style="
            color: rgba(255,255,255,0.8);
            font-size: 1rem;
            margin-top: 0.5rem;
            position: relative;
        ">
            Preserving the past, enriching the future — One story at a time
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Welcome card with glassmorphism effect
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
    ">
        <h3 style="
            color: #1a1a2e;
            margin-bottom: 1rem;
            font-size: 2rem;
            font-weight: 600;
        ">Welcome to Your Cultural Journey! 🎉</h3>
        <p style="
            font-size: 1.15rem;
            color: #16213e;
            line-height: 1.8;
            margin-bottom: 1rem;
        ">
            Join a growing community dedicated to preserving India's rich cultural tapestry.
        </p>
        <p style="
            font-size: 1rem;
            color: #0f3460;
            line-height: 1.6;
        ">
            📚 Document stories • 🔍 Discover heritage • 🤝 Connect with enthusiasts
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Modern feature cards
    st.markdown("<h3 style='text-align: center; color: #1a1a2e; margin: 2rem 0;'>✨ Core Features</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
            transition: transform 0.3s;
        ">
            <h4 style="color: white; margin-bottom: 1rem; font-size: 1.3rem;">📝 Text Stories</h4>
            <p style="color: rgba(255,255,255,0.9); font-size: 0.95rem; line-height: 1.5;">
                Document traditions, folklore, recipes, and wisdom passed through generations
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 2rem;
            border-radius: 15px;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 10px 20px rgba(245, 87, 108, 0.3);
        ">
            <h4 style="color: white; margin-bottom: 1rem; font-size: 1.3rem;">🤝 Community Hub</h4>
            <p style="color: rgba(255,255,255,0.9); font-size: 0.95rem; line-height: 1.5;">
                Connect, collaborate, and participate in cultural preservation initiatives
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
            padding: 2rem;
            border-radius: 15px;
            height: 200px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 10px 20px rgba(250, 112, 154, 0.3);
        ">
            <h4 style="color: white; margin-bottom: 1rem; font-size: 1.3rem;">🔍 Discover</h4>
            <p style="color: rgba(255,255,255,0.9); font-size: 0.95rem; line-height: 1.5;">
                Explore rich cultural content from diverse regions and communities
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation buttons
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1a1a2e;'>🚀 Get Started</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📝 Write Story", use_container_width=True, type="primary"):
            st.switch_page("pages/02_📝_Text_Stories.py")
    with col2:
        if st.button("🤝 Join Community", use_container_width=True, type="primary"):
            st.switch_page("pages/06_🤝_Community.py")
    with col3:
        if st.button("🔍 Explore", use_container_width=True, type="primary"):
            st.switch_page("pages/04_🔍_Discover.py")

    # Stats section
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #1a1a2e; margin-bottom: 2rem;'>📊 Our Growing Impact</h3>", unsafe_allow_html=True)

    # Include actual session contributions
    actual_stories = len(st.session_state.get('contributions', []))
    total_stories = 2547 + actual_stories

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style="
            text-align: center; padding: 1.5rem;
            background: white; border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        ">
            <h2 style="color: #667eea; margin: 0;">{total_stories:,}</h2>
            <p style="color: #666; margin: 0.5rem 0 0 0;">Cultural Stories</p>
            <small style="color: #4caf50;">↑ 127 this week</small>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="
            text-align: center; padding: 1.5rem;
            background: white; border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        ">
            <h2 style="color: #f093fb; margin: 0;">1,234</h2>
            <p style="color: #666; margin: 0.5rem 0 0 0;">Active Users</p>
            <small style="color: #4caf50;">↑ 89 today</small>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="
            text-align: center; padding: 1.5rem;
            background: white; border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        ">
            <h2 style="color: #fa709a; margin: 0;">456</h2>
            <p style="color: #666; margin: 0.5rem 0 0 0;">Heritage Sites</p>
            <small style="color: #4caf50;">↑ 23 this month</small>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div style="
            text-align: center; padding: 1.5rem;
            background: white; border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        ">
            <h2 style="color: #fee140; margin: 0;">28</h2>
            <p style="color: #666; margin: 0.5rem 0 0 0;">Languages</p>
            <small style="color: #4caf50;">↑ 2 added</small>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #666;">
        <p>🏛️ <strong>BharatVerse</strong> - Preserving India's Cultural Heritage for Future Generations</p>
        <p style="font-size: 0.9rem;">Made with ❤️ for cultural preservation</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

