import streamlit as st
import  numpy as np
import pandas as pd
from PIL import Image
import time

#タイトルの追加
st.title('Streamlit入門')

#テキストの追加
st.write('DataFrame')

df = pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns=['lat','lon'])

st.write(df)
#↑と機能的に近いが、↓は引数で表のサイズを変更できる highloghtはpandasの昨日
st.dataframe(df.style.highlight_max(axis=0),width=500,height=100)
#↓静的な表を作るとき
st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```
import streamlit as st
import  numpy as np
import pandas as pd
```

"""

#画像費用時
#折れ線グラフ
st.line_chart(df)

#エリアグラフ
st.area_chart(df)

#棒グラフ
st.bar_chart(df)

#地図へ
st.map(df)

#画像表示
st.write('Display Image')
img = Image.open(r'C:\Users\teiji\OneDrive\Desktop\kuji.jpg')
#caption=guide use_column_widthは画面サイズの件
st.image(img,caption='kuji',use_column_width=True)

#チェックボックスの画像費用時

if st.checkbox('Show Image'):
    img = Image.open(r'C:\Users\teiji\OneDrive\Desktop\kuji.jpg')
    #caption=guide use_column_widthは画面サイズの件
    st.image(img,caption='kuji',use_column_width=True)

#セレクトボックス作成
option = st.selectbox(
    'あなたがすきなもの',
    list(range(1,11))
)

'あなたの好きな数字は',option,'です'

#テキストボックス作成
st.write('Interactive wijets')
text = st.sidebar.text_input('ご趣味は？')
'あなたの趣味は',text,'です'

# #スライダー
# condition = st.slider('あなたの今の調子は？',0,100,5)
# 'あなたの調子は',condition,'です'

# #サイドバーバージョン
# #テキストボックス作成
# text = st.sidebar.text_input('ご趣味は？')
# 'あなたの趣味は',text,'です'

#スライダー
condition = st.sidebar.slider('あなたの今の調子は？',0,100,5)
'あなたの調子は',condition,'です'

#カラム制
left_column,right_column = st.columns(2)
button = left_column.button('右に文字を表示')
if button:
    right_column.write('右カラム')

#FAQでよく使うやつ
expander = st.expander('問い合わせ')
expander.write('問い合わせ回答')
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ回答1')

st.write('プログレスバーの表示')
'''Start'''
latest_iteration = st.empty()
for x in range(100):
    latest_iteration.text(f'Iteration {x+1} %')
    time.sleep(0.2)
'''Done'''