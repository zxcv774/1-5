
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="연애 코칭 앱",
    page_icon="💖",
    layout="centered"
)

# 제목
st.title("💖 연애 코칭 앱")

st.write("연애 고민을 입력하면 간단한 조언을 해드립니다.")

# 입력창
user_input = st.text_area(
    "연애 고민 입력",
    placeholder="예: 썸남이 연락이 뜸해졌어요..."
)

# 버튼
if st.button("조언 받기"):

    if user_input.strip() == "":
        st.warning("고민을 입력해주세요.")
    else:

        # 아주 간단한 규칙 기반 답변
        if "연락" in user_input:
            answer = """
            연락 빈도보다 중요한 건 관계의 전체 흐름입니다.
            상대를 몰아붙이기보다 편안한 대화를 시도해보세요.
            """

        elif "이별" in user_input:
            answer = """
            이별 직후에는 감정 정리가 우선입니다.
            급하게 관계를 되돌리려 하기보다 자신의 감정을 돌보세요.
            """

        elif "고백" in user_input:
            answer = """
            고백은 완벽한 타이밍보다 진심이 중요합니다.
            부담스럽지 않게 솔직한 마음을 표현해보세요.
            """

        else:
            answer = """
            상대의 마음만 분석하기보다,
            내가 어떤 관계를 원하는지도 함께 생각해보세요.
            """

        st.success("연애 코칭 결과")
        st.write(answer)

# 하단 문구
st.caption("Made with Streamlit 💕")
