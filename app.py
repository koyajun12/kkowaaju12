import random
import streamlit as st

# 페이지 기본 설정 (스마트폰에 최적화)
st.set_page_config(
    page_title="JLPT N5 한자 공부 앱", page_icon="📖", layout="centered"
)

# 이미지 속 1번 ~ 103번 전체 한자 데이터베이스
KANJI_DB = [
    {"kanji": "日", "kor_meaning": "날 일", "onyomi": "ニチ, ジツ", "kunyomi": "ひ, か"},
    {"kanji": "一", "kor_meaning": "한 일", "onyomi": "イチ, イツ", "kunyomi": "ヒトツ"},
    {"kanji": "国", "kor_meaning": "나라 국", "onyomi": "コク", "kunyomi": "くに"},
    {"kanji": "会", "kor_meaning": "모일 회", "onyomi": "カイ, エ", "kunyomi": "あ・う"},
    {"kanji": "人", "kor_meaning": "사람 인", "onyomi": "ジン, ニン", "kunyomi": "ひと"},
    {"kanji": "年", "kor_meaning": "해 년", "onyomi": "ネン", "kunyomi": "とし"},
    {"kanji": "大", "kor_meaning": "큰 대", "onyomi": "ダイ, タイ", "kunyomi": "おお・きい"},
    {"kanji": "十", "kor_meaning": "열 십", "onyomi": "ジュウ, ジッ", "kunyomi": "とお"},
    {"kanji": "二", "kor_meaning": "두 이", "onyomi": "ニ", "kunyomi": "ふた・つ"},
    {"kanji": "本", "kor_meaning": "근본 본", "onyomi": "ホン", "kunyomi": "もと"},
    {"kanji": "中", "kor_meaning": "가운데 중", "onyomi": "チュウ", "kunyomi": "なか"},
    {"kanji": "長", "kor_meaning": "긴 장", "onyomi": "チョウ", "kunyomi": "なが・い"},
    {
        "kanji": "出",
        "kor_meaning": "날 출",
        "onyomi": "シュツ",
        "kunyomi": "で・る, だ・す",
    },
    {"kanji": "三", "kor_meaning": "석 삼", "onyomi": "サン", "kunyomi": "みっ・つ"},
    {"kanji": "時", "kor_meaning": "때 시", "onyomi": "ジ", "kunyomi": "とき"},
    {
        "kanji": "行",
        "kor_meaning": "다닐 행",
        "onyomi": "コウ, ギョウ",
        "kunyomi": "い・く, おこな・う",
    },
    {"kanji": "社", "kor_meaning": "모여들 사", "onyomi": "シャ", "kunyomi": "やしろ"},
    {"kanji": "見", "kor_meaning": "볼 견", "onyomi": "ケン", "kunyomi": "み・る"},
    {"kanji": "月", "kor_meaning": "달 월", "onyomi": "ゲツ, ガツ", "kunyomi": "つき"},
    {
        "kanji": "分",
        "kor_meaning": "나눌 분",
        "onyomi": "ブン, フン, ブ",
        "kunyomi": "わ・かる",
    },
    {
        "kanji": "後",
        "kor_meaning": "뒤 후",
        "onyomi": "ゴ, 코우",
        "kunyomi": "のち, うしろ, あと",
    },
    {"kanji": "前", "kor_meaning": "앞 전", "onyomi": "ゼン", "kunyomi": "まえ"},
    {
        "kanji": "生",
        "kor_meaning": "날 생",
        "onyomi": "セイ, ショウ",
        "kunyomi": "い・きる, う・まれ",
    },
    {"kanji": "五", "kor_meaning": "다섯 오", "onyomi": "ゴ", "kunyomi": "いつ・つ"},
    {"kanji": "間", "kor_meaning": "사이 간", "onyomi": "カン, ケン", "kunyomi": "あいだ, ま"},
    {
        "kanji": "上",
        "kor_meaning": "위 상",
        "onyomi": "ジョウ, ショウ",
        "kunyomi": "うえ, あ・がる",
    },
    {"kanji": "東", "kor_meaning": "동녘 동", "onyomi": "トウ", "kunyomi": "ひがし"},
    {"kanji": "四", "kor_meaning": "넉 사", "onyomi": "シ", "kunyomi": "よっ・つ, よん"},
    {"kanji": "今", "kor_meaning": "이제 금", "onyomi": "コン, キン", "kunyomi": "いま"},
    {"kanji": "新", "kor_meaning": "새 신", "onyomi": "シン", "kunyomi": "あたら・しい"},
    {"kanji": "金", "kor_meaning": "쇠 금", "onyomi": "キン, コン", "kunyomi": "かね"},
    {
        "kanji": "九",
        "kor_meaning": "아홉 구",
        "onyomi": "キュウ, ク",
        "kunyomi": "ここの・つ",
    },
    {
        "kanji": "入",
        "kor_meaning": "들 입",
        "onyomi": "ニュウ",
        "kunyomi": "はい・る, い・れる",
    },
    {"kanji": "立", "kor_meaning": "설 립", "onyomi": "リツ", "kunyomi": "た・つ"},
    {"kanji": "手", "kor_meaning": "손 수", "onyomi": "シュ", "kunyomi": "て"},
    {"kanji": "学", "kor_meaning": "배울 학", "onyomi": "ガク", "kunyomi": "まな・ぶ"},
    {"kanji": "高", "kor_meaning": "높을 고", "onyomi": "コウ", "kunyomi": "たか・い"},
    {"kanji": "円", "kor_meaning": "둥글 엔", "onyomi": "エン", "kunyomi": "まる・い"},
    {"kanji": "子", "kor_meaning": "아들 자", "onyomi": "シ, ス", "kunyomi": "こ"},
    {"kanji": "目", "kor_meaning": "눈 목", "onyomi": "モク", "kunyomi": "め"},
    {"kanji": "外", "kor_meaning": "바깥 외", "onyomi": "ガイ, ゲ", "kunyomi": "そと, ほか"},
    {"kanji": "言", "kor_meaning": "말씀 언", "onyomi": "ゲン, ゴン", "kunyomi": "い・う, こと"},
    {"kanji": "八", "kor_meaning": "여덟 팔", "onyomi": "ハチ", "kunyomi": "やっ・つ"},
    {"kanji": "六", "kor_meaning": "여섯 륙", "onyomi": "ロク", "kunyomi": "むっ・つ"},
    {"kanji": "下", "kor_meaning": "아래 하", "onyomi": "カ, ゲ", "kunyomi": "した, さ・がる"},
    {"kanji": "来", "kor_meaning": "올 래", "onyomi": "ライ", "kunyomi": "く・る, き・たる"},
    {"kanji": "気", "kor_meaning": "기운 기", "onyomi": "キ, ケ", "kunyomi": "-"},
    {
        "kanji": "小",
        "kor_meaning": "작을 소",
        "onyomi": "ショウ",
        "kunyomi": "ちい・さい, こ",
    },
    {"kanji": "七", "kor_meaning": "일곱 칠", "onyomi": "シチ", "kunyomi": "なな・つ"},
    {"kanji": "山", "kor_meaning": "뫼 산", "onyomi": "サン", "kunyomi": "やま"},
    {
        "kanji": "話",
        "kor_meaning": "말할 화",
        "onyomi": "ワ",
        "kunyomi": "はな・す, はなし",
    },
    {"kanji": "多", "kor_meaning": "많을 다", "onyomi": "タ", "kunyomi": "おお・い"},
    {"kanji": "安", "kor_meaning": "편안 안", "onyomi": "アン", "kunyomi": "やす・い"},
    {"kanji": "女", "kor_meaning": "계집 녀", "onyomi": "ジョ, ニョ", "kunyomi": "おんな, め"},
    {"kanji": "北", "kor_meaning": "북녘 북", "onyomi": "ホク", "kunyomi": "きた"},
    {"kanji": "午", "kor_meaning": "낮 오", "onyomi": "ゴ", "kunyomi": "-"},
    {"kanji": "百", "kor_meaning": "일백 백", "onyomi": "ヒャク", "kunyomi": "-"},
    {"kanji": "書", "kor_meaning": "글 서", "onyomi": "ショ", "kunyomi": "か・く"},
    {"kanji": "先", "kor_meaning": "먼저 선", "onyomi": "セン", "kunyomi": "さき"},
    {"kanji": "名", "kor_meaning": "이름 명", "onyomi": "メイ, ミョウ", "kunyomi": "な"},
    {"kanji": "川", "kor_meaning": "내 천", "onyomi": "セン", "kunyomi": "かわ"},
    {"kanji": "千", "kor_meaning": "일천 천", "onyomi": "セン", "kunyomi": "ち"},
    {"kanji": "道", "kor_meaning": "길 도", "onyomi": "ドウ", "kunyomi": "みち"},
    {"kanji": "水", "kor_meaning": "물 수", "onyomi": "スイ", "kunyomi": "みず"},
    {"kanji": "半", "kor_meaning": "반 반", "onyomi": "ハン", "kunyomi": "なか・ば"},
    {"kanji": "男", "kor_meaning": "사나이 남", "onyomi": "ダン,ナン", "kunyomi": "おとこ"},
    {"kanji": "西", "kor_meaning": "서녘 서", "onyomi": "セイ, サイ", "kunyomi": "にし"},
    {"kanji": "電", "kor_meaning": "번개 전", "onyomi": "デン", "kunyomi": "-"},
    {"kanji": "口", "kor_meaning": "입 구", "onyomi": "コウ, ク", "kunyomi": "くち"},
    {
        "kanji": "少",
        "kor_meaning": "적을 소",
        "onyomi": "ショウ",
        "kunyomi": "すく・ない, すこ・し",
    },
    {"kanji": "校", "kor_meaning": "학교 교", "onyomi": "コウ", "kunyomi": "-"},
    {"kanji": "語", "kor_meaning": "말씀 어", "onyomi": "ゴ", "kunyomi": "かた・る"},
    {
        "kanji": "空",
        "kor_meaning": "빌 공",
        "onyomi": "クウ",
        "kunyomi": "そら, あ・く, から",
    },
    {"kanji": "土", "kor_meaning": "흙 토", "onyomi": "ド, ト", "kunyomi": "つち"},
    {"kanji": "木", "kor_meaning": "나무 목", "onyomi": "ボク, モク", "kunyomi": "き"},
    {"kanji": "聞", "kor_meaning": "들을 문", "onyomi": "ブン, モン", "kunyomi": "き・く"},
    {
        "kanji": "食",
        "kor_meaning": "밥 식",
        "onyomi": "ショク",
        "kunyomi": "た・べる, く・う",
    },
    {"kanji": "車", "kor_meaning": "수레 차", "onyomi": "シャ", "kunyomi": "くるま"},
    {"kanji": "何", "kor_meaning": "어찌 하", "onyomi": "カ", "kunyomi": "なに, なん"},
    {"kanji": "南", "kor_meaning": "남녘 남", "onyomi": "ナン", "kunyomi": "みなみ"},
    {"kanji": "足", "kor_meaning": "발 족", "onyomi": "ソク", "kunyomi": "あし, た・りる"},
    {"kanji": "万", "kor_meaning": "일만 만", "onyomi": "マン, バン", "kunyomi": "-"},
    {"kanji": "店", "kor_meaning": "가게 점", "onyomi": "テン", "kunyomi": "みせ"},
    {"kanji": "毎", "kor_meaning": "매양 매", "onyomi": "マイ", "kunyomi": "-"},
    {"kanji": "白", "kor_meaning": "흰 백", "onyomi": "ハク", "kunyomi": "しろ・い"},
    {"kanji": "古", "kor_meaning": "옛 고", "onyomi": "コ", "kunyomi": "ふる・い"},
    {"kanji": "天", "kor_meaning": "하늘 천", "onyomi": "テン", "kunyomi": "あまつ, あめ"},
    {"kanji": "買", "kor_meaning": "살 매", "onyomi": "バイ", "kunyomi": "か・う"},
    {"kanji": "週", "kor_meaning": "돌 주", "onyomi": "シュウ", "kunyomi": "-"},
    {"kanji": "母", "kor_meaning": "어미 모", "onyomi": "ボ", "kunyomi": "はは"},
    {"kanji": "火", "kor_meaning": "불 화", "onyomi": "カ", "kunyomi": "ひ"},
    {"kanji": "花", "kor_meaning": "꽃 화", "onyomi": "カ", "kunyomi": "はな"},
    {"kanji": "右", "kor_meaning": "우측 우", "onyomi": "ウ, ユウ", "kunyomi": "みぎ"},
    {"kanji": "読", "kor_meaning": "읽을 독", "onyomi": "ドク", "kunyomi": "よ・む"},
    {"kanji": "友", "kor_meaning": "벗 우", "onyomi": "ユウ", "kunyomi": "とも"},
    {"kanji": "左", "kor_meaning": "왼 좌", "onyomi": "サ", "kunyomi": "ひだり"},
    {"kanji": "休", "kor_meaning": "쉴 휴", "onyomi": "キュウ", "kunyomi": "やす・む"},
    {"kanji": "父", "kor_meaning": "아비 부", "onyomi": "フ", "kunyomi": "ちち"},
    {"kanji": "駅", "kor_meaning": "정거장 역", "onyomi": "エキ", "kunyomi": "-"},
    {"kanji": "雨", "kor_meaning": "비 우", "onyomi": "ウ", "kunyomi": "あめ"},
    {"kanji": "饮", "kor_meaning": "마실 음", "onyomi": "イン", "kunyomi": "の・む"},
    {
        "kanji": "魚",
        "kor_meaning": "물고기 어",
        "onyomi": "ギョ",
        "kunyomi": "さかな, うお",
    },
    {"kanji": "耳", "kor_meaning": "귀 이", "onyomi": "ジ", "kunyomi": "みみ"},
]

st.title("🇯🇵 JLPT N5 한자 학습 앱")

# 모드 선택
mode = st.radio(
    "학습 모드를 선택하세요",
    ("🎴 플래시카드", "✍️ 직접 입력 퀴즈"),
    horizontal=True,
)

# 세션 상태 초기화 (문제 유지)
if "card_item" not in st.session_state:
    st.session_state.card_item = random.choice(KANJI_DB)
if "quiz_item" not in st.session_state:
    st.session_state.quiz_item = random.choice(KANJI_DB)
if "show_card_answer" not in st.session_state:
    st.session_state.show_card_answer = False

# ----------------------------------------------------
# 1. 플래시카드 모드
# ----------------------------------------------------
if mode == "🎴 플래시카드":
    st.markdown("---")
    item = st.session_state.card_item

    # 한자 크게 표시
    st.markdown(
        f"<h1 style='text-align: center; font-size: 100px; margin: 0;'>{item['kanji']}</h1>",
        unsafe_allow_html=True,
    )

    if st.session_state.show_card_answer:
        st.info(
            f"**훈음**: {item['kor_meaning']}\n\n**음독**: {item['onyomi']}\n\n**훈독**: {item['kunyomi']}"
        )
    else:
        st.write(" ")

    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "👁️ 정답 확인 / 뒤집기", use_container_width=True
        ):
            st.session_state.show_card_answer = (
                not st.session_state.show_card_answer
            )
            st.rerun()

    with col2:
        if st.button("➡️ 다음 한자", use_container_width=True):
            st.session_state.card_item = random.choice(KANJI_DB)
            st.session_state.show_card_answer = False
            st.rerun()

# ----------------------------------------------------
# 2. 직접 입력 퀴즈 모드
# ----------------------------------------------------
else:
    st.markdown("---")
    item = st.session_state.quiz_item

    st.markdown(
        f"<h1 style='text-align: center; font-size: 90px; margin: 0;'>{item['kanji']}</h1>",
        unsafe_allow_html=True,
    )

    user_input = st.text_input(
        "한국어 훈음을 입력하세요 (예: 날 일)", key="user_quiz_input"
    )

    if st.button("제출", use_container_width=True):
        if user_input.replace(" ", "") == item["kor_meaning"].replace(" ", ""):
            st.success("⭕ 정답입니다!")
        else:
            st.error(
                f"❌ 오답입니다!\n\n정답: {item['kor_meaning']} (음독: {item['onyomi']} / 훈독: {item['kunyomi']})"
            )

    if st.button("➡️ 다음 문제", use_container_width=True):
        st.session_state.quiz_item = random.choice(KANJI_DB)
        st.rerun()
