from datetime import date

import streamlit as st


def streamlit():
    st.title('N2M 데모')
    st.markdown('**Transformers Encoder-Decoder 모델을 활용한 Sequence to Sequence 문제 실습**')
    st.markdown("#### 데이터셋([Link](https://github.com/htw5295/Neural_date_translation_dataset))", unsafe_allow_html=True)
    data_info = """
- Faker 라이브러리로 생성한 날짜 표기 데이터
- 입력 : 다양한 형태의 날짜 표기 데이터
- 출력 : yyyy-mm-dd 형태의 날짜 표기 데이터
- 학습 데이터 : 24,000개
- 검증 데이터 : 3,000개
- 평가 데이터 : 3,000개
    """
    st.markdown(data_info)
    st.markdown("#### 모델")
    model_info = """
- [facebook/bart-base](https://huggingface.co/facebook/bart-base)의 Tokenizer와 Config 활용
- Huggingface의 [AutoModelForSeq2SeqLM](https://huggingface.co/docs/transformers/model_doc/auto#transformers.AutoModelForSeq2SeqLM) 모델 활용
    """
    st.markdown(model_info)
    st.markdown("#### 평가")
    eval_info = """
- 예측 데이터를 yyyy-mm-dd 형식으로 디코딩한 뒤 정답 데이터와 비교하여 일치, 불일치를 판단함
    """
    st.markdown(eval_info)


    today = date.today().strftime('%b %d %Y')
    st.subheader('Input human readable date text')
    title = st.text_input('Input date', today)

    if st.button('Translation'):
        result = '2022-07-24'

        st.subheader('Generated yyyy-mm-dd format date text')
        st.markdown(f"##### {today}　　>>>　　{result}")

streamlit()
