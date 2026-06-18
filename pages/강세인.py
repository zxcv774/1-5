import streamlit as st
import random

st.set_page_config(
    page_title="지갑 사정에 맞춘 메뉴 추천기",
    page_icon="💸",
    layout="centered"
)

MENU_DATA = [
    {"name": "김밥", "price": 4000, "category": "한식"},
    {"name": "라면", "price": 4500, "category": "한식"},
    {"name": "떡볶이", "price": 5000, "category": "분식"},
    {"name": "비빔밥", "price": 8000, "category": "한식"},
    {"name": "제육덮밥", "price": 9000, "category": "한식"},
    {"name": "돈까스", "price": 10000, "category": "일식"},
    {"name": "냉면", "price": 11000, "category": "한식"},
    {"name": "국밥", "price": 12000, "category": "한식"},
    {"name": "짜장면", "price": 7000, "category": "중식"},
    {"name": "짬뽕", "price": 9000, "category": "중식"},
    {"name": "초밥", "price": 18000, "category": "일식"},
    {"name": "파스타", "price": 16000, "category": "양식"},
    {"name": "햄버거 세트", "price": 9000, "category": "패스트푸드"},
    {"name": "치킨", "price": 22000, "category": "치킨"},
    {"name": "피자", "price": 25000, "category": "양식"},
    {"name": "스테이크", "price": 30000, "category": "양식"},
]

st.title("💸 지갑 사정에 맞춘 메뉴 추천기")
st.write("현재 예산에 맞는 메뉴를 추천해드립니다.")

with st.form("recommend_form"):
    budget = st.number_input(
        "오늘 식사 예산 (원)",
        min_value=0,
        step=1000,
        value=10000
    )

    meal_time = st.radio(
        "식사 시간",
        ["점심", "저녁"],
        horizontal=True
    )

    categories = sorted(list(set(item["category"] for item in MENU_DATA)))

    category = st.selectbox(
        "음식 종류",
        ["전체"] + categories
    )

    submitted = st.form_submit_button("🍽️ 메뉴 추천받기")

if submitted:
    try:
        if budget <= 0:
            st.warning("예산을 입력해주세요.")
            st.stop()

        filtered = [
            item for item in MENU_DATA
            if item["price"] <= budget
        ]

        if category != "전체":
            filtered = [
                item for item in filtered
                if item["category"] == category
            ]

        if not filtered:
            st.error(
                f"{budget:,}원 이하에서 선택 가능한 메뉴가 없습니다."
            )
            st.stop()

        recommendations = random.sample(
            filtered,
            min(3, len(filtered))
        )

        st.success(
            f"{meal_time} 예산 {budget:,}원 기준 추천 결과"
        )

        for idx, menu in enumerate(recommendations, start=1):
            st.markdown(
                f"""
                ### {idx}. {menu['name']}
                - 카테고리: {menu['category']}
                - 예상 가격: {menu['price']:,}원
                """
            )

        final_pick = random.choice(recommendations)

        st.divider()

        st.subheader("🎯 오늘의 최종 추천")
        st.metric(
            label=final_pick["name"],
            value=f"{final_pick['price']:,}원"
        )

        remain = budget - final_pick["price"]

        if remain >= 0:
            st.info(
                f"선택 후 예상 잔액: {remain:,}원"
            )

    except Exception as e:
        st.error(
            f"오류가 발생했습니다: {str(e)}"
        )

st.divider()

st.caption(
    "예산에 맞는 메뉴를 랜덤 추천하는 간단한 앱입니다."
)
