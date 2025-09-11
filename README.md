Possession — Interactive Systems Project

By: Jose Miguel Lopez & Juan Sebastian Garizao

Project Description

This project is a text-based adventure game inspired by Zork-like interactive fiction, created as part of the Interactive Systems course. The main objective was to design a branching narrative with immersive audio feedback using OpenAL.

In the game, the player explores an eerie old house where a possessed individual waits in the basement. Each decision taken while exploring different rooms changes the final outcome of the confrontation.

The system integrates:

Branching narrative with Nodes and Choices.

Inventory system for collecting and using items (knife, holy water, ritual notes, etc.).

Flags system to track story progress (e.g., whether the player read the letter or found the ritual notes).

Spatial and ambient audio: every room has its own looping atmosphere, and actions trigger one-shot sound effects.

Multiple endings depending on preparation and items collected.

⚙️ Technologies Used

Python 3.10+

OpenAL (via pyopenal) for 3D audio and sound spatialization.

Object-Oriented Programming for modularity:

Inventory → manages player items.

Choice → defines decisions, requirements, and effects.

Node → represents story scenes.

AudioManager → handles ambient loops and sound effects.

📖 Gameplay

Start in the foyer of the haunted house.

Explore the living room, kitchen, attic, and basement to gather tools and knowledge.

Each action plays a contextual sound effect (door creaks, key pickup, chants, etc.).

Rooms have ambient looping audio (basement drips, attic wind, demonic whispers).

The final confrontation (Node 8) has different endings depending on inventory:

Use holy water → exorcism success (good ending).

Use ritual notes → binding (neutral ending).

Use knife → violent resolution (bad ending).

Enter unprepared → possession (worst ending).

🔊 Audio Design

The audio layer was central to this project.

Ambient loops:

Foyer → creak_loop.wav

Living Room → room_hum_loop.wav

Kitchen → fridge_hum_loop.wav

Attic → attic_wind_loop.wav

Basement → basement_drip_loop.wav

Threshold → hum_build_loop.wav

Confrontation → demonic_whisper_loop.wav

Effect sounds:

Key pickup → key_pickup.wav

Letter rustle → paper_rustle.wav

Book pages → page_rustle.wav

Knife pickup → knife_pickup.wav

Cabinet unlock → lock_open.wav

Drawer rummage → drawer_rummage.wav

Trunk tape cut → tape_cut.wav

Ritual chant → chant.wav

Holy water splash → holy_splash.wav

Door bang → door_bang.wav

Demon scream → scream.wav
