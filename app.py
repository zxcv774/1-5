import streamlit as st

# 페이지 설정 (닫히지 않았던 괄호와 따옴표 수정)
st.set_page_config(
    page_title="오늘 뭐 먹지?",
    layout="wide"  # 컬럼(col1, col2, col3)이 예쁘게 나오도록 레이아웃을 wide로 설정하는 것을 추천합니다.
)

st.title("🍽️ 오늘 뭐 먹지?")
st.write("원하는 방식으로 오늘의 식사 메뉴를 정해보세요!")

st.divider()

st.subheader("메뉴 선택 방법")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/강세인.py",
        label="🎡 룰렛 돌려 메뉴 정하기",
        icon="🎡"
    )

with col2:
    st.page_link(
        "pages/여서현.py",
        label="💰 지갑 사정 고려",
        icon="💰"
    )

with col3:
    st.page_link(
        "pages/이예나.py",
        label="🎰 슬롯머신",
        icon="🎰"
    )

st.divider()

st.info(
    "오늘의 메뉴를 쉽고 재미있게 결정해보세요!"
)
