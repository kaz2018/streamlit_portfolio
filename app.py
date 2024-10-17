import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("my streamlit app")

#----------------------------------
st.header('lesson 5 : add line plots')

data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'revenue': [100, 120, 180, 140, 200, 210],
    'profit': [20, 25, 50, 40, 50, 55]
}
df = pd.DataFrame(data)

st.write('sample data')
st.dataframe(df)


fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['month'],
        y=df['revenue'],
        mode='lines+markers',
        name='revenue'
    )
)
fig.add_trace(
    go.Scatter(
        x=df['month'],
        y=df['profit'],
        mode='lines+markers',
        name='profit'
    )
)
fig.update_layout(
    title='revenue and profit',
    xaxis_title='month',
    yaxis_title='amount'
)
st.plotly_chart(fig)



fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df['month'],
        y=df['revenue'],
        mode='lines+markers',
        name='revenue',
        line=dict(color='blue', width=2)
    )
)
fig.add_trace(
    go.Scatter(
        x=df['month'],
        y=df['profit'],
        mode='lines+markers',
        name='profit',
        line=dict(color='red', width=2)
    )
)
fig.update_layout(
    title='revenue and profit',
    xaxis_title='month',
    yaxis_title='amount',
    font=dict(family='Meirio', size=12),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    ),
    hovermode='x unified'
)
fig.update_xaxes(tickangle=45)
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='lightgray')
st.plotly_chart(fig)


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
