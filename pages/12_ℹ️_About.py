import streamlit as st
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from streamlit_app.utils.main_styling import load_custom_css


def main():
    st.set_page_config(
        page_title="About - BharatVerse",
        page_icon="ℹ️",
        layout="wide"
    )
    load_custom_css()

    # Header
    st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='color: #FF6B35; font-size: 3rem; margin-bottom: 0.5rem;'>🇮🇳 About BharatVerse</h1>
        <h2 style='color: #2E86AB; font-size: 1.5rem; margin-bottom: 1rem;'>Preserving India's Cultural Heritage Digitally</h2>
    </div>
    """, unsafe_allow_html=True)

    # Mission
    st.markdown("## 🎯 Our Mission")
    st.markdown("""
    BharatVerse is dedicated to preserving, documenting, and celebrating the rich cultural heritage of India
    through innovative digital technologies. We believe that every story, song, tradition, and cultural practice
    deserves to be preserved for future generations.

    Our platform empowers individuals and communities to become cultural custodians, contributing to a
    comprehensive digital archive that represents the incredible diversity of Indian culture.
    """)

    # Vision
    st.markdown("## 🌟 Our Vision")
    st.markdown("""
    To create the world's most comprehensive digital repository of Indian cultural heritage, where:
    - Every regional tradition finds its voice
    - Cultural knowledge is accessible to all
    - Communities actively participate in preservation efforts
    - Technology serves as a bridge between past and future
    - Cultural diversity is celebrated and protected
    """)

    # Key features
    st.markdown("## ✨ Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📚 Story Documentation
        - Rich text editor with multimedia support
        - Multi-language content creation
        - Cultural context preservation
        - Community storytelling platform

        ### 🖼️ Visual Archive
        - Image upload and management
        - AI-powered cultural recognition
        - Historical context documentation
        - Visual storytelling tools

        ### 🎵 Audio Heritage
        - High-quality audio recording capabilities
        - Automatic transcription and translation
        - Metadata tagging and categorization
        - Regional dialect preservation
        """)

    with col2:
        st.markdown("""
        ### 🔍 Smart Discovery
        - Advanced search and filtering
        - Content recommendation engine
        - Cultural pattern recognition
        - Cross-referencing capabilities

        ### 🤝 Community Collaboration
        - Expert validation networks
        - Collaborative projects
        - Knowledge sharing forums
        - Cultural exchange programs

        ### 🤖 AI-Powered Insights
        - Content analysis and categorization
        - Cultural trend identification
        - Sentiment analysis
        - Automated quality assessment
        """)

    # Technology stack
    st.markdown("## 🛠️ Technology Stack")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **Frontend & UI**
        - Streamlit for web interface
        - Responsive design
        - Interactive visualizations
        - Real-time updates
        """)

    with col2:
        st.markdown("""
        **Backend & API**
        - FastAPI for REST services
        - PostgreSQL database
        - Redis for caching
        - Docker containerization
        """)

    with col3:
        st.markdown("""
        **AI & ML**
        - Natural Language Processing
        - Computer Vision
        - Audio processing
        - Machine Learning models
        """)

    # Impact
    st.markdown("## 📈 Our Impact")

    actual_stories = len(st.session_state.get('contributions', []))

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Cultural Items", f"{2547 + actual_stories:,}", "Growing daily")
    with col2:
        st.metric("Languages Covered", "28", "Expanding")
    with col3:
        st.metric("Regions Documented", "36", "Nationwide")
    with col4:
        st.metric("Community Members", "1,234", "Join us!")

    # Team
    st.markdown("## 👥 Our Team")
    st.markdown("""
    BharatVerse is built by a passionate team of technologists, cultural enthusiasts, and preservation experts
    who believe in the power of technology to preserve and celebrate cultural heritage.

    **Core Values:**
    - **Authenticity**: Ensuring cultural accuracy and respect
    - **Inclusivity**: Representing all communities and traditions
    - **Innovation**: Using cutting-edge technology for preservation
    - **Community**: Building bridges between cultures and generations
    - **Accessibility**: Making cultural knowledge available to everyone
    """)

    # Get involved
    st.markdown("## 🚀 Get Involved")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🤝 For Contributors
        - Share your cultural knowledge
        - Document family traditions
        - Record regional stories and songs
        - Upload historical photographs
        - Participate in community projects
        """)

    with col2:
        st.markdown("""
        ### 👨‍🏫 For Experts
        - Validate cultural content
        - Provide historical context
        - Lead preservation projects
        - Mentor community members
        - Contribute specialized knowledge
        """)

    # Contact
    st.markdown("## 📞 Contact Us")
    st.markdown("""
    We'd love to hear from you! Whether you have questions, suggestions, or want to collaborate:

    - **Email**: contact@bharatverse.org
    - **Community Forum**: Join our discussions
    - **Social Media**: Follow us for updates
    - **GitHub**: Contribute to our open-source projects
    """)

    # CTA
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #FF6B35, #2E86AB); border-radius: 15px; color: white;'>
        <h2 style='margin-bottom: 1rem;'>Start Your Cultural Journey Today</h2>
        <p style='font-size: 1.1rem; margin-bottom: 1.5rem;'>
            Every contribution matters. Every story counts. Every tradition deserves preservation.
        </p>
        <p style='font-size: 1rem; opacity: 0.9;'>
            Join thousands of cultural custodians in preserving India's incredible heritage for future generations.
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
