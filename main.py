import streamlit as st
import pandas as pd

# ①社員番号の入力画面
st.title('社員情報検索システム')
st.subheader('社員番号を入力してください')

employee_data = {
    '社員番号': ['100001', '100002', '100003'],
    '名前': ['花子さん', '太郎さん', '次郎さん'],
    'EX': ['〇', '×', '×'],
    'e-5489': ['×', '〇', '〇'],
    'えきねっと': ['×', '×', '〇']
}
df = pd.DataFrame(employee_data)

# ユーザーに社員番号を入力させる
employee_id = st.text_input('社員番号')

# ②エンターボタン
if st.button('検索') :
    st.write('成功')
    st.table(df)
else:
    st.write('社員番号を入れて検索ボタンを押下くだせえ')
