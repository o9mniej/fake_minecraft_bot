import minescript
from minescript import EventQueue, EventType
import re

# Define the pattern to match chat messages
pattern = re.compile(r"\b.*!ask\b", re.IGNORECASE)

# Define a list of authorized friends
authorized_friends = {"Djslawo", "Dorito17", "Real_PretzelPal"}  # Replace with your friends' usernames

def main():
    # Notify that the chat listener is active
    minescript.echo("🟢 Chat listener active — watching for '!ask' in messages…")

    # Create an event queue to handle events
    with EventQueue() as q:
        # Register the chat listener
        q.register_chat_listener()

        while True:
            # Retrieve the next event from the queue
            event = q.get()

            # Check if the event is a chat message
            if event.type == EventType.CHAT:
                # Extract the message and sender
                text = getattr(event, "message", "")
                sender = getattr(event, "username", "")  # assuming 'username' contains the sender's name

                # Ensure the message is a string and matches the pattern
                if isinstance(text, str) and pattern.search(text):
                    if sender in authorized_friends:
                        minescript.echo(f"✅ Matched message from {sender}")
                        minescript.chat("thinking...")
                    else:
                        minescript.chat('{error: "unauthorized access"}')

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
