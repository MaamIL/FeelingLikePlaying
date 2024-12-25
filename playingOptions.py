import streamlit as st
import random
import gameselect as gm

game_list = gm.game_list



def send_to_option(selected_option):
    """
    according to game selection mode- open the options for selecting the game
    """
    st.divider()
    if selected_option == 0: #Select from the game list
        game_selection = st.selectbox("Select game from list:",game_list )
        st.write(game_selection)
        with st.expander("Game Details"):
            display_game_details(game_selection)
        col1_but, col2_but = st.columns(2)
        with col2_but:
            take_me_to_game_button = st.button("Start Playing", on_click=start_game, args=(game_selection,))

    elif selected_option == 1: # Free text
        game_desc = st.text_area("Describe what you feel like playing:", placeholder="e.g., 'I want a quick game where I can play against the computer and involves guessing'")
        # st.write(game_desc)
        if st.button("Suggest Game"):
            with st.spinner("Thinking..."):
                ft_suggest_game(game_desc)

    elif selected_option == 2: # questionnaire
        st.write("Anser following questions to match the game you feel like playing:")
        game_desc_q = game_questioneere()
        # st.write(game_desc_q)
        if st.button("Suggest Game"):
            with st.spinner("Thinking..."):
                ft_suggest_game(game_desc_q)

    elif selected_option == 3: # Surprise me!        
        ind = random.randrange(len(game_list))
        # Convert dictionary keys to a list
        game_keys = list(game_list.keys())
        # Access the key at index 3
        surprise_game = game_keys[ind]
        # print(surprise_game)
        st.write(surprise_game)
        with st.expander("Game Details"):
            display_game_details(surprise_game)
        col1_but, col2_but = st.columns(2)
        with col2_but:
            start_surpise = st.button("Start Playing", on_click=start_game, args=(surprise_game,))


def start_game(game_name):
    st.write(game_name)
    if game_name == "Memmory Game":
        import memmory_game.memmoryGame as mg
        mg.rungame()
    elif game_name == "Guess the Number":
        import GuessingGame.game as gtn
        gtn.main()
    # elif game_name == "Point Color Detect":
    #     import ColorDetect.color_detect as cd
    #     cd.main()
    elif game_name == "Hangman":
        import hangman.FinalGame as hm
        hm.main()
    elif game_name == "Tic-Tac-Toe":
        import TicTacToe_tkinter.game as ttt
        ttt.main()
    elif game_name == "Rock, Paper, Scissors":
        import paper_rock_scissors.game as rps
        rps.main()
    # elif game_name == "Chutes N Ladders":
    #     import chutesNladders.chutesNladdersGame as cnl
    #     cnl.main()

def display_game_details(game):
    """
    display game details in col1 and game image in col2
    """
    col1_game, col2_game = st.columns(2)
    with col1_game:
        st.text(game_list[game]["text"])
    with col2_game:
        # Display image if available. if not- <game> image text
        try:
            st.image(game_list[game]["image"], caption=game if game else "Game image")
        except:
            st.text(f"#broken {game} image")

def ft_suggest_game(description):
    """
    suggest game upon user description free text similarity
    """
    if description.strip():
        # Find the best matching game
        game_ai = gm.GameSelector(game_list)
        best_match_game, similarity_score = game_ai.find_best_match(description)
                    # Display results
        st.success(f"📌 Best Match: {best_match_game}")
        st.write(f"Similarity Score: {similarity_score:.2%}")
        
        # Display additional game details
        game_details = game_list[best_match_game]
        
        # Expander for more game information
        with st.expander("Game Details"):
            display_game_details(best_match_game)
                            
        # Option to launch the game
        st.write("Ready to play?")
        take_me_to_suggestedgame_button = st.button(f"Launch {best_match_game}", on_click=start_game, args=(best_match_game,))
        # if st.button(f"Launch {best_match_game}"):            
        #     # st.info(f"Launching {best_match_game}...")
        #     print(best_match_game)
        #     start_game(best_match_game)
        #     print(best_match_game)
    else:
        st.warning("Please enter a description of the game you want to play.")

def game_questioneere():
    """
    render the query according to questionere answers
    """
    w1 = st.radio("How many players?", ["1 player", "2 players"])
    w2 = st.radio("Type of game:", ["Logic", "Classic", "Cards"])
    w3 = st.radio("Duration of game:", ["Fast", "Not too long", "Long"])
    w4 = st.radio("Subject of game:", ["Words", "Numbers", "Colors", "Other"])
    
    return w1 + ", "  + w2  + ", " + w3  + ", " + w4 
            
    
    
