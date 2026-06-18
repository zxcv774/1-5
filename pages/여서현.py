import streamlit as st
import random
import time

st.set_page_config(
    page_title="오늘 뭐 먹지? 🎯",
    page_icon="🍽️",
    layout="centered"
)

# 세션 상태 초기화
if "menus" not in st.session_state:
    st.session_state.menus = []

if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = None


def add_menu():
    menu = new_menu.strip()

    if not menu:
        st.warning("메뉴를 입력해주세요.")
        return

    if menu in st.session_state.menus:
        st.warning("이미 추가된 메뉴입니다.")
        return

    st.session_state.menus.append(menu)


st.title("🍽️ 오늘 뭐 먹지?")
st.subheader("🎯 메뉴 룰렛")

st.write(
    "먹고 싶은 메뉴를 추가한 뒤 룰렛을 돌려보세요!"
)

# 메뉴 입력
new_menu = st.text_input(
    "메뉴 입력",
    placeholder="예: 김치찌개"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ 메뉴 추가"):
        add_menu()

with col2:
    if st.button("🍱 예시 메뉴 추가"):
        sample_menus = [
            "김치찌개",
            "제육볶음",
            "돈까스",
            "햄버거",
            "피자",
            "초밥",
            "파스타",
            "치킨"
        ]

        for menu in sample_menus:
            if menu not in st.session_state.menus:
                st.session_state.menus.append(menu)

# 메뉴 목록
st.divider()

st.subheader("📋 현재 메뉴")

if st.session_state.menus:
    for idx, menu in enumerate(st.session_state.menus, start=1):
        st.write(f"{idx}. {menu}")
else:
    st.info("아직 등록된 메뉴가 없습니다.")

# 초기화
if st.button("🗑️ 메뉴 전체 삭제"):
    st.session_state.menus = []
    st.session_state.selected_menu = None
    st.rerun()

st.divider()

# 룰렛
if st.button("🎯 룰렛 돌리기", type="primary"):

    if len(st.session_state.menus) < 2:
        st.error("최소 2개 이상의 메뉴를 추가해주세요.")
    else:

        placeholder = st.empty()

        try:
            # 회전 연출
            for _ in range(20):
                placeholder.markdown(
                    f"""
                    ## 🎲 {random.choice(st.session_state.menus)}
                    """
                )
                time.sleep(0.08)

            result = random.choice(st.session_state.menus)
            st.session_state.selected_menu = result

            placeholder.empty()

            st.success("메뉴가 결정되었습니다!")
            st.balloons()

        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")

# 결과 표시
if st.session_state.selected_menu:

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
            background-color:#FFEB99;
            padding:25px;
            border-radius:15px;
            text-align:center;
            border:3px solid orange;
        ">
            <h1>🍴 {st.session_state.selected_menu}</h1>
            <h3>오늘의 메뉴 당첨!</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
