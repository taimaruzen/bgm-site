import streamlit as st

st.set_page_config(page_title="フリーBGMダウンロード", page_icon="🎵")
st.title("🎵 フリーBGMダウンロードサイト")
st.caption("著作権フリー・商用OKのBGMを配布しています。")

# BGMの一覧（表示名・ファイルパス・ダウンロード名を分けて管理）
bgms = [
    {
        "title": "cfg.mp3",            # 表示される曲名
        "file": "bgm/cfg.mp3",            # 実際の音声ファイルのパス
        "filename": "cfg.mp3"      # ダウンロード時のファイル名
    }
]

# 曲一覧を表示
for bgm in bgms:
    st.subheader(bgm["title"])
    st.audio(bgm["file"])

    with open(bgm["file"], "rb") as f:
        st.download_button("⬇️ ダウンロード", f, file_name=bgm["filename"])
