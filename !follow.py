import minescript
import sys

# List of allowed friends
ALLOWED = {"Djslawo", "Dorito17", "Real_PretzelPal"}  # Add more names as needed

def on_chat_message(sender, message):
    if sender in ALLOWED and message == "!follow":
        minescript.execute(f"#follow player {sender}")
        minescript.chat(f"following {sender}")

# Register the chat listener
minescript.on_chat(on_chat_message)
