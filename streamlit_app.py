import streamlit as st

st.header("All about IPL")


st.markdown(
    """
<style>
button {
    width: 250px;
    padding-top: 15px !important;
    padding-bottom: 15px !important;
}
</style>
""",
    unsafe_allow_html=True,
)


st.sidebar.button("Tourney Stats", use_container_width=True)
st.sidebar.button("Match stats", use_container_width=True)
st.sidebar.button("Player Stats", use_container_width=True)
st.sidebar.button("Dream11", use_container_width=True)
