<p align="center">
  <h1 align="center">🏛️ BharatVerse</h1>
  <p align="center"><strong>Preserving India's Cultural Heritage — One Story at a Time</strong></p>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#contributing">Contributing</a>
</p>

---

## 📖 About

**BharatVerse** is a community-driven platform built to document, discover, and celebrate India's rich cultural heritage. From folk tales and traditional recipes to regional art forms and ancestral wisdom — BharatVerse provides a digital space where cultural stories can be preserved for future generations.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📝 **Text Stories** | Submit and share cultural stories — traditions, folklore, recipes, and wisdom |
| 🔍 **Discover** | Search and explore heritage content across regions, categories, and languages |
| 📊 **Analytics** | Visualize cultural data with interactive charts and dashboards |
| 🤝 **Community Hub** | Connect with enthusiasts, collaborate on preservation initiatives |
| 📚 **Browse Contributions** | Explore all community contributions in one place |
| ℹ️ **About** | Learn about the mission and vision behind BharatVerse |

## 🛠️ Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/) — for rapid, interactive web app development
- **Data & Visualization:** Pandas, NumPy, Plotly
- **Image Processing:** Pillow
- **UI Enhancements:** Streamlit Option Menu, Streamlit Extras
- **Language:** Python 3.9+

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/GovindXDev/bharatverse.git
   cd bharatverse
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   streamlit run Home.py
   ```

   The app will open in your browser at `http://localhost:8501`.

## 📁 Project Structure

```
bharatverse/
├── Home.py                     # Main entry point & landing page
├── requirements.txt            # Python dependencies
├── .gitignore
├── .streamlit/                 # Streamlit configuration
├── pages/                      # Multi-page app modules
│   ├── 02_📝_Text_Stories.py   # Story submission page
│   ├── 04_🔍_Discover.py      # Search & discovery page
│   ├── 05_📊_Analytics.py     # Analytics dashboard
│   ├── 06_🤝_Community.py     # Community hub
│   ├── 11_📚_Browse_Contributions.py  # Contributions browser
│   └── 12_ℹ️_About.py         # About page
├── core/                       # Core application services
│   ├── __init__.py
│   ├── service_manager.py      # Service lifecycle management
│   └── error_handler.py        # Error handling & recovery
└── streamlit_app/              # Feature modules & utilities
    ├── __init__.py
    ├── text_module.py           # Text story logic
    ├── search_module.py         # Search & filtering
    ├── analytics_module.py      # Analytics & visualization
    ├── community_module.py      # Community features
    └── utils/                   # Shared utilities & styling
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Inspired by India's vibrant and diverse cultural heritage
- Made with ❤️ for cultural preservation

---

<p align="center">
  <strong>🏛️ BharatVerse</strong> — Preserving the past, enriching the future.
</p>
