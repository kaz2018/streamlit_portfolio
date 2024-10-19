import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

st.title("my streamlit app")

#----------------------------------
st.header('lesson 8 : cache')

def generate_large_dateset():
    data = pd.DataFrame(np.random.randn(1000000, 5), columns=['A', 'B', 'C', 'D', 'E'])
    return data

@st.cache_data
def load_data_cached():
    return generate_large_dateset()

def load_data_uncached():
    return generate_large_dateset()

st.subheader('without cache')
start_time = time.time()
data_uncached = load_data_uncached()
end_time = time.time()
st.write(f'loading time : {end_time - start_time:.2f} sec')
st.write(data_uncached.head())

st.subheader('with cache')
start_time = time.time()
data_cached = load_data_cached()
end_time = time.time()
st.write(f'loading time : {end_time - start_time:.2f} sec')
st.write(data_cached.head())

@st.cache_resource
def load_large_dataset():
    return pd.DataFrame(
                np.random.randn(1000000, 5),
                columns=['A', 'B', 'C', 'D', 'E']
    )
st.subheader('large dataset')
start_time = time.time()
large_data = load_large_dataset()
end_time = time.time()
st.write(f'loading time : {end_time - start_time:.2f} sec')
st.write(f'data shape : {large_data.shape}')
st.write(large_data.head())


@st.cache_data(ttl=10)
def get_current_time():
    return pd.Timestamp.now()

st.subheader('disable cache')
st.write('update per 10 sec')
st.write(get_current_time())



#----------------------------------
st.header('lesson 7: pie chart')
data = {
    'product' : ['A', 'B', 'C', 'D', 'E'],
    'sales' : [300, 200, 180, 150, 120]
}
df = pd.DataFrame(data)

st.write('sample : pie chart')
st.dataframe(df)

fig = go.Figure(data=go.Pie(labels=df['product'], values=df['sales']))
fig.update_layout(title='sales share by product')
st.plotly_chart(fig)


# custom
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen', 'lightcoral']

fig = go.Figure(data=[go.Pie(
                    labels=df['product'],
                    values=df['sales'],
                    hole=.3,
                    marker=dict(
                        colors=colors,
                        line=dict(color='#000000', width=2)
                    )
)])
fig.update_traces(
    textposition='inside',
    textinfo='percent+label',
    hoverinfo='label+value+percent',
    textfont_size=14
)
fig.update_layout(
    title='sales by product',
    font=dict(family='Meirio', size=12),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    annotations=[dict(text='sales', x=0.5, y=0.5, font_size=20, showarrow=False)]
)
st.plotly_chart(fig)

#----------------------------------
st.header('lesson 6 : bar chart')
data = {
    'product': ['A', 'B', 'C', 'D', 'E'],
    'sales': [300, 400, 200, 600, 500],
    'profit': [30, 60, 20, 100, 80]
}
df = pd.DataFrame(data)

st.write('sample data')
st.dataframe(df)

fig = go.Figure()
fig.add_trace(go.Bar(x=df['product'], y=df['sales'], name='sales'))
fig.add_trace(go.Bar(x=df['product'], y=df['profit'], name='profit'))

fig.update_layout(
    title='sales and profit',
    xaxis_title='product',
    yaxis_title='amount',
    barmode='group'
)
st.plotly_chart(fig)



fig = go.Figure()
fig.add_trace(go.Bar(x=df['product'], y=df['sales'], name='sales', marker_color='blue'))
fig.add_trace(go.Bar(x=df['product'], y=df['profit'], name='profit', marker_color='red'))

fig.update_layout(
    title='sales and profit',
    xaxis_title='product',
    yaxis_title='amount',
    barmode='group',
    font=dict(family='Meirio', size=12),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    hovermode='x unified'
)

# グラフに数値のラベルを表示
fig.update_traces(texttemplate='%{y}', textposition='outside')

fig.update_yaxes(range=[0, max(df['sales'].max(), df['profit'].max()) * 1.1])
st.plotly_chart(fig)


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
