import streamlit as st
import reveal_slides as rs
from utils import write_message
from agent import generate_response
from data.docs import users, slides, slide_caption
from graph import erase_messages, erase_sessions

from contextlib import redirect_stdout

# Page Config
st.set_page_config(
    page_title="ngTelco",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# Funzione per resettare la sessione
def reset_session():
    erase_sessions()
    erase_messages()
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Benvenuto! Scegli un utente per iniziare.",
        }
    ]
    st.session_state.user_selected = False
    st.session_state.selected_user = None


# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Benvenuto! Scegli un utente per iniziare.",
        },
    ]

if "user_selected" not in st.session_state:
    st.session_state.user_selected = False
if "selected_user" not in st.session_state:
    st.session_state.selected_user = None


# Funzione per confermare la selezione dell'utente
def confirm_user_selection():
    reset_session()  # Resetta la sessione quando si conferma un nuovo utente
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": f"Ciao {st.session_state.user_select.split()[0]}, sono ngTelco! Come posso aiutarti?",
        }
    ]
    st.session_state.user_selected = True
    st.session_state.selected_user = st.session_state.user_select


# Sidebar for user selection
with st.sidebar:
    st.logo(
        image="images/logo.png",
    )
    st.selectbox(
        "Seleziona un utente:",
        users,
        key="user_select",
    )
    if st.button(
        "Conferma",
        on_click=confirm_user_selection,
    ):
        pass
    st.divider()
    st.image(
        "images/graph.png",
        use_container_width=True,
        caption="Graph Schema",
    )

# Controlla se l'utente è selezionato
if not st.session_state.user_selected:
    st.markdown("# :violet-background[**ngTelco**] - Agentic RAG ***PoC***")
    currState = rs.slides(
        slides,
        theme="black",
        height=500,
        config={
            "transition": "slide",
            "width": 900,
            "height": 900,
            "center": True,
        },
    )
    if currState["indexh"] == 0:
        st.markdown(slide_caption[0])
    if currState["indexh"] == 1:
        st.markdown(slide_caption[1])
    if currState["indexh"] == 2:
        st.markdown(slide_caption[2])
    if currState["indexh"] == 3:
        st.markdown(slide_caption[3])


else:
    # Submit handler
    def handle_submit(message):
        with st.spinner("Sto pensando..."):
            context = f"User: {st.session_state.selected_user}. Message: {message}"
            response = generate_response(context)
            write_message("assistant", response)

    # Display messages in Session State
    for message in st.session_state.messages:
        write_message(message["role"], message["content"], save=False)

    # Handle any user input
    if prompt := st.chat_input("Scrivi un messaggio...."):
        write_message("user", prompt)
        handle_submit(prompt)
