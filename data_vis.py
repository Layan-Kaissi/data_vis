# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


st.set_page_config(layout="wide")  
st.title('Plotly Data Visualizations')
st.header('Welcome to our collection of plotly visualizations!')
st.subheader("Stock")
st.caption("A plot of the Apple Stock from 2015 to 2022, showing the Open, High, Low, and Close values")
df1 = pd.read_csv('appl.csv')

with st.expander("APPL Data"):
            st.write(df1)
    
hovertext=[]
for i in range(len(df1['Open'])):
    hovertext.append('Open: '+str(df1['Open'][i])+'<br>Close: '+str(df1['Close'][i]))
    
fig1 = go.Figure(data=go.Ohlc(x=df1['Date'],
                open=df1['Open'],
                high=df1['High'],
                low=df1['Low'],
                close=df1['Close'],
                text=hovertext,
                hoverinfo='text', increasing_line_color= 'cyan', decreasing_line_color= 'red'))
fig1.update_layout(
    title='AAPL Stock from 2015 to 2022',
    yaxis_title='AAPL Stock',
    shapes = [dict(
        x0='2015-31-08', x1='2015-31-08', y0=0, y1=1, xref='x', yref='paper',
        line_width=2)],
    annotations=[dict(
        x='2015-31-08', y=0.05, xref='x', yref='paper',
        showarrow=False, xanchor='left', text='Increase Period Begins')]
)
fig1.update_layout(
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="black"
)
fig1.update_layout(xaxis=dict(showgrid=False, zeroline=True, linecolor='black'),
                  yaxis=dict(showgrid=True, zeroline=True, linecolor='black'))

st.plotly_chart(fig1)
st.subheader("Korea Demographics")
st.caption("The graph shows the rates of marriage, divorce, birth and death in all of Korea's Regions from 2000 to 2022")
st.caption('Choose a Region in order to explore the changes in its demographic rates over the years')
df2 = pd.read_csv('korea demo.csv')
with st.expander("Korean Demographics Data"):
            st.write(df2)
region_list = df2["Region"].unique()
options = st.selectbox('Choose a Region',
    region_list)
df2 = df2[df2['Region'] == options]
fig3 = px.line(df2, x='Date', y='Birth_rate', color="Region", title="Demographics From 2000 to 2022")
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['Death_rate'],
                    mode='lines',
                    name='death rate', opacity=0.5))
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['Marriage_rate'],
                    mode='lines',
                    name='marriage rate', opacity=0.5))
fig3.add_trace(go.Scatter(x=df2['Date'], y=df2['Divorce_rate'],
                    mode='lines',
                    name='divorce rate', opacity=0.5))
fig3.update_layout(xaxis=dict(showgrid=False, zeroline=True, linecolor='black'),
                  yaxis=dict(showgrid=True, zeroline=True, linecolor='black'))

fig3.update_layout(
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="black"
)
st.write(fig3)
st.subheader("CO2 Emission")
st.caption("The scatter plot represents the co2 emission of all countries in 2019")
st.caption("Choose one or more regions to explore the amount of CO2 emitted by each country in 2019")
df4 = pd.read_csv('co2.csv')
with st.expander("CO2 Emission Data"):
            st.write(df4)
options = st.multiselect(
    'Choose a Region',
    ['Latin America & Caribbean', 'South Asia', 'Sub-Saharan Africa', 'Europe & Central Asia', 'Middle East & North Africa', 'East Asia & Pacific', 
     'North America'], ['Middle East & North Africa'])
df4 = df4[df4['Region'].isin(options)]
fig4 = px.scatter(df4,
    x='Country Name',
    y='2019', color=df4['Region'],  
labels={
                     "Country Name" : "Country Name",
                     "2019" : "2019",
                     
                 },
                title="CO2 Emission in 2019")
  
fig4.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
fig4.update_layout(xaxis=dict(showgrid=True, zeroline=True, linecolor='black'),
                  yaxis=dict(showgrid=True, zeroline=True, linecolor='black'))
 
fig4.update_layout(
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="black"
)
st.write(fig4)  
st.subheader("Honey Production in the US")

df5 = pd.read_csv('honey.csv')
with st.expander("Honey Production Data"):
            st.write(df5)
st.caption("The animation shows the total production and production value of Honey from 1998 to 2012 in each state in the US")
fig6 = px.scatter(df5, x="totalprod", y="prodvalue", animation_frame="year", animation_group="prodvalue",
           size="totalprod", color="state", hover_name="state",title="Honey Production")
fig6.update_layout(
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="black"
)
fig6.update_layout(xaxis=dict(showgrid=True, zeroline=True, linecolor='black'),
                  yaxis=dict(showgrid=True, zeroline=True, linecolor='black'))

st.plotly_chart(fig6)
st.caption("The below scatter plot and bar plot show the Total production of Honey in each state from 1998 to 2012")

fig7 = px.scatter(df5,
    x='state',
    y='totalprod',color_discrete_sequence = ['blue'],
    labels={
                     'totalprod' : "Total Production",
                     'state' : "State Code",
                     
                 }, 
                title="Honey Production"
    )

  

fig7.update_layout(
    updatemenus=[
        dict(buttons=list([
            dict(
                args=["type", "scatter"],
                label="Scatter Plot",
                method="restyle"
            ),
            dict(
                args=["type", "bar"],
                label="Bar Chart",
                method="restyle"
            )
        ]), 
            direction="down",
        ),
    ]
)
fig7.update_layout(
    font_family="Courier New",
    font_color="black",
    title_font_family="Times New Roman",
    title_font_color="black"
)
fig7.update_layout(xaxis=dict(showgrid=True, zeroline=True, linecolor='black'),
                  yaxis=dict(showgrid=True, zeroline=True, linecolor='black'))

st.plotly_chart(fig7)

st.subheader('Thank you for visiting our webpage!')
