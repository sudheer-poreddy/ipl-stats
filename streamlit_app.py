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
def dream11():
    st.success('you have selected dream11')

st.sidebar.button("Tourney Stats", use_container_width=True)
st.sidebar.button("Match stats", use_container_width=True)
st.sidebar.button("Player Stats", use_container_width=True)
st.sidebar.button("Dream11", on_click= dream11, use_container_width=True)

def dream11():
    st.success('you have selected dream11')
