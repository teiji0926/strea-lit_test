import streamlit as st

# ①社員番号の入力画面
st.title('社員情報検索システム')
st.subheader('社員番号を入力してください')

# ユーザーに社員番号を入力させる
employee_id = st.text_input('社員番号')

# ②エンターボタン
if st.button('検索') :
    st.write('成功')
    else:
        st.write('該当する社員番号が見つかりません。')
