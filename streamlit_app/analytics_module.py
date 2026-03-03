"""
Analytics Module for BharatVerse
Data visualization and analytics dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from core.service_manager import get_service_manager
from core.error_handler import error_boundary, handle_errors


def generate_sample_data():
    """Generate sample data for demonstration"""
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
    contributions_data = pd.DataFrame({
        'date': dates,
        'stories': np.random.poisson(10, 30),
        'users': np.random.poisson(5, 30),
        'views': np.random.poisson(100, 30),
    })

    categories = ['Folklore', 'Recipes', 'Traditions', 'Music', 'Dance', 'Art', 'History', 'Languages']
    category_data = pd.DataFrame({
        'category': categories,
        'count': [random.randint(20, 100) for _ in categories],
        'engagement': [random.randint(50, 500) for _ in categories]
    })

    regions = ['North', 'South', 'East', 'West', 'Central', 'Northeast']
    region_data = pd.DataFrame({
        'region': regions,
        'contributions': [random.randint(50, 200) for _ in regions],
        'active_users': [random.randint(20, 80) for _ in regions]
    })

    return contributions_data, category_data, region_data


@handle_errors(fallback_value=None, show_error=True)
def create_time_series_chart(data: pd.DataFrame):
    """Create time series chart for contributions"""
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data['date'], y=data['stories'],
        mode='lines+markers', name='Stories',
        line=dict(color='#667eea', width=2),
        marker=dict(size=6),
        fill='tozeroy', fillcolor='rgba(102, 126, 234, 0.1)'
    ))

    fig.add_trace(go.Scatter(
        x=data['date'], y=data['users'],
        mode='lines+markers', name='New Users',
        line=dict(color='#f093fb', width=2),
        marker=dict(size=6),
        fill='tozeroy', fillcolor='rgba(240, 147, 251, 0.1)'
    ))

    fig.update_layout(
        title="Activity Over Time",
        xaxis_title="Date", yaxis_title="Count",
        hovermode='x unified',
        template='plotly_white',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig


@handle_errors(fallback_value=None, show_error=True)
def create_category_chart(data: pd.DataFrame):
    """Create bar chart for content categories"""
    fig = px.bar(
        data, x='category', y='count',
        color='engagement',
        color_continuous_scale=['#667eea', '#764ba2'],
        labels={'count': 'Number of Stories', 'engagement': 'Engagement Score'},
        title="Content by Category"
    )
    fig.update_layout(
        template='plotly_white', height=400, showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig


@handle_errors(fallback_value=None, show_error=True)
def create_region_chart(data: pd.DataFrame):
    """Create pie chart for regional distribution"""
    fig = px.pie(
        data, values='contributions', names='region',
        title="Regional Distribution",
        color_discrete_sequence=px.colors.sequential.Purples_r,
        hole=0.4
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(template='plotly_white', height=400)
    return fig


@handle_errors(fallback_value=None, show_error=True)
def create_language_chart():
    """Create horizontal bar chart for language distribution"""
    languages = ['Hindi', 'Bengali', 'Telugu', 'Tamil', 'Marathi', 'Gujarati', 'Kannada', 'Malayalam']
    counts = [random.randint(30, 150) for _ in languages]

    fig = go.Figure(go.Bar(
        y=languages, x=counts,
        orientation='h',
        marker=dict(
            color=counts,
            colorscale='Viridis',
            showscale=True
        )
    ))
    fig.update_layout(
        title="Content by Language",
        xaxis_title="Number of Items",
        template='plotly_white', height=400,
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig


def display_metrics():
    """Display key metrics"""
    # Include actual session state contributions count
    actual_stories = len(st.session_state.get('contributions', []))
    total_stories = 2547 + actual_stories

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="Total Stories", value=f"{total_stories:,}", delta="+127 this week")
    with col2:
        st.metric(label="Active Users", value="1,234", delta="+89 this week")
    with col3:
        st.metric(label="Total Views", value="45.2K", delta="+2.3K today")
    with col4:
        st.metric(label="Engagement Rate", value="68%", delta="+5%")


def analytics_page():
    """Main analytics page"""

    # Header
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
    ">
        <h1 style="color: white; margin: 0;">📊 Analytics Dashboard</h1>
        <p style="color: rgba(255,255,255,0.9); margin-top: 0.5rem;">
            Track engagement and growth of cultural content
        </p>
    </div>
    """, unsafe_allow_html=True)

    get_service_manager()
    display_metrics()

    st.markdown("---")

    # Time period selector
    col1, col2 = st.columns([3, 1])
    with col2:
        time_period = st.selectbox(
            "Time Period",
            ["Last 7 days", "Last 30 days", "Last 90 days", "All time"],
            index=1
        )

    # Generate sample data
    contributions_data, category_data, region_data = generate_sample_data()

    # Charts row 1
    st.markdown("### 📈 Trends")
    with error_boundary("Failed to load time series chart"):
        fig = create_time_series_chart(contributions_data)
        if fig:
            st.plotly_chart(fig, use_container_width=True)

    # Charts row 2
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📚 Content Categories")
        with error_boundary("Failed to load category chart"):
            fig = create_category_chart(category_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### 🗺️ Regional Distribution")
        with error_boundary("Failed to load region chart"):
            fig = create_region_chart(region_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

    # Language distribution
    st.markdown("### 🌐 Language Distribution")
    with error_boundary("Failed to load language chart"):
        fig = create_language_chart()
        if fig:
            st.plotly_chart(fig, use_container_width=True)

    # Top contributors section
    st.markdown("---")
    st.markdown("### 🏆 Top Contributors This Month")

    contributors = pd.DataFrame({
        'Rank': ['🥇', '🥈', '🥉', '4', '5'],
        'Contributor': ['Priya Sharma', 'Raj Patel', 'Anita Desai', 'Vikram Singh', 'Meera Reddy'],
        'Stories': [23, 19, 17, 15, 14],
        'Views': ['2.3K', '1.9K', '1.7K', '1.5K', '1.4K'],
        'Region': ['North', 'West', 'South', 'East', 'Central']
    })

    st.dataframe(contributors, use_container_width=True, hide_index=True)

    # Recent activity feed
    st.markdown("---")
    st.markdown("### 🔄 Recent Activity")

    activities = [
        {"time": "2 minutes ago", "action": "New story added", "details": "Traditional Rajasthani Recipe by Priya"},
        {"time": "15 minutes ago", "action": "Community event created", "details": "Cultural Festival Discussion"},
        {"time": "1 hour ago", "action": "New user joined", "details": "Welcome to Amit Kumar!"},
        {"time": "3 hours ago", "action": "Story featured", "details": "Ancient Tamil Folklore gains 100+ views"},
        {"time": "5 hours ago", "action": "Milestone reached", "details": "2,500 stories collected!"},
    ]

    for activity in activities:
        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.6);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 0.5rem;
            border-left: 3px solid #667eea;
        ">
            <small style="color: #888;">{activity['time']}</small>
            <div><strong>{activity['action']}</strong></div>
            <div style="color: #666;">{activity['details']}</div>
        </div>
        """, unsafe_allow_html=True)

    # Export section
    st.markdown("---")
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        st.markdown("### 📥 Export Analytics Data")
    with col2:
        if st.button("📊 Export to CSV", use_container_width=True):
            csv = contributions_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"analytics_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    with col3:
        if st.button("📈 Generate Report", use_container_width=True):
            st.info("Report generation feature coming soon!")


if __name__ == "__main__":
    analytics_page()
