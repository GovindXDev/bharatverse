"""
Community Module for BharatVerse
Community hub with feed, groups, events, and forums
"""

import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu


def community_page():
    """Main community page"""
    user_info = st.session_state.get('user_info')

    colored_header(
        label="🤝 BharatVerse Community",
        description="Connect and collaborate on cultural preservation",
        color_name="violet-70"
    )

    selected = option_menu(
        None,
        ["Feed", "Groups", "Events", "Forums"],
        icons=["newspaper", "people-fill", "calendar-event", "chat-dots"],
        default_index=0,
        orientation="horizontal"
    )

    if selected == "Feed":
        show_feed(user_info)
    elif selected == "Groups":
        show_groups(user_info)
    elif selected == "Events":
        show_events(user_info)
    else:
        show_forums(user_info)


def show_feed(user_info):
    st.markdown("### 📰 Community Feed")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Members", "1,234", "+89")
    col2.metric("Posts Today", "56", "+12")
    col3.metric("Events", "8", "+3")
    col4.metric("Groups", "45", "+2")

    # Post creation area
    with st.expander("✍️ Share Something"):
        post_title = st.text_input("Title", key="post_title")
        post_content = st.text_area("Content", height=100, key="post_content")
        if st.button("Post", type="primary"):
            if post_title and post_content:
                if 'community_posts' not in st.session_state:
                    st.session_state.community_posts = []
                st.session_state.community_posts.append({
                    "author": "You",
                    "title": post_title,
                    "content": post_content,
                    "time": "Just now",
                    "likes": 0
                })
                st.success("Posted successfully! 🎉")
                st.rerun()
            else:
                st.warning("Please provide both a title and content.")

    # Show user posts first
    if 'community_posts' in st.session_state:
        for idx, p in enumerate(reversed(st.session_state.community_posts)):
            with st.container():
                st.markdown(f"**{p['author']}** · {p['time']}")
                st.markdown(f"### {p['title']}")
                if p.get('content'):
                    st.markdown(p['content'])
                c1, c2, c3 = st.columns([1, 1, 8])
                with c1:
                    if st.button(f"❤️ {p['likes']}", key=f"user_like_{idx}"):
                        st.session_state.community_posts[len(st.session_state.community_posts) - 1 - idx]['likes'] += 1
                        st.rerun()
                with c2:
                    st.button("💬", key=f"user_comment_{idx}")
                st.divider()

    # Sample posts
    posts = [
        {"author": "Priya", "title": "Madhubani Painting Workshop", "time": "2h ago", "likes": 45,
         "content": "Just attended an amazing Madhubani painting workshop in Patna! The intricate patterns tell stories of our rich cultural heritage. 🎨"},
        {"author": "Raj", "title": "Folk Music Festival Chennai", "time": "5h ago", "likes": 23,
         "content": "The annual folk music festival in Chennai was incredible this year. So many traditional instruments and performers from across Tamil Nadu! 🎵"},
        {"author": "Admin", "title": "New Language Support Added", "time": "1d ago", "likes": 156,
         "content": "We're excited to announce support for 2 new languages: Konkani and Dogri! Keep contributing in your native languages. 🌐"},
        {"author": "Meera", "title": "Documenting Grandma's Recipes", "time": "2d ago", "likes": 89,
         "content": "Started documenting my grandmother's traditional Rajasthani recipes before they're lost forever. Already captured 15 unique dishes! 🍛"},
    ]

    for i, p in enumerate(posts):
        with st.container():
            st.markdown(f"**{p['author']}** · {p['time']}")
            st.markdown(f"### {p['title']}")
            st.markdown(p['content'])
            c1, c2, c3 = st.columns([1, 1, 8])
            with c1:
                st.button(f"❤️ {p['likes']}", key=f"l{i}")
            with c2:
                st.button("💬", key=f"c{i}")
            st.divider()


def show_groups(user_info):
    st.markdown("### 👥 Cultural Groups")
    st.markdown("Join groups to connect with people who share your cultural interests.")

    groups = [
        {"name": "Tamil Literature Circle", "members": 234, "description": "Discussing and preserving Tamil literary traditions", "icon": "📚"},
        {"name": "Kathak Dancers Network", "members": 189, "description": "Connecting classical Kathak dancers across India", "icon": "💃"},
        {"name": "Northeast Culture Hub", "members": 456, "description": "Celebrating the diverse cultures of Northeast India", "icon": "🏔️"},
        {"name": "Sanskrit Scholars Forum", "members": 167, "description": "Academic discussions on Sanskrit texts and traditions", "icon": "📜"},
        {"name": "Indian Cuisine Keepers", "members": 312, "description": "Preserving traditional recipes from every region", "icon": "🍛"},
        {"name": "Folk Art Collective", "members": 278, "description": "Supporting and documenting folk art traditions", "icon": "🎨"},
    ]

    cols = st.columns(2)
    for i, g in enumerate(groups):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-left: 4px solid #667eea;">
                <h4 style="margin: 0 0 0.5rem 0;">{g['icon']} {g['name']}</h4>
                <p style="color: #666; margin: 0 0 0.5rem 0; font-size: 0.9rem;">{g['description']}</p>
                <p style="color: #888; margin: 0; font-size: 0.85rem;">👥 {g['members']} members</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Join Group", key=f"j{i}", use_container_width=True):
                st.success(f"Joined {g['name']}! 🎉")


def show_events(user_info):
    st.markdown("### 📅 Cultural Events")
    st.markdown("Discover and participate in cultural events happening around India.")

    events = [
        {"name": "🎨 Madhubani Art Workshop", "date": "Tomorrow", "time": "10 AM - 1 PM",
         "location": "Online (Zoom)", "spots": 15, "description": "Learn the fundamentals of Madhubani painting from master artists."},
        {"name": "🎵 Classical Music Evening", "date": "Saturday", "time": "6 PM - 9 PM",
         "location": "National Auditorium, Delhi", "spots": 200, "description": "An evening of Hindustani classical music featuring renowned artists."},
        {"name": "🚶 Heritage Walk - Old Delhi", "date": "Sunday", "time": "8 AM - 12 PM",
         "location": "Chandni Chowk, Delhi", "spots": 30, "description": "Explore the rich cultural heritage of Old Delhi with expert guides."},
        {"name": "📖 Storytelling Festival", "date": "Next Wednesday", "time": "4 PM - 7 PM",
         "location": "Online (YouTube Live)", "spots": "Unlimited", "description": "Share and listen to folk stories from across India."},
        {"name": "🍛 Traditional Cooking Masterclass", "date": "Next Saturday", "time": "11 AM - 2 PM",
         "location": "Community Kitchen, Mumbai", "spots": 20, "description": "Learn to cook traditional Maharashtrian dishes with local chefs."},
    ]

    for i, e in enumerate(events):
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 12px; margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
            <h4 style="margin: 0 0 0.5rem 0;">{e['name']}</h4>
            <p style="color: #666; font-size: 0.95rem; margin: 0 0 0.5rem 0;">{e['description']}</p>
            <p style="color: #888; margin: 0; font-size: 0.85rem;">📅 {e['date']} · 🕐 {e['time']} · 📍 {e['location']} · 🎟️ {e['spots']} spots</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button("Register", key=f"r{i}", use_container_width=True):
                st.success(f"Registered for {e['name']}! 🎉")
        with col2:
            if st.button("Remind Me", key=f"remind_{i}", use_container_width=True):
                st.info("Reminder set!")
        st.divider()


def show_forums(user_info):
    st.markdown("### 💬 Discussion Forums")
    st.markdown("Share your knowledge and learn from the community.")

    # New topic creation
    with st.expander("📝 Start a New Discussion"):
        topic_title = st.text_input("Discussion Title", key="forum_title")
        topic_content = st.text_area("Your thoughts...", height=100, key="forum_content")
        topic_category = st.selectbox("Category", ["General", "Art & Craft", "Music & Dance", "Food & Recipes", "History", "Languages"])
        if st.button("Start Discussion", type="primary"):
            if topic_title:
                st.success("Discussion started! 🎉")
            else:
                st.warning("Please provide a title.")

    topics = [
        {"title": "How to Preserve Traditional Weaving Techniques?", "replies": 45, "views": 234, "category": "Art & Craft", "author": "Lakshmi"},
        {"title": "Learning Classical Music - Where to Start?", "replies": 32, "views": 156, "category": "Music & Dance", "author": "Rahul"},
        {"title": "Documenting Family Recipes - Best Practices", "replies": 67, "views": 345, "category": "Food & Recipes", "author": "Anita"},
        {"title": "Importance of Regional Dialects in Storytelling", "replies": 28, "views": 189, "category": "Languages", "author": "Dev"},
        {"title": "Digital Archives for Temple Architecture", "replies": 19, "views": 123, "category": "History", "author": "Sanjay"},
        {"title": "Teaching Children About Cultural Heritage", "replies": 51, "views": 278, "category": "General", "author": "Neha"},
    ]

    for i, t in enumerate(topics):
        st.markdown(f"""
        <div style="background: white; padding: 1rem 1.5rem; border-radius: 10px; margin-bottom: 0.75rem; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <h4 style="margin: 0 0 0.25rem 0; color: #1a1a2e;">{t['title']}</h4>
                    <small style="color: #888;">by {t['author']} · {t['category']}</small>
                </div>
                <div style="text-align: right;">
                    <span style="color: #667eea; font-weight: 600;">💬 {t['replies']}</span>
                    <span style="color: #888; margin-left: 1rem;">👁️ {t['views']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    community_page()
