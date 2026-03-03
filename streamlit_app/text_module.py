"""
Text Module for BharatVerse
Story submission and text content management
"""

import streamlit as st
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))


@st.cache_data(ttl=1800, show_spinner=False)
def get_text_processing_config():
    """Get cached text processing configuration"""
    return {
        'max_text_length': 10000,
        'supported_languages': ['hi', 'en', 'bn', 'te', 'mr', 'ta', 'gu', 'kn', 'ml', 'pa'],
        'batch_size': 5
    }


def text_page():
    st.markdown("## 📝 Story Keeper")
    st.markdown("Document stories, proverbs, recipes, and wisdom from your culture.")

    get_text_processing_config()

    # Language selection
    st.markdown("### 🌐 Language Selection")
    language = st.selectbox(
        "Select the language of your story:",
        ["Hindi", "Bengali", "Telugu", "Marathi", "Tamil",
         "Gujarati", "Kannada", "Malayalam", "Punjabi", "English"],
        index=0
    )

    # Story type selection
    st.markdown("### 📖 Story Type")
    story_type = st.selectbox(
        "What type of content are you sharing?",
        ["Folk Tale", "Proverb", "Recipe", "Song", "Poem",
         "Historical Account", "Personal Story", "Other"]
    )

    # Title input
    title = st.text_input("Title", "")

    # Content input
    content = st.text_area(
        "Story Content",
        "",
        height=200,
        placeholder="Share your story, recipe, proverb, or cultural wisdom here..."
    )

    # Simple analysis section
    if st.checkbox("Analyze Text"):
        st.markdown("---")
        st.markdown("### 🔄 Text Analysis")
        if st.button("Analyze", key="analyze_story"):
            if not content.strip():
                st.warning("Please enter some content to analyze.")
            else:
                with st.spinner("Analyzing text..."):
                    word_count = len(content.split())
                    char_count = len(content)
                    sentence_count = content.count('.') + content.count('!') + content.count('?')
                    if sentence_count == 0:
                        sentence_count = 1

                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Word Count", word_count)
                    with col2:
                        st.metric("Character Count", char_count)
                    with col3:
                        st.metric("Sentences", sentence_count)
                    with col4:
                        st.metric("Language", language)

                    # Readability estimate
                    avg_words_per_sentence = word_count / sentence_count
                    if avg_words_per_sentence < 15:
                        readability = "Easy"
                    elif avg_words_per_sentence < 25:
                        readability = "Moderate"
                    else:
                        readability = "Complex"

                    st.info(f"📊 Readability: **{readability}** (avg {avg_words_per_sentence:.1f} words/sentence)")
                    st.success("✅ Basic analysis completed!")

    # Metadata
    st.markdown("---")
    st.markdown("### 🏷️ Metadata & Tags")

    col1, col2 = st.columns(2)
    with col1:
        author = st.text_input("Author/Credited Contributor", "Anonymous")
        region = st.text_input("Region/State", "")
    with col2:
        keywords = st.text_input("Keywords/Tags (comma-separated)", "tradition, culture")
        year_composed = st.number_input("Year Composed (Optional)", 1800, 2026, 2026)

    # Consent checkbox
    consent = st.checkbox(
        "I confirm that I have the right to share this content and agree to the "
        "terms of use and CC-BY 4.0 license for the contributed data."
    )

    # Submit button
    if st.button("Submit Story", type="primary", use_container_width=True):
        if not title.strip():
            st.error("Please provide a title for your story.")
        elif not content.strip():
            st.error("Please provide content for your story.")
        elif not consent:
            st.error("Please confirm that you have the right to share this content.")
        else:
            # Prepare contribution data
            contribution_data = {
                "title": title,
                "content": content,
                "content_type": "text",
                "language": language,
                "story_type": story_type,
                "author": author,
                "region": region,
                "keywords": keywords,
                "year_composed": year_composed,
                "created_at": datetime.now().isoformat()
            }

            # Save to session state
            if 'contributions' not in st.session_state:
                st.session_state.contributions = []
            st.session_state.contributions.append(contribution_data)

            st.success("✅ Story saved successfully!")
            st.balloons()
            st.markdown("### 🎉 Thank you for your contribution!")
            st.markdown("Your story has been added to the BharatVerse collection.")

            if st.button("Submit Another Story"):
                st.rerun()


if __name__ == "__main__":
    text_page()
