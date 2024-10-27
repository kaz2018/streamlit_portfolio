import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import time

st.title("my streamlit app")

#----------------------------------
st.header('lesson 11: sliders and checkboxs')

sld = st.slider(
    'test: ',
    min_value=1,
    max_value=10,
    value=(3, 7),
    key='test1'
)
st.write(sld)

sample_size = st.slider(
    'select sample size: ',
    min_value=10,
    max_value=1000,
    value=100,
    step=10,
    key='sample_slider'
    )

data_sample1 = pd.DataFrame(np.random.randn(sample_size, 2), columns=['X', 'Y'])

fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=data_sample1['X'],
    y=data_sample1['Y'],
    mode='markers'
    ))
st.plotly_chart(fig1)


data_sample2 = pd.DataFrame(np.random.uniform(0, 100, size=(1000, 2)), columns=['P' ,'Q'])

range_values = st.slider(
    'select range: ',
    min_value=0.0,
    max_value=100.0,
    value=(25.0, 75.0),
    key='range_slider'
    )

filtered_data = data_sample2[
    (data_sample2['P'] >= range_values[0])
    & (data_sample2['P'] <= range_values[1])
    ]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(
    x=filtered_data['P'],
    y=filtered_data['Q'],
    mode='markers')
    )
st.plotly_chart(fig2)


data_sample3 = pd.DataFrame(np.random.randn(200, 2), columns=('M', 'N'))

color_option = st.selectbox('select marker color: ', ['blue', 'red', 'green', 'purple'], key='color_select')

fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=data_sample3['M'],
    y=data_sample3['N'],
    mode='markers',
    marker=dict(color=color_option)
    ))
st.plotly_chart(fig3)



columns_to_plot = st.multiselect(
    'select clumns to plot: ',
    ['A', 'B', 'C', 'D'],
    default=['A', 'B'],
    key='column_multiselect'
)

num_points = st.slider(
    'number of data points: ',
    min_value=50,
    max_value=1000,
    value=200,
    step=50,
    key='points_slider'
)

data_sample4 = pd.DataFrame(np.random.randn(num_points, 4), columns=['A', 'B', 'C', 'D'])

fig4 = go.Figure()
for col in columns_to_plot:
    fig4.add_trace(go.Scatter(
        x=data_sample4.index,
        y=data_sample4[col],
        mode='lines+markers',
        name=col
    ))

st.plotly_chart(fig4)




#----------------------------------
st.header('lesson 10 : buttons & checkboxes')
if st.button('generate data', key='generate_data'):
    random_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
    st.write(random_data)

show_chart = st.checkbox('display chart', key='show_chart')

if show_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['X', 'Y', 'Z'])
    fig = go.Figure()
    for column in chart_data.columns:
        fig.add_trace(go.Scatter(x=chart_data.index, y=chart_data[column], mode='lines', name=column))
    st.plotly_chart(fig)



if 'counter' not in st.session_state:
    st.session_state.counter = 0

col1, col2, col3 = st.columns(3)

if col1.button('count up', key='count_up'):
    st.session_state.counter += 1
if col2.button('count down', key='count_down'):
    st.session_state.counter -= 1
if col3.button('reset', key='reset_count'):
    st.session_state.counter = 0

st.write(f'current count: {st.session_state.counter}')



#----------------------------------
st.header('lesson 9 : managing session')
if 'count' not in st.session_state:
    st.session_state.count = 0

st.write(f'current count : {st.session_state.count}')

if st.button('count up'):
    st.session_state.count += 1
    st.rerun()

if 'user_name' not in st.session_state:
    st.session_state.user_name = ''
if 'user_email' not in st.session_state:
    st.session_state.user_email = ''

user_name = st.text_input('user name', value=st.session_state.user_name, key='tmp_user_name')
user_email = st.text_input('email address', value=st.session_state.user_email, key='tmp_email')

if st.button('save user info'):
    st.session_state.user_name = user_name
    st.session_state.user_email = user_email
    st.success('saved')

st.write(f'saved user name: {st.session_state.user_name}')
st.write(f'saved email address: {st.session_state.user_email}')

# manage session of dataframe
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['product', 'price'])

product = st.text_input('product name', key='tmp_product_name')
price = st.number_input('price', min_value=0, key='tmp_price')

if st.button('add product'):
    new_data = pd.DataFrame({
        'product': [product],
        'price' : [price]
    })
    st.session_state.df = pd.concat([st.session_state.df, new_data],
                                    ignore_index=True)

st.write('products')
st.write(st.session_state.df)

if st.button('reset data'):
    st.session_state.df = pd.DataFrame(columns=['product', 'price'])
    st.rerun()



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

name = st.text_input('enter your name', key='tmp_name')
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
