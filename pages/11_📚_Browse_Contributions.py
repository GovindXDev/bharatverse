import streamlit as st
import sys
from pathlib import Path
from datetime import datetime

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from streamlit_app.utils.main_styling import load_custom_css


def main():
    st.set_page_config(
        page_title="Browse Contributions - BharatVerse",
        page_icon="📚",
        layout="wide"
    )
    load_custom_css()

    # Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    ">
        <h1 style="color: white; margin: 0;">📚 Browse Contributions</h1>
        <p style="color: rgba(255,255,255,0.9); margin-top: 0.5rem;">
            Explore all cultural content contributed by the community
        </p>
    </div>
    """, unsafe_allow_html=True)

    contributions = st.session_state.get('contributions', [])

    if not contributions:
        st.info("🔍 No contributions yet! Be the first to share your cultural story.")
        st.markdown("### How to contribute:")
        st.markdown("1. Go to **📝 Text Stories** from the sidebar")
        st.markdown("2. Fill in your story details")
        st.markdown("3. Submit your contribution")
        st.markdown("4. Come back here to see all contributions!")

        if st.button("📝 Go to Text Stories", type="primary"):
            st.switch_page("pages/02_📝_Text_Stories.py")
        return

    # Stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Contributions", len(contributions))
    with col2:
        languages = set([c.get('language', 'Unknown') for c in contributions])
        st.metric("Languages", len(languages))
    with col3:
        story_types = set([c.get('story_type', 'Unknown') for c in contributions])
        st.metric("Story Types", len(story_types))
    with col4:
        regions = set([c.get('region', 'Unknown') for c in contributions if c.get('region')])
        st.metric("Regions", len(regions))

    st.markdown("---")

    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        filter_language = st.selectbox(
            "Filter by Language",
            ["All"] + sorted(list(set([c.get('language', 'Unknown') for c in contributions])))
        )
    with col2:
        filter_type = st.selectbox(
            "Filter by Type",
            ["All"] + sorted(list(set([c.get('story_type', 'Unknown') for c in contributions])))
        )
    with col3:
        sort_order = st.selectbox("Sort by", ["Newest First", "Oldest First", "Title A-Z", "Title Z-A"])

    # Apply filters
    filtered = contributions.copy()
    if filter_language != "All":
        filtered = [c for c in filtered if c.get('language') == filter_language]
    if filter_type != "All":
        filtered = [c for c in filtered if c.get('story_type') == filter_type]

    # Apply sorting
    if sort_order == "Newest First":
        filtered = sorted(filtered, key=lambda x: x.get('created_at', ''), reverse=True)
    elif sort_order == "Oldest First":
        filtered = sorted(filtered, key=lambda x: x.get('created_at', ''))
    elif sort_order == "Title A-Z":
        filtered = sorted(filtered, key=lambda x: x.get('title', '').lower())
    elif sort_order == "Title Z-A":
        filtered = sorted(filtered, key=lambda x: x.get('title', '').lower(), reverse=True)

    st.markdown(f"### Showing {len(filtered)} of {len(contributions)} contributions")

    # Display contributions
    for i, contrib in enumerate(filtered):
        with st.container():
            col1, col2 = st.columns([1, 4])

            with col1:
                type_icons = {
                    "Folk Tale": "📖", "Proverb": "💬", "Recipe": "🍳",
                    "Song": "🎵", "Poem": "📜", "Historical Account": "🏛️",
                    "Personal Story": "👤", "Other": "📄"
                }
                icon = type_icons.get(contrib.get('story_type', ''), '📄')
                st.markdown(f"""
                <div style='background: linear-gradient(135deg, #667eea, #764ba2); padding: 1.5rem; border-radius: 10px; text-align: center; color: white;'>
                    <h1 style="margin: 0;">{icon}</h1>
                    <small>{contrib.get('story_type', 'Unknown')}</small>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"### {contrib.get('title', 'Untitled')}")

                c1, c2, c3, c4 = st.columns(4)
                with c1:
                    st.markdown(f"**Language:** {contrib.get('language', 'N/A')}")
                with c2:
                    st.markdown(f"**Author:** {contrib.get('author', 'Anonymous')}")
                with c3:
                    st.markdown(f"**Region:** {contrib.get('region', 'N/A')}")
                with c4:
                    created = contrib.get('created_at', '')
                    if created:
                        try:
                            dt = datetime.fromisoformat(created)
                            st.markdown(f"**Date:** {dt.strftime('%b %d, %Y')}")
                        except Exception:
                            st.markdown(f"**Date:** Recent")

                # Content preview
                content = contrib.get('content', '')
                if len(content) > 300:
                    st.markdown(content[:300] + "...")
                else:
                    st.markdown(content)

                # Tags
                keywords = contrib.get('keywords', '')
                if keywords:
                    tags = [t.strip() for t in keywords.split(',')]
                    tags_html = " ".join([
                        f"<span style='background: #e1f5fe; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; margin: 2px;'>{tag}</span>"
                        for tag in tags
                    ])
                    st.markdown(f"**Tags:** {tags_html}", unsafe_allow_html=True)

            # View full content
            with st.expander(f"📋 View Full Content - {contrib.get('title', 'Untitled')}"):
                st.markdown(f"## {contrib.get('title', 'Untitled')}")
                st.markdown(f"**Type:** {contrib.get('story_type', 'N/A')} | **Language:** {contrib.get('language', 'N/A')} | **Region:** {contrib.get('region', 'N/A')}")
                st.markdown(f"**Author:** {contrib.get('author', 'Anonymous')} | **Year:** {contrib.get('year_composed', 'N/A')}")
                st.markdown("---")
                st.markdown(contrib.get('content', 'No content available.'))

            st.markdown("---")


if __name__ == "__main__":
    main()
