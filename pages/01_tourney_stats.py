import streamlit as st


def match_stats():
    st.success('Suchesssssss')


st.sidebar.button("Match stats", on_click= match_stats, use_container_width=True)

st.sidebar.selectbox('Select a player', ['Virat Kohli', 'Sachin Tendulkar', 'Rohit Sharma', "is", "john"])