import streamlit as st

# ページ設定
st.set_page_config(page_title="🎵 フリーBGMダウンロードサイト", page_icon="🎧", layout="centered")

# カスタムCSSでデザイン
st.markdown("""
    <style>
    body {
        background-color: #f4f8fb;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 48px;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #7f8c8d;
        margin-bottom: 40px;
    }
    .card {
        background-color: white;
        padding: 30px;
        margin-bottom: 30px;
        border-radius: 18px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.07);
    }
    .music-title {
        font-size: 28px;
        font-weight: bold;
        color: #34495e;
        margin-bottom: 10px;
    }
    .music-desc {
        font-size: 16px;
        color: #7f8c8d;
        margin-bottom: 20px;
    }
    .stAudio {
        margin-bottom: 20px;
    }
    .stDownloadButton > button {
        background-color: #2980b9;
        color: white;
        font-size: 16px;
        padding: 0.6em 1.5em;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown("<div class='title'>🎵 フリーBGMダウンロードサイト</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>著作権フリー・商用OKのBGMを無料で配布中</div>", unsafe_allow_html=True)

# BGMリスト
bgms = [
    {
        "title": "Relax Loop",
        "file": "bgm/cfg.mp3",
        "filename": "relax_loop.mp3",
        "description": "落ち着いたループ音。Vlog・配信・店舗BGMなど幅広く利用可能（2:57）"
    }
]

# BGMカード表示
for bgm in bgms:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='music-title'>{bgm['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='music-desc'>{bgm['description']}</div>", unsafe_allow_html=True)
    st.audio(bgm["file"])

    with open(bgm["file"], "rb") as f:
        st.download_button("⬇️ ダウンロードする", f, file_name=bgm["filename"], help="MP3ファイルを保存")
    
    st.markdown("</div>", unsafe_allow_html=True)
