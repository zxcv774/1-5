import streamlit as st
import random
import time

st.set_page_config(
    page_title="🎰 오늘 뭐 먹지 슬롯머신",
    page_icon="🎰",
    layout="centered"
)

# -----------------------
# 음식 데이터
# -----------------------
foods = [
    "김치찌개", "된장찌개", "제육볶음", "비빔밥",
    "불고기", "삼겹살", "냉면", "돈까스",
    "초밥", "우동", "라멘", "규동",
    "짜장면", "짬뽕", "탕수육",
    "떡볶이", "라볶이", "김밥",
    "치즈버거", "불고기버거",
    "까르보나라", "알리오올리오",
    "로제파스타", "마르게리타피자",
    "페퍼로니피자", "스테이크",
    "치킨", "마라탕", "쌀국수"
]

# -----------------------
# 세션 상태
# -----------------------
if "history" not in st.session_state:
    st.session_state.history = []

if "lever_pulled" not in st.session_state:
    st.session_state.lever_pulled = False

# -----------------------
# 제목
# -----------------------
st.title("🎰 오늘 뭐 먹지?")
st.write("레버를 당겨 오늘의 메뉴를 결정하세요!")

st.markdown("---")

# -----------------------
# 슬롯 표시
# -----------------------
slot_area = st.empty()

slot_area.markdown(
"""
# 🎰 슬롯머신

| 🍔 | 🍕 | 🍜 |
|---|---|---|
| ??? | ??? | ??? |
"""
)

# -----------------------
# 레버
# -----------------------
if st.button("🕹️ 레버 당기기", use_container_width=True):
    st.session_state.lever_pulled = True

# -----------------------
# 슬롯 실행
# -----------------------
if st.session_state.lever_pulled:

    try:

        recent = st.session_state.history[-5:]

        available = [
            food for food in foods
            if food not in recent
        ]

        if not available:
            available = foods

        winner = random.choice(available)

        delays = (
            [0.03] * 15 +
            [0.05] * 10 +
            [0.08] * 8 +
            [0.12] * 5 +
            [0.18] * 3
        )

        for delay in delays:

            left = random.choice(foods)
            center = random.choice(foods)
            right = random.choice(foods)

            slot_area.markdown(
                f"""
# 🎰 슬롯머신

| 🍔 | 🍕 | 🍜 |
|---|---|---|
| {left} | {center} | {right} |

### 🔄 릴 회전 중...
"""
            )

            time.sleep(delay)

        left_final = random.choice(foods)
        right_final = random.choice(foods)

        slot_area.markdown(
            f"""
# 🎰 슬롯머신

| 🍔 | 🏆당첨🏆 | 🍜 |
|---|---|---|
| {left_final} | **{winner}** | {right_final} |

# 🍽️ {winner}
"""
        )

        st.session_state.history.append(winner)

        st.balloons()

        st.success(
            f"오늘 먹을 메뉴는 👉 {winner}"
        )

    except Exception as e:
        st.error(f"오류 발생: {e}")

    finally:
        st.session_state.lever_pulled = False

# -----------------------
# 기록
# -----------------------
st.markdown("---")

st.subheader("📜 최근 추천 기록")

if st.session_state.history:

    for item in reversed(
        st.session_state.history[-10:]
    ):
        st.write(f"• {item}")

else:
    st.info("아직 추천 기록이 없습니다.")

# -----------------------
# 정보
# -----------------------
st.caption(
    f"등록된 음식 수 : {len(foods)}개"
)
