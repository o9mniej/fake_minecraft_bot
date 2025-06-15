import re
import minescript
from minescript import schedule_tick_tasks, execute

# 1. List the Minecraft usernames of your friends here
friends = ["Djslawo", "Dorito17", "Real_PretzelPal"]

# 2. Patterns for full and 2‑coord commands
pat3 = re.compile(r"!goto\s+(-?\d+)\s+(-?\d+)\s+(-?\d+)")
pat2 = re.compile(r"!goto\s+(-?\d+)\s+(-?\d+)$")

def on_tick():
    for evt in minescript.chat_events():
        name = evt['sender']         # sender’s Minecraft name
        msg = evt['message'].strip()

        if name not in friends:
            continue  # ignore non-friends

        m3 = pat3.match(msg)
        if m3:
            x, y, z = m3.groups()
            execute(f"#goto {x} {y} {z}")
        else:
            m2 = pat2.match(msg)
            if m2:
                x, z = m2.groups()
                execute(f"#goto {x} {z}")

schedule_tick_tasks(on_tick)
