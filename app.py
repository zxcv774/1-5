import streamlit as st
import random
import time

st.set_page_config(
    page_title="오늘 뭐 먹지?",
    page_icon="🍚",
    layout="centered"
)

# ------------------------
# 데이터
# ------------------------

food_categories = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "비빔밥",
        "불고기",
        "제육볶음",
        "삼겹살",
        "냉면"
    ],
    "중식": [
        "짜장면",
        "짬뽕",
        "탕수육",
        "마라탕",
        "마라샹궈",
        "볶음밥"
    ],
    "일식": [
        "초밥",
        "라멘",
        "우동",
        "돈까스",
        "규동",
        "가츠동"
    ],
    "양식": [
        "파스타",
        "스테이크",
        "리조또",
        "피자",
        "햄버거",
        "샐러드"
    ],
    "분식": [
        "떡볶이",
        "순대",
        "김밥",
        "라볶이",
        "쫄면"
    ],
    "패스트푸드": [
        "버거",
        "치킨",
        "핫도그",
        "감자튀김",
        "치킨버거"
    ]
}

all_foods = []
for foods in food_categories.values():
    all_foods.extend(foods)

# ------------------------
# 페이지 이동 상태
# ------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ------------------------
# 메인 화면
# ------------------------

if st.session_state.page == "home":

    st.title("🍚 오늘 뭐 먹지?")
    st.write("원하는 방식으로 메뉴를 결정해보세요!")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎰")
        st.write("슬롯 머신")
        if st.button("입장", key="slot"):
            st.session_state.page = "slot"
            st.rerun()

    with col2:
        st.subheader("🍚")
        st.write("카테고리 추천")
        if st.button("입장 ", key="recommend"):
            st.session_state.page = "recommend"
            st.rerun()

    with col3:
        st.subheader("🎯")
        st.write("룰렛")
        if st.button("입장  ", key="roulette"):
            st.session_state.page = "roulette"
            st.rerun()

# ------------------------
# 슬롯 머신
# ------------------------

elif st.session_state.page == "slot":

    st.title("🎰 슬롯 머신 메뉴 선택")

    if st.button("← 메인으로"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("---")

    slot_area = st.empty()

    if st.button("슬롯 돌리기"):

        final_food = random.choice(all_foods)

        for _ in range(20):
            a = random.choice(all_foods)
            b = random.choice(all_foods)
            c = random.choice(all_foods)

            slot_area.markdown(
                f"""
                # {a} | {b} | {c}
                """
            )

            time.sleep(0.08)

        slot_area.markdown(
            f"""
            # 🎉 {final_food}
            ### 오늘의 메뉴 당첨!
            """
        )

# ------------------------
# 카테고리 추천
# ------------------------

elif st.session_state.page == "recommend":

    st.title("🍚 밥 메뉴 기준 추천")

    if st.button("← 메인으로"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("---")

    category = st.selectbox(
        "먹고 싶은 종류를 선택하세요",
        list(food_categories.keys())
    )

    if st.button("추천 받기"):

        result = random.choice(food_categories[category])

        st.success(f"오늘은 **{result}** 어떠세요? 😋")

# ------------------------
# 룰렛
# ------------------------

elif st.session_state.page == "roulette":

    st.title("🎯 룰렛 메뉴 선택")

    if st.button("← 메인으로"):
        st.session_state.page = "home"
        st.rerun()

    st.markdown("---")

    user_input = st.text_area(
        "메뉴를 한 줄에 하나씩 입력하세요",
        height=200,
        placeholder="치킨\n피자\n족발\n햄버거"
    )

    if st.button("룰렛 돌리기"):

        items = [
            x.strip()
            for x in user_input.split("\n")
            if x.strip()
        ]

        if len(items) < 2:
            st.warning("최소 2개 이상의 메뉴를 입력해주세요.")
        else:

            roulette_area = st.empty()

            for _ in range(25):
                current = random.choice(items)

                roulette_area.markdown(
                    f"# 🎯 {current}"
                )

                time.sleep(0.06)

            winner = random.choice(items)

            roulette_area.markdown(
                f"""
                # 🏆 {winner}
                ### 오늘의 메뉴 확정!
                """
            )
