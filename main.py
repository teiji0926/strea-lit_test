import streamlit as st
import pandas as pd

# 例の社員データフレーム (サンプルデータ)
employee_data = {
    '社員番号': ['100001', '100002', '100003'],
    '名前': ['花子さん', '太郎さん', '次郎さん'],
    'EX': ['〇', '×', '×'],
    'e-5489': ['×', '〇', '〇'],
    'えきねっと': ['×', '×', '〇']
}
df = pd.DataFrame(employee_data)

# ①社員番号の入力画面
st.title('社員情報検索システム')
st.markdown('<p style="font-size:18px;">社員番号を入力してください</p>', unsafe_allow_html=True)

# ユーザーに社員番号を入力させる
employee_id = st.text_input('社員番号')

# ②エンターボタン
if st.button('検索'):
    # ③エンターボタンが押された後の処理
    if employee_id in df['社員番号'].values:
        # 社員情報を取得して表示し、インデックスをリセットして表示しないようにする
        employee_info = df[df['社員番号'] == employee_id].reset_index(drop=True)
        
        st.markdown('<h3>カード保有情報:</h3>', unsafe_allow_html=True)
        
        # 名前とカード情報をスタイリッシュに表示
        st.markdown(f"""
            <div style="background-color: #f0f0f5; padding: 10px; border-radius: 10px;">
                <p><strong>名前:</strong> {employee_info['名前'].values[0]}</p>
                <p><strong>EX:</strong> {employee_info['EX'].values[0]}</p>
                <p><strong>e-5489:</strong> {employee_info['e-5489'].values[0]}</p>
                <p><strong>えきねっと:</strong> {employee_info['えきねっと'].values[0]}</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.write('該当する社員番号が見つかりません。')
