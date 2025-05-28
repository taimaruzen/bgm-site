import streamlit as st

st.set_page_config(page_title="フリーBGMダウンロード", page_icon="🎵")
st.title("🎵 フリーBGMダウンロードサイト")
st.caption("著作権フリー・商用OKのBGMを配布しています。")

bgms = [
    {"title": "Relax Loop", "file": "C.F.G.mp3"},
]

for bgm in bgms:
    st.subheader(bgm["title"])
    st.audio(bgm["file"])

    with open(bgm["file"], "rb") as f:
        st.download_button("⬇️ ダウンロード", f, file_name=bgm["title"] + ".mp3")
