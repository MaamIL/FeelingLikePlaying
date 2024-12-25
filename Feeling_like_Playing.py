import streamlit as st
import playingOptions as po

def build_window_eng():
    st.title(":game_die: Feeling like Playing :black_joker:" )
    # language = st.radio("",["Heb", "Eng"], horizontal=True)
    game_selection_mode = [":white_check_mark: Select from the game list", ":pencil2: Free text", ":grey_question: questionnaire", ":gift: Surprise me!"]
    play_options = st.radio("What do I feel like playing:", game_selection_mode)
    po.send_to_option(game_selection_mode.index(play_options))

build_window_eng()