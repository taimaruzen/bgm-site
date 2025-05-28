import streamlit as st

# ページ設定
st.set_page_config(page_title="🎵 フリーBGMダウンロードサイト", page_icon="🎧")

# サイドバー（フィルターやリンク）
st.sidebar.title("🎚️ メニュー")
genre = st.sidebar.radio("ジャンルを選択", ["すべて", "リラックス", "エピック"])

st.sidebar.markdown("---")
st.sidebar.markdown("💡 提供：taimaruzen")
st.sidebar.markdown("[GitHubで見る](https://github.com/taimaruzen/bgm-site)")

# メインタイトル
st.markdown("<h1 style='text-align: center;'>🎵 フリーBGMダウンロードサイト</h1>", unsafe_allow_html=True)
st.caption("著作権フリー・商用OKのBGMを無料で配布中")

# BGMリスト（ジャンル付き）
bgms = [
    {
        "title": "Relax Loop",
        "file": "bgm/cfg.mp3",
        "filename": "relax_loop.mp3",
        "description": "落ち着いたループ音。Vlog・配信・店舗BGMなど幅広く利用可能（2:57）",
        "genre": "リラックス"
    },
    {
        "title": "Epic Adventure",
        "file": "bgm/epic.mp3",
        "filename": "epic_adventure.mp3",
        "description": "壮大な展開があるBGM。映像・映画・オープニングに最適（3:21）",
        "genre": "エピック"
    }
]

# フィルタリング
filtered_bgms = [b for b in bgms if genre == "すべて" or b["genre"] == genre]

# 表示
for bgm in filtered_bgms:
    st.markdown(f"### 🎧 {bgm['title']}")
    st.markdown(f"<p style='color:gray;'>{bgm['description']}</p>", unsafe_allow_html=True)
    st.audio(bgm["file"])
    with open(bgm["file"], "rb") as f:
        st.download_button("⬇️ ダウンロードする", f, file_name=bgm["filename"])
    st.markdown("---")
