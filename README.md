# Possession — Interactive Systems Project  
**By:** Jose Miguel Lopez & Juan Sebastian Garizao  

## Project Description  
This project is a text-based adventure game inspired by Zork-like interactive fiction, created as part of the Interactive Systems course. The main objective was to design a branching narrative with immersive audio feedback using OpenAL.  

In the game, the player explores an eerie old house where a possessed individual waits in the basement. Each decision taken while exploring different rooms changes the final outcome of the confrontation.  

The system integrates:  
- Branching narrative with Nodes and Choices.  
- Inventory system for collecting and using items (knife, holy water, ritual notes, etc.).  
- Flags system to track story progress (e.g., whether the player read the letter or found the ritual notes).  
- Spatial and ambient audio: every room has its own looping atmosphere, and actions trigger one-shot sound effects.  
- Multiple endings depending on preparation and items collected.  

## Technologies Used  
- Python 3.10+  
- OpenAL (via pyopenal) for 3D audio and sound spatialization.  
- Object-Oriented Programming for modularity:  
  - `Inventory` → manages player items.  
  - `Choice` → defines decisions, requirements, and effects.  
  - `Node` → represents story scenes.  
  - `AudioManager` → handles ambient loops and sound effects.  
Instructions to run this project locally.

## Setup

### 1. Create & activate a virtual environment

**On macOS / Linux**
```bash
python -m venv venv
source venv/bin/activate
```

**On Windows (Command Prompt)**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the project

```bash
python src/main.py
```

## Deactivate virtual environment
When you're done:
```bash
venv\Scripts\deactivate
```

## Gameplay  
- Start in the foyer of the haunted house.  
- Explore the living room, kitchen, attic, and basement to gather tools and knowledge.  
- Each action plays a contextual sound effect (door creaks, key pickup, chants, etc.).  
- Rooms have ambient looping audio (basement drips, attic wind, demonic whispers).  
- The final confrontation (Node 8) has different endings depending on inventory:  
  - Use holy water → exorcism success (good ending).  
  - Use ritual notes → binding (neutral ending).  
  - Use knife → violent resolution (bad ending).  
  - Enter unprepared → possession (worst ending).  

### Ambient Loops  
- Foyer → `foyer.wav`  
- Living Room → `livingRoomLoop.wav`  
- Kitchen → `kitchen.wav`  
- Stair Landing → `stair_creak_loop.wav`  
- Attic → `attic_wind_loop.wav`  
- Basement Corridor → `basement_drip_loop.wav`  
- Threshold → `chains.wav`  
- Confrontation → `demonic_whisper_loop.wav`  

### Effect Sounds  
- Key pickup → `key_pickup.wav`  
- Letter found → `letter.wav`  
- Reading letter/book → `page_rustle.wav`, `page_rustle2.wav`  
- Stairs movement → `stairs.wav`  
- Knife pickup → `knife_pickup.wav`  
- Unlock cabinet → `lock_open.wav`  
- Search shelves/drawers → `shelf_clatter.wav`  
- Open trunk with knife → `tape_cut.wav`  
- Force trunk → `wood_snap.wav`  
- Basement approach (voices) → `mumbles.wav`  
- Exorcism (holy water) → `holy_splash.wav`  
- Ritual chant → `ritualChant.wav`  
- Knife fight → `knife_swipe.wav`  
- Burst in unprepared → `fightScream.wav`  
- Final confrontation → `fightScream.wav` or `scream.wav`  

### Ending Effects  
- Exorcism success → `goodEnding.wav` + `holy_scream.wav`  
- Ritual success → `ritualChant.wav`  
- Violence → `badEnding.wav` + `demon_roar.wav`  
- Unprepared → `badEnding.wav`  