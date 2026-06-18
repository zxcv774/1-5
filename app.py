import streamlit as st
import random

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="오늘 뭐 먹지?",
    page_icon="🍽️",
    layout="centered"
)

# -----------------------------
# 음식 데이터
# -----------------------------
foods = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "제육볶음",
        "불고기",
        "비빔밥",
        "삼겹살",
        "순두부찌개",
        "닭갈비"
    ],
    "양식": [
        "파스타",
        "스테이크",
        "피자",
        "햄버거",
        "리조또",
        "샐러드",
        "오믈렛",
        "라자냐"
    ],
    "일식": [
        "초밥",
        "라멘",
        "돈카츠",
        "우동",
        "가츠동",
        "규동",
        "사시미",
        "오코노미야키"
    ]
}

# -----------------------------
# 세션 상태 초기화
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"


# -----------------------------
# 홈 화면
# -----------------------------
def home_page():
    st.title("🍽️ 오늘 뭐 먹지?")
    st.write("먹고 싶은 음식 종류를 선택하세요.")

    st.markdown("### 메뉴")

    # 이미지 느낌의 세로 버튼 배치
    if st.button("한식", use_container_width=True):
        st.session_state.page = "한식"
        st.rerun()

    if st.button("양식", use_container_width=True):
        st.session_state.page = "양식"
        st.rerun()

    if st.button("일식", use_container_width=True):
        st.session_state.page = "일식"
        st.rerun()


# -----------------------------
# 음식 추천 페이지
# -----------------------------
def food_page(category):
    st.title(f"🍴 {category} 추천")

    try:
        food = random.choice(foods[category])

        st.success(f"오늘의 추천 메뉴: {food}")

        st.write("맛있게 드세요 😋")

        if st.button("🔄 다시 추천받기"):
            st.rerun()

    except Exception:
        st.error("메뉴 추천 중 오류가 발생했습니다.")

    st.divider()

    if st.button("🏠 홈으로"):
        st.session_state.page = "home"
        st.rerun()


# -----------------------------
# 라우팅
# -----------------------------
if st.session_state.page == "home":
    home_page()

elif st.session_state.page == "한식":
    food_page("한식")

elif st.session_state.page == "양식":
    food_page("양식")

elif st.session_state.page == "일식":
    food_page("일식")
