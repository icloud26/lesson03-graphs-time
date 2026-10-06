import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")

st.write(
    "1년 동안의 일별 박스오피스 데이터를 이용해 "
    "영화의 관객 수가 시간에 따라 어떻게 변했는지 살펴봅니다."
)


# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------
DATA_URL = (
    "https://raw.githubusercontent.com/"
    "greatsong/modudata/main/data/kobis_daily.csv"
)

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 날짜를 실제 날짜 형식으로 변환
    df["날짜"] = pd.to_datetime(
        df["날짜"].astype(str),
        format="%Y%m%d"
    )

    # 관객 수를 숫자로 변환
    df["일관객"] = pd.to_numeric(
        df["일관객"],
        errors="coerce"
    )

    return df


df = load_data()


# ==================================================
# 1구역 : 영화별 일관객 변화
# ==================================================
st.divider()

st.header("1. 영화별 일관객 변화")

st.write(
    "영화를 선택하면 날짜에 따라 하루 관객 수가 "
    "어떻게 변했는지 확인할 수 있습니다."
)

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
    "영화를 선택하세요",
    movie_list
)

movie_df = df[df["영화명"] == selected_movie].copy()

movie_df = movie_df.sort_values("날짜")


# --------------------------------------------------
# 선 그래프
# --------------------------------------------------
fig = px.line(
    movie_df,
    x="날짜",
    y="일관객",
    markers=True,
    title=f"{selected_movie}의 날짜별 일관객 변화"
)

fig.update_traces(
    hovertemplate=(
        "날짜: %{x|%Y-%m-%d}<br>"
        "관객 수: %{y:,.0f}명"
        "<extra></extra>"
    )
)

fig.update_layout(
    xaxis_title="날짜",
    yaxis_title="일관객 수",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# --------------------------------------------------
# 그래프 해석 자리
# --------------------------------------------------
st.markdown("#### 💡 이 그래프로 알 수 있는 것")

st.info(
    "여기에 그래프를 보고 알 수 있는 특징을 한 문장으로 작성합니다."
)


# ==================================================
# 다음 그래프 구역
# ==================================================
st.divider()

st.header("2. 다음 그래프")

st.write(
    "앞으로 새로운 그래프를 추가할 구역입니다."
)
