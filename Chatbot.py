import streamlit as st
import time

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

db = {
'97김정근':'임원',
'96한승하':'임원',
'00김다윤':'임원',
'99정유진':'임원',
'99권소은':'임원',
'04민다인':'임원',
'03신동재':'임원',
'01유태영':'임원',
    '02김은하': '김은하',
    '02김령은': '김은하',
    '05홍동기': '김은하',
    '05이진우': '김은하',
    '05조성우': '김은하',
    '04이채원': '김은하',
    '04김지우': '김은하',
    '03김에스더': '김은하',
    '02이승훈': '김은하',
    '01김현우': '김은하',
    '99정시은': '김은하',
    '99홍해미': '김은하',
    '98전은규': '김은하',
    '97최린': '김은하',
    '96박상우': '김은하',
    '96이성준': '김은하',
    '95정유정': '김은하',
    '98김상정': '김상정',
    '99박주영': '김상정',
    '05김요안나': '김상정',
    '05김민주': '김상정',
    '05진가영': '김상정',
    '04최정우': '김상정',
    '04이민정': '김상정',
    '04정채민': '김상정',
    '04유준상': '김상정',
    '03김종명': '김상정',
    '03임현균': '김상정',
    '01김수정': '김상정',
    '01황민서': '김상정',
    '01한호진': '김상정',
    '01임우균': '김상정',
    '01김민경': '김상정',
    '00정예찬': '김상정',
    '99권오석': '김상정',
    '98김용훈': '김상정',
    '97백수연': '김상정',
    '96김수민': '김상정',
    '95박새미': '김상정',
    '95이유빈': '김상정',
    '95조정연': '김상정',
    '95김지현': '김상정',
    '91김성효': '김상정',
    '97박유섭': '박유섭',
    '01임재형': '박유섭',
    '05황준오': '박유섭',
    '05김찬희': '박유섭',
    '04이태현': '박유섭',
    '04김민호': '박유섭',
    '04이용찬': '박유섭',
    '03한재민': '박유섭',
    '03박세준': '박유섭',
    '02김상겸': '박유섭',
    '01장석진': '박유섭',
    '00이민구': '박유섭',
    '00최윤서': '박유섭',
    '99남윤태': '박유섭',
    '98서지영': '박유섭',
    '98김태훈': '박유섭',
    '99정서호': '박유섭',
    '96문혜림': '박유섭',
    '95이효진': '박유섭',
    '94유재희': '박유섭',
    '93조현진': '박유섭',
    '87이상원': '박유섭',
    '92김형우': '김형우',
    '01임서연': '김형우',
    '05이유담': '김형우',
    '05이서연': '김형우',
    '04윤정아': '김형우',
    '04박서연': '김형우',
    '02안용호': '김형우',
    '03권영훈': '김형우',
    '01김현근': '김형우',
    '01전유진': '김형우',
    '01주다연': '김형우',
    '99김령희': '김형우',
    '99이승원': '김형우',
    '99이동환': '김형우',
    '99이지운': '김형우',
    '98전혜원': '김형우',
    '98조소정': '김형우',
    '94이수정': '김형우',
    '94유재영': '김형우',
    '93유재철': '김형우',
    '89한재석': '김형우',
    '98박상원': '박상원',
    '99김하민': '박상원',
    '05이재경': '박상원',
    '05조성준': '박상원',
    '04이정원': '박상원',
    '04박세인': '박상원',
    '02정의진': '박상원',
    '01최하은': '박상원',
    '01유대규': '박상원',
    '01김성민': '박상원',
    '01윤세훈': '박상원',
    '00류혜영': '박상원',
    '99양안현': '박상원',
    '98고주희': '박상원',
    '98이현영': '박상원',
    '97박지혜': '박상원',
    '92안재민': '박상원',
    '94박성영': '박상원',
    '92최동욱': '박상원',
    '90정수진': '박상원',
    '01김진명': '김진명',
    '98임다연': '김진명',
    '05김수환': '김진명',
    '05안홍주': '김진명',
    '05신서현': '김진명',
    '05오예린': '김진명',
    '03이지훈': '김진명',
    '03윤성욱': '김진명',
    '02정재민': '김진명',
    '99송채은': '김진명',
    '98진예란': '김진명',
    '96유재현': '김진명',
    '94홍지선': '김진명',
    '92이동건': '김진명',
    '03이두현': '김진명',
    '98김상원': '김진명',
    '98김성구': '김진명',
    '97박수인': '김진명',
    '98정서현': '김진명',
    '98장건희': '김진명',
    '00김예지': '김예지',
    '97김지우': '김예지',
    '05김동주': '김예지',
    '05이지우': '김예지',
    '05김주연': '김예지',
    '05김혜원': '김예지',
    '04김완우': '김예지',
    '04이소정': '김예지',
    '04이민영': '김예지',
    '02박주원': '김예지',
    '01김성경': '김예지',
    '99김주희': '김예지',
    '99이창현': '김예지',
    '99유정연': '김예지',
    '98심어진': '김예지',
    '98김효경': '김예지',
    '97정서윤': '김예지',
    '97이승은': '김예지',
    '97김예은': '김예지',
    '97이정민': '김예지',
    '96조한동': '김예지',
    '94문호승': '김예지',
    '95이현신': '김예지',
    '01김다빈': '김다빈',
    '03김지윤': '김다빈',
    '05백현우': '김다빈',
    '05김영현': '김다빈',
    '05박해원': '김다빈',
    '05채은서': '김다빈',
    '05임혜수': '김다빈',
    '04박세영': '김다빈',
    '04김윤주': '김다빈',
    '04조민욱': '김다빈',
    '04하성민': '김다빈',
    '04김지효': '김다빈',
    '00정영욱': '김다빈',
    '00박현우': '김다빈',
    '00허승민': '김다빈',
    '00민유선': '김다빈',
    '99문창현': '김다빈',
    '99신재욱': '김다빈',
    '99박현지': '김다빈',
    '00박채연': '김다빈',
    '97강현지': '김다빈',
    '94임정빈': '김다빈',
    '93이재윤': '김다빈',
    '93이지후': '김다빈',
    '97이주영': '김다빈',
    '98이주윤': '김다빈',
    '03권혁서': '권혁서',
    '98이유진': '권혁서',
    '05이채원': '권혁서',
    '05김소영': '권혁서',
    '05조아라': '권혁서',
    '05남해인': '권혁서',
    '05나윤서': '권혁서',
    '04전유리': '권혁서',
    '04김소정': '권혁서',
    '03남성진': '권혁서',
    '03곽성민': '권혁서',
    '01김지우': '권혁서',
    '01안하연': '권혁서',
    '99김정래': '권혁서',
    '00유승완': '권혁서',
    '98이주화': '권혁서',
    '98박태웅': '권혁서',
    '97송혜수': '권혁서',
    '97고주은': '권혁서',
    '93조유나': '권혁서',
    '90최은지': '권혁서',
    '86최범규': '권혁서',
    '90최우빈': '최우빈',
    '01한예은': '최우빈',
    '05신현빈': '최우빈',
    '05윤서진': '최우빈',
    '05박준영': '최우빈',
    '04안예원': '최우빈',
    '04송현수': '최우빈',
    '03김동균': '최우빈',
    '02정다빈': '최우빈',
    '03김지성': '최우빈',
    '01윤여정': '최우빈',
    '00윤지호': '최우빈',
    '98박원우': '최우빈',
    '98허유진': '최우빈',
    '97김준회': '최우빈',
    '97전동훈': '최우빈',
    '96백원우': '최우빈',
    '96류현우': '최우빈',
    '95이현식': '최우빈',
    '93전현우': '최우빈'
}

st.title("⛪ Pistis GPT")
st.subheader("❤️ 올해 나의 순은 어디?")
st.caption("Made By Syngha Han")

typewriter("🤖 태어난 연도와 이름을 입력해주세요!",8)
typewriter("🤖 ex) 03홍길동",8)

if prompt := st.chat_input():
    prompt = prompt.replace(' ','')

    try:
        int(prompt[:2])

    except ValueError:
        typewriter("🤖 아래와 같이 입력해 보세요",8)
        typewriter("🤖 00" + prompt,8)
    else:    
        if prompt in db:
            typewriter("🤖 올해 당신은" + db[prompt] + "순 입니다!",8)
            for names in db:
                if db[names] == db[prompt]:
                    typewriter(names[2:] + "["+ names[:2] + "]",8)
        else:
            typewriter("🤖 등록되지 않은 청년입니다😭",8)
            typewriter("🤖 누락되었을 경우 목사님 혹은 임원들께 문의해주세요!",8)
            typewriter("🤖 회장: 김정근 (📳010-5239-5267)",8)
            typewriter("🤖 존재하는 등록 신자",8)

            checkpoint = True
            for age in range (0,9):
                if "0" + str(age) + prompt[2:] in db:
                    typewriter("🤖 " + prompt[2:] + "(0"+ str(age) + ")",8)
                    checkpoint = False
            for age in range (10,99):
                if str(age) + prompt[2:] in db:
                    typewriter("🤖 " + prompt[2:] + "("+ str(age) + ")",8)
                    checkpoint = False

            if checkpoint:
                typewriter("🤖 없음",8)