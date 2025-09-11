import os
import sys
from audioManager import AudioManager
from inventory import Inventory
from choice import Choice
from node import Node

def clear_screen():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")

def build_story():
    nodes = {}

    nodes[1] = Node(
        id=1,
        title="Foyer",
        description=(
            "You stand in the dim foyer of an old house. The air is cold.\n"
            "A coat rack hangs by the door, an umbrella stand leans in the corner.\n"
            "From somewhere deeper in the house you can hear a low humming."
        ),
        choices=[
            Choice("Step into the living room", target=2),
            Choice(
                "Search the coat rack",
                target=1,
                requiresFlag={"grabbed_rusty_key": False},
                effectsInv={"rusty_key": 1},
                effectsFlag={"grabbed_rusty_key": True},
                sound="src/sounds/key_pickup.wav",
            ),
            Choice(
                "Check the umbrella stand",
                target=1,
                requiresFlag={"has_letter": False},
                effectsInv={"letter": 1},
                effectsFlag={"has_letter": True},
                sound="src/sounds/letter.wav",
            ),
            Choice(
                "Read the old letter",
                target=1,
                requiresInv={"letter": 1},
                requiresFlag={"read_letter": False},
                effectsFlag={"read_letter": True},
                sound="src/sounds/page_rustle.wav",
            ),
            Choice("Leave the house", target=None),
        ],
    )

    nodes[2] = Node(
        id=2,
        title="Living room",
        description=(
            "A sagging sofa faces a shuttered window. Bookshelves line one wall — "
            "one book looks worn, as if it were read often. The wood creaks around you."
        ),
        choices=[
            Choice(
                "Read the worn book on the shelf",
                target=2,
                requiresFlag={"read_book": False},
                effectsInv={"journal": 1},
                effectsFlag={"read_book": True},
                sound="src/sounds/page_rustle.wav",
            ),
            Choice("Follow the hallway to the kitchen", target=3),
            Choice("Go up the staircase", target=4, sound="src/sounds/stairs.wav"),
            Choice("Return to the foyer", target=1),
        ],
    )

    nodes[3] = Node(
        id=3,
        title="Kitchen",
        description=(
            "The kitchen is torn apart, as if ravaged by someone, or something. There is a small knife on the counter.\n "
            "An old metal cabinet on the far wall is locked with a padlock."
        ),
        choices=[
            Choice(
                "Pick up the small knife",
                target=3,
                requiresFlag={"picked_knife": False},
                effectsInv={"knife": 1},
                effectsFlag={"picked_knife": True},
                sound="src/sounds/knife_pickup.wav",
            ),
            Choice(
                "Try to open the locked cabinet (use rusty key)",
                target=3,
                requiresInv={"rusty_key": 1},
                requiresFlag={"opened_cabinet": False},
                effectsInv={"holy_water": 1, "rusty_key": -1},
                effectsFlag={"opened_cabinet": True},
                sound="src/sounds/lock_open.wav",
            ),
            Choice("Look into the sink and drawers (nothing special)", target=3, sound="src/sounds/drawer_rummage.wav"),
            Choice("Return to the living room", target=2),
        ],
    )

    nodes[4] = Node(
        id=4,
        title="Stair landing",
        description=(
            "The staircase creaks. The hallway splits: a narrow door down to the basement, "
            "and a steep ladder leading to a cramped attic hatch."
        ),
        choices=[
            Choice("Climb up into the attic", target=5, sound="src/sounds/stairs.wav"),
            Choice("Descend to the basement", target=6, sound="src/sounds/stairs.wav"),
            Choice("Go back to the living room", target=2, sound="src/sounds/stairs.wav"),
        ],
    )

    nodes[5] = Node(
        id=5,
        title="Attic",
        description=(
            "Dust motes float in the slanting beams of light. A trunk sits in the corner, "
            "its lid sealed with brittle tape."
        ),
        choices=[
            Choice(
                "Cut open the trunk with your knife",
                target=5,
                requiresInv={"knife": 1},
                requiresFlag={"opened_trunk": False},
                effectsInv={"ritual_notes": 1},
                effectsFlag={"opened_trunk": True},
                sound="src/sounds/tape_cut.wav",
            ),
            Choice(
                "Force the trunk open with your hands",
                target=5,
                requiresFlag={"opened_trunk": False},
                effectsInv={"ritual_notes": 1},
                effectsFlag={"opened_trunk": True},
                sound="src/sounds/wood_snap.wav",
            ),
            Choice("Return to the stair landing", target=4, sound="src/sounds/stairs.wav"),
        ],
    )

    nodes[6] = Node(
        id=6,
        title="Basement corridor",
        description=(
            "Damp concrete and a single bare bulb that lights a path of blood droplets on the floor. The blood is still fresh. The humming is louder here. "
            "A heavy door at the end stands slightly open, a foul smell leaking from it."
        ),
        choices=[
            Choice("Approach the heavy door", target=7, sound="src/sounds/mumbles.wav"),
            Choice(
                "Search the storage shelves",
                target=6,
                requiresFlag={"searched_shelves": False},
                effectsInv={"moldy_rag": 1},
                effectsFlag={"searched_shelves": True},
                sound="src/sounds/shelf_clatter.wav",
            ),
            Choice("Go back upstairs", target=4, sound="src/sounds/stairs.wav"),
        ],
    )

    nodes[7] = Node(
        id=7,
        title="Threshold",
        description=(
            "The door opens into a small, sparsely furnished room. Chains hang on one wall, "
            "and on a low table are strange symbols that look like a rushed ritual. "
            "You see a figure facing the back wall, gently rocking back and forth while it mumbles to itself."
        ),
        choices=[
            Choice(
                "Sprinkle holy water and attempt an exorcism",
                target=8,
                requiresInv={"holy_water": 1},
                effectsInv={"holy_water": -1},
                effectsFlag={"used_exorcism": True},
                sound="src/sounds/whisper.wav",
            ),
            Choice(
                "Use the ritual notes you found to try to bind the thing",
                target=8,
                requiresInv={"ritual_notes": 1},
                effectsInv={"ritual_notes": -1},
                effectsFlag={"used_ritual": True},
            ),
            Choice(
                "Rush in with the knife and try to fight",
                target=8,
                requiresInv={"knife": 1},
                effectsFlag={"used_violence": True},
                sound="src/sounds/knife_swipe.wav",
            ),
            Choice(
                "Burst in unprepared",
                target=8,
                effectsFlag={"used_none": True},
                sound="src/sounds/fightScream.wav",
            ),
            Choice("Step back quietly and rethink your approach", target=6),
        ],
    )

    nodes[8] = Node(
        id=8,
        title="Confrontation",
        description=(
            "The thing locks eyes with you. It seems to have been a person at some point in the past."
            "You make your choice and face the consequences."
        ),
        choices=[
            Choice(
                "Proceed with encounter", 
                target=None,
                sound="src/sounds/scream.wav")
        ],
    )

    return nodes

NARRATION_MAP = {
    "rusty_key": "You find a rusty key in one of the coat's pockets. It feels cold and rough in your hand.",
    "letter": "You find a letter hidden away. You grab it. The paper crackles.",
    "knife": "You take the small kitchen knife. It makes you feel safe.",
    "holy_water": "The padlock snaps loose with a shriek, revealing a small vial.\nA vial of cloudy liquid hums faintly in your hands. A worn out label sticks to the front: \"Holy Water\"",
    "ritual_notes": "The trunk lid gives way and inside you find handwritten notes.\nThey seem to be instructions for a ritual.",
    "read_letter": "You read the letter. The handwriting is hurried and mentions a 'binding' in the basement.",
    "read_book": "The book's margins are full of frantic annotations and strange symbols.",
}

def make_narration_for_choice(choice, inventory, flags):
    lines = []

    for key, qty in choice.effectsInv.items():
        if qty > 0 and key in NARRATION_MAP:
            lines.append(NARRATION_MAP[key])

    for key in choice.effectsFlag.keys():
        if key in NARRATION_MAP:
            lines.append(NARRATION_MAP[key])

    if not lines:
        lines.append(f"You {choice.text}")

    return "\n".join(lines)

def main():
    nodes = build_story()
    current_node = 1
    inventory = Inventory({})
    flags = {}
    audio = AudioManager()
    running = True
    ambient_map = {
        1: "src/sounds/foyer.wav",
        2: "src/sounds/livingRoomLoop.wav",
        3: "src/sounds/kitchen.wav",
        6: "src/sounds/basement_drip_loop.wav",
        7: "src/sounds/chains.wav",
    }
    clear_screen()
    print("Possesion\nBy: Jose M. Lopez & Juan S. Garizao\nType the number of a choice and press Enter.")
    while running:
        if not isinstance(nodes, dict):
            raise RuntimeError("nodes must be a dict mapping id->Node. build_story() returned something else.")
        node = nodes[current_node]
        print(f"\n=== {node.title} ===\n")
        print(node.description + "\n")
        if node.id in ambient_map:
            try:
                audio.play_ambient(ambient_map[node.id])
            except Exception:
                pass
        if node.id == 8:
            used_exorcism = flags.get("used_exorcism", False)
            used_ritual = flags.get("used_ritual", False)
            used_violence = flags.get("used_violence", False)
            used_none = flags.get("used_none", False)
            if used_exorcism:
                audio.play_effect("src/sounds/goodEnding.wav")
                print("\nYou move carefully, whispering words as you sprinkle the holy water.\nThe room shakes, light floods, and the horrid face in front of you softens.\nThe person collapses — alive, and freed. You survived, and you saved them.")
            elif used_ritual:
                audio.play_effect("src/sounds/ritualChant.wav")
                print("\nFollowing the notes precisely, you trace the sigils and speak the binding phrases. The air convulses.\nFor a terrible second you see a giant shadow emerge from below the person.\nThe mumbling stops. The person slumps, alive but in rough shape. the possession broken but the cost evident.")
            elif used_violence:
                audio.play_effect("src/sounds/badEnding.wav")
                print("\nYou lunge with the knife. For a moment it seems to work — the creature recoils — but the blood from its wound burns you as it lands on your body.\n With a terrible shriek, it falls to the ground. Its breathing slows to a halt. You were able to subdue the creature, but killed the person it was before.")
            else:
                audio.play_effect("src/sounds/badEnding.wav")
                print("\nYou rush in empty-handed. There is no time to think. The thing is faster. It overwhelms you. Everything goes black.")
            running = False
            break
        available_choices = [c for c in node.choices if c.is_available(inventory, flags)]
        for idx, choice in enumerate(available_choices, start=1):
            print(f"{idx}. {choice.text}")
        if getattr(inventory, "equipment", None):
            inv_list = [f"{k} x{v}" for k, v in inventory.equipment.items() if v]
            if inv_list:
                print("Inventory:", ", ".join(inv_list))
        try:
            selection = int(input("\nChoose an option: ")) - 1
            if selection < 0 or selection >= len(available_choices):
                raise IndexError()
            choice = available_choices[selection]
        except (ValueError, IndexError):
            print("Invalid option")
            continue
        if getattr(choice, "sound", None):
            try:
                audio.play_effect(choice.sound)
            except Exception:
                pass
        choice.apply_effects(inventory, flags)
        narration = make_narration_for_choice(choice, inventory, flags)
        print("\n" + narration)
        input("\n(Press Enter to continue...)")
        clear_screen()
        try:
            if choice.effectsFlag.get("used_exorcism"):
                audio.play_effect("src/sounds/holy_scream.wav")
        except Exception:
            pass
        if choice.target is None:
            print("The story ends here. Thanks for playing.")
            running = False
        else:
            current_node = choice.target
    try:
        audio.close()
    except Exception:
        pass

if __name__ == "__main__":
    main()
