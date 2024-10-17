import streamlit as st

st.title("my streamlit app")
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
