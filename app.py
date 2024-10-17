import streamlit as st
import pandas as pd

st.title("my streamlit app")

#----------------------------------
st.header('lesson 4 : add data')

name = st.text_input('enter your name')
if name:
    st.write(f'hello {name}')

age = st.number_input(
    'input your age',
    min_value=0,
    max_value=120,
    value=20
)
st.write(f'your age is {age}')

date = st.date_input('select date')
st.write(f'selected date is {date}')

data = {
    'name': ['taro', 'jiro', 'hanako'],
    'age': [20, 30, 40],
    'city': ['tokyo', 'osaka', 'kyoto']
}
df = pd.DataFrame(data)

st.subheader('display dataframe')
st.dataframe(df)

st.subheader('display table')
st.table(df)



#----------------------------------
st.header('lesson 3 : add texts')

st.write("normal text")
st.markdown("this is **bold** and this is *italic*")
st.latex(r'E=mc^2')
st.latex(r'\sqrt{x^2 + y^2} = z')

st.info('info')
st.warning('warning')
st.error('error')
st.success('success')

code = '''
def hello():
    print("hello streamlit")
'''
st.code(code, language='python')
