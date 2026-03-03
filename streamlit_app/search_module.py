"""
Search / Discover Module for BharatVerse
Advanced search with filters, featured collections, and trending searches
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


def get_sample_data():
    """Sample cultural heritage data for search results"""
    return [
        {
            "title": "Traditional Bengali Baul Song",
            "type": "Audio",
            "language": "Bengali",
            "region": "East India",
            "description": "A soulful Baul song about spiritual journey and divine love, performed by a traditional Baul singer from Birbhum district.",
            "quality": 92,
            "tags": ["baul", "spiritual", "folk", "bengali", "traditional"]
        },
        {
            "title": "Rajasthani Wedding Customs",
            "type": "Text",
            "language": "Hindi",
            "region": "West India",
            "description": "Detailed documentation of traditional Rajasthani wedding rituals including pre-wedding ceremonies and post-wedding customs.",
            "quality": 88,
            "tags": ["wedding", "rajasthani", "customs", "rituals", "traditional"]
        },
        {
            "title": "Kathakali Performance Photos",
            "type": "Image",
            "language": "Malayalam",
            "region": "South India",
            "description": "High-quality photographs of Kathakali performance showcasing traditional makeup, costumes, and expressions.",
            "quality": 95,
            "tags": ["kathakali", "kerala", "dance", "performance", "traditional"]
        },
        {
            "title": "Punjabi Harvest Songs",
            "type": "Audio",
            "language": "Punjabi",
            "region": "North India",
            "description": "Collection of traditional Punjabi songs sung during harvest season, celebrating the joy of farming and community.",
            "quality": 87,
            "tags": ["punjabi", "harvest", "farming", "community", "celebration"]
        },
        {
            "title": "Tamil Pongal Recipes",
            "type": "Recipe",
            "language": "Tamil",
            "region": "South India",
            "description": "Authentic recipes for Pongal festival including sweet pongal, ven pongal, and traditional accompaniments.",
            "quality": 91,
            "tags": ["pongal", "tamil", "festival", "recipes", "traditional"]
        },
        {
            "title": "Gujarati Garba Dance Tutorial",
            "type": "Audio",
            "language": "Gujarati",
            "region": "West India",
            "description": "Step-by-step audio guide for learning traditional Garba dance moves performed during Navratri festival.",
            "quality": 89,
            "tags": ["garba", "gujarati", "dance", "navratri", "tutorial"]
        },
        {
            "title": "Assamese Bihu Celebration",
            "type": "Image",
            "language": "Assamese",
            "region": "Northeast India",
            "description": "Vibrant images from Bihu celebration showing traditional dance, music, and cultural activities.",
            "quality": 93,
            "tags": ["bihu", "assamese", "celebration", "dance", "culture"]
        },
        {
            "title": "Marathi Folk Tales",
            "type": "Story",
            "language": "Marathi",
            "region": "West India",
            "description": "Collection of traditional Marathi folk tales passed down through generations, featuring moral lessons and cultural wisdom.",
            "quality": 86,
            "tags": ["marathi", "folk tales", "stories", "wisdom", "traditional"]
        },
        {
            "title": "Karnataka Yakshagana Art",
            "type": "Image",
            "language": "Kannada",
            "region": "South India",
            "description": "Dramatic photographs of Yakshagana theatre performances, a traditional art form from coastal Karnataka.",
            "quality": 90,
            "tags": ["yakshagana", "karnataka", "theatre", "traditional", "art"]
        },
        {
            "title": "Odissi Classical Dance",
            "type": "Audio",
            "language": "Odia",
            "region": "East India",
            "description": "Recordings of traditional Odissi dance music, one of the oldest surviving dance forms of India.",
            "quality": 94,
            "tags": ["odissi", "classical", "dance", "odia", "ancient"]
        }
    ]


def filter_results(data, content_types, languages, regions, query):
    """Filter search results based on criteria"""
    filtered = []
    for item in data:
        include = True
        if content_types and item['type'] not in content_types:
            include = False
        if languages and item['language'] not in languages:
            include = False
        if regions and item['region'] not in regions:
            include = False
        if query:
            query_lower = query.lower()
            searchable = f"{item['title']} {item['description']} {' '.join(item['tags'])}".lower()
            if query_lower not in searchable:
                include = False
        if include:
            filtered.append(item)
    return filtered


def search_page():
    st.markdown("## 🔍 Discover Cultural Heritage")
    st.markdown("Search and explore India's rich cultural contributions")

    # Advanced search interface
    with st.container():
        st.markdown("### 🎯 Advanced Search")

        search_query = st.text_input(
            "🔍 Search for stories, songs, recipes, traditions...",
            placeholder="Try: 'Bengali folk song', 'Diwali recipes', 'wedding customs'",
            help="Use keywords, phrases, or specific terms to find cultural content"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            content_type = st.multiselect(
                "Content Type",
                ["Audio", "Text", "Image", "Recipe", "Story", "Custom"],
                default=["Audio", "Text", "Image"]
            )
        with col2:
            languages = st.multiselect(
                "Languages",
                ["Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati",
                 "Kannada", "Malayalam", "Punjabi", "Odia", "Assamese", "Urdu"],
                default=[]
            )
        with col3:
            regions = st.multiselect(
                "Regions",
                ["North India", "South India", "East India", "West India",
                 "Northeast India", "Central India"],
                default=[]
            )
        with col4:
            time_period = st.selectbox(
                "Time Period",
                ["All Time", "Last Week", "Last Month", "Last 3 Months", "Last Year"]
            )

        with st.expander("🔧 More Filters"):
            col1, col2, col3 = st.columns(3)
            with col1:
                categories = st.multiselect(
                    "Categories",
                    ["Festival", "Wedding", "Religious", "Folk", "Classical", "Modern",
                     "Food", "Art", "Dance", "Music", "Literature", "Craft"]
                )
            with col2:
                st.slider("Minimum Quality Score", 0, 100, 0)
                st.checkbox("Has English Translation")
            with col3:
                sort_by = st.selectbox(
                    "Sort By",
                    ["Relevance", "Date Added", "Popularity", "Quality Score", "Alphabetical"]
                )
                sort_order = st.radio("Order", ["Descending", "Ascending"], horizontal=True)

    # Search results
    if search_query or any([content_type, languages, regions]):
        st.markdown("---")
        st.markdown("### 📚 Search Results")

        all_data = get_sample_data()

        # Also include user contributions from session state
        if 'contributions' in st.session_state:
            for contrib in st.session_state.contributions:
                all_data.append({
                    "title": contrib.get("title", "Untitled"),
                    "type": "Text",
                    "language": contrib.get("language", "Unknown"),
                    "region": contrib.get("region", "Unknown"),
                    "description": contrib.get("content", "")[:200],
                    "quality": 80,
                    "tags": [t.strip() for t in contrib.get("keywords", "").split(",")]
                })

        search_results = filter_results(all_data, content_type, languages, regions, search_query)

        if not search_results:
            st.info("🔍 No results found. Try adjusting your filters or contribute content!")
            st.markdown("**Try:**")
            st.markdown("- Broaden your search query")
            st.markdown("- Remove some filters")
            st.markdown("- Add text content in the Text Stories page")
            return

        # Results summary
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Results", len(search_results))
        with col2:
            st.metric("Languages Found", len(set([r.get('language', 'Unknown') for r in search_results])))
        with col3:
            st.metric("Regions Covered", len(set([r.get('region', 'Unknown') for r in search_results])))

        # Results display
        icon_map = {
            "Audio": "🎙️", "Text": "📝", "Image": "📷",
            "Recipe": "🍳", "Story": "📖", "Custom": "🎭"
        }

        for i, result in enumerate(search_results[:10]):
            with st.container():
                col1, col2 = st.columns([1, 4])

                with col1:
                    st.markdown(f"""
                    <div style='background: #f0f2f6; padding: 2rem; border-radius: 8px; text-align: center; height: 120px; display: flex; align-items: center; justify-content: center;'>
                        <h1>{icon_map.get(result['type'], '📄')}</h1>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"### {result['title']}")

                    c1, c2, c3, c4 = st.columns(4)
                    with c1:
                        st.markdown(f"**Language:** {result['language']}")
                    with c2:
                        st.markdown(f"**Region:** {result['region']}")
                    with c3:
                        st.markdown(f"**Type:** {result['type']}")
                    with c4:
                        st.markdown(f"**Quality:** {result['quality']}%")

                    st.markdown(result['description'])

                    tags_html = " ".join([
                        f"<span style='background: #e1f5fe; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; margin: 2px;'>{tag}</span>"
                        for tag in result['tags']
                    ])
                    st.markdown(f"**Tags:** {tags_html}", unsafe_allow_html=True)

                    c1, c2, c3, c4 = st.columns(4)
                    with c1:
                        if st.button(f"👁️ View", key=f"view_{i}"):
                            st.session_state[f"show_details_{i}"] = True
                    with c2:
                        if st.button(f"⬇️ Download", key=f"download_{i}"):
                            st.success("Download started!")
                    with c3:
                        if st.button(f"❤️ Favorite", key=f"fav_{i}"):
                            st.success("Added to favorites!")
                    with c4:
                        if st.button(f"📤 Share", key=f"share_{i}"):
                            st.success("Share link copied!")

                if st.session_state.get(f"show_details_{i}", False):
                    with st.expander("📋 Content Details", expanded=True):
                        st.markdown(f"### {result['title']}")
                        st.markdown(f"**Type:** {result['type']} | **Language:** {result['language']} | **Region:** {result['region']}")
                        st.markdown(f"**Quality Score:** {result['quality']}%")
                        st.markdown("**Description:**")
                        st.markdown(result['description'])
                        st.markdown("**Tags:** " + ", ".join(result['tags']))

                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Views", "1,234")
                            st.metric("Downloads", "456")
                        with col2:
                            st.metric("Favorites", "89")
                            st.metric("Shares", "23")

                        if st.button("Close Details", key=f"close_{i}"):
                            st.session_state[f"show_details_{i}"] = False
                            st.rerun()

                st.markdown("---")

    # Featured collections
    st.markdown("### 🌟 Featured Collections")

    collections = [
        {
            "title": "Festival Songs of India",
            "description": "Traditional songs sung during various Indian festivals",
            "count": 156, "image": "🎵",
            "tags": ["festival", "music", "traditional"]
        },
        {
            "title": "Regional Wedding Customs",
            "description": "Wedding traditions and rituals from different states",
            "count": 89, "image": "💒",
            "tags": ["wedding", "customs", "regional"]
        },
        {
            "title": "Ancient Stories & Legends",
            "description": "Mythological stories and local legends",
            "count": 234, "image": "📚",
            "tags": ["mythology", "stories", "legends"]
        },
        {
            "title": "Traditional Recipes",
            "description": "Authentic recipes passed down through generations",
            "count": 178, "image": "🍛",
            "tags": ["food", "recipes", "traditional"]
        }
    ]

    col1, col2 = st.columns(2)
    for i, collection in enumerate(collections):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 10px; color: white; margin-bottom: 1rem;'>
                <h2>{collection['image']} {collection['title']}</h2>
                <p>{collection['description']}</p>
                <p><strong>{collection['count']} items</strong></p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Explore Collection", key=f"collection_{i}", use_container_width=True):
                st.success(f"Exploring {collection['title']}...")

    # Trending searches
    st.markdown("---")
    st.markdown("### 🔥 Trending Searches")

    trending = [
        "Diwali celebrations", "Bengali folk songs", "South Indian recipes",
        "Rajasthani art", "Punjabi wedding songs", "Kerala boat race",
        "Gujarati garba", "Tamil classical music", "Assamese bihu dance"
    ]

    cols = st.columns(3)
    for i, trend in enumerate(trending):
        with cols[i % 3]:
            if st.button(f"🔍 {trend}", key=f"trend_{i}", use_container_width=True):
                st.rerun()

    # Search tips
    with st.expander("💡 Search Tips & Suggestions"):
        st.markdown("""
        ### How to Search Effectively:

        **🎯 Use Specific Keywords:**
        - Instead of "song", try "Bengali folk song" or "Rajasthani devotional song"
        - Use festival names: "Holi songs", "Diwali recipes", "Durga Puja traditions"

        **🏷️ Combine Filters:**
        - Select specific languages and regions for targeted results
        - Use content type filters to find exactly what you need

        **📅 Time-based Searches:**
        - Recent additions often have better quality and metadata
        - Historical content might have unique cultural value

        **🔤 Try Different Languages:**
        - Search in both English and native scripts
        - Use transliterated terms (e.g., "bhajan", "kirtan", "qawwali")

        ### Popular Search Categories:
        - **Music:** "classical ragas", "folk songs", "devotional music"
        - **Food:** "festival recipes", "regional cuisine", "traditional sweets"
        - **Stories:** "panchatantra", "jataka tales", "local legends"
        - **Customs:** "wedding rituals", "birth ceremonies", "harvest festivals"
        """)


if __name__ == "__main__":
    search_page()
