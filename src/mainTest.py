# main.py  (updated with clear-screen, narration, dynamic descriptions)
import os
import sys
from audioManager import AudioManager
from inventory import Inventory
from choice import Choice
from node import Node

# helper: clear the terminal screen cross-platform
def clear_screen():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")


def build_story():

    nodes = {}

    # 1 - Foyer
    nodes[1] = Node(
        id=1,
        title="Foyer",
        description=(
            "You stand in the dim foyer of an old house. The air is cold. "
            "A coat rack hangs by the door, an umbrella stand leans in the corner. "
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
                sound="sounds/key_pickup.wav",
            ),
            Choice(
                "Check the umbrella stand",
                target=1,
                requiresFlag={"has_letter": False},
                effectsInv={"letter": 1},
                effectsFlag={"has_letter": True},
                sound="sounds/paper_rustle.wav",
            ),
            Choice(
                "Read the old letter",
                target=1,
                requiresInv={"letter": 1},
                requiresFlag={"read_letter": False},
                effectsFlag={"read_letter": True},
                sound="sounds/page_rustle.wav",
            ),
            Choice("Leave the house", target=None),
        ],
    )

    # 2 - Living Room
    nodes[2] = Node(
        id=2,
        title="Living room",
        description=(
            "A sagging sofa faces a shuttered window. Bookshelves line one wall — "
            "one book looks worn, as if it were read often."
        ),
        choices=[
            Choice(
                "Read the worn book on the shelf",
                target=2,
                requiresFlag={"read_book": False},
                effectsInv={"journal": 1},
                effectsFlag={"read_book": True},
                sound="sounds/page_rustle.wav",
            ),
            Choice("Follow the hallway to the kitchen", target=3),
            Choice("Go up the staircase", target=4),
            Choice("Return to the foyer", target=1),
        ],
    )

    # 3 - Kitchen
    nodes[3] = Node(
        id=3,
        title="Kitchen",
        description=(
            "The kitchen is cold and lately used. A small knife lies on the counter. "
            "An old metal cabinet on the far wall is locked with a padlock."
        ),
        choices=[
            Choice(
                "Pick up the small knife",
                target=3,
                requiresFlag={"picked_knife": False},
                effectsInv={"knife": 1},
                effectsFlag={"picked_knife": True},
                sound="sounds/knife_pickup.wav",
            ),
            # opening cabinet requires the rusty key from foyer; one-time
            Choice(
                "Try to open the locked cabinet (use rusty key)",
                target=3,
                requiresInv={"rusty_key": 1},
                requiresFlag={"opened_cabinet": False},
                effectsInv={"holy_water": 1, "rusty_key": -1},
                effectsFlag={"opened_cabinet": True},
                sound="sounds/lock_open.wav",
            ),
            Choice("Look into the sink and drawers (nothing special)", target=3, sound="sounds/drawer_rummage.wav"),
            Choice("Return to the living room", target=2),
        ],
    )

    # 4 - Stair landing (access to attic and basement)
    nodes[4] = Node(
        id=4,
        title="Stair landing",
        description=(
            "The staircase creaks. The hallway splits: a narrow door down to the basement, "
            "and a steep ladder leading to a cramped attic hatch."
        ),
        choices=[
            Choice("Climb up into the attic", target=5),
            Choice("Descend to the basement", target=6),
            Choice("Go back to the living room", target=2),
        ],
    )

    # 5 - Attic
    nodes[5] = Node(
        id=5,
        title="Attic",
        description=(
            "Dust motes float in the slanting beams of light. A trunk sits in the corner, "
            "its lid sealed with brittle tape."
        ),
        choices=[
            # require knife to cut tape (knife present if picked up in kitchen)
            Choice(
                "Cut open the trunk with your knife",
                target=5,
                requiresInv={"knife": 1},
                requiresFlag={"opened_trunk": False},
                effectsInv={"ritual_notes": 1},
                effectsFlag={"opened_trunk": True},
                sound="sounds/tape_cut.wav",
            ),
            Choice(
                "Force the trunk open with your hands (risky)",
                target=5,
                requiresFlag={"opened_trunk": False},
                effectsInv={"ritual_notes": 1},
                effectsFlag={"opened_trunk": True},
                sound="sounds/wood_snap.wav",
            ),
            Choice("Return to the stair landing", target=4),
        ],
    )

    # 6 - Basement (approach toward the possessed person's room)
    nodes[6] = Node(
        id=6,
        title="Basement corridor",
        description=(
            "Damp concrete and a single bare bulb. The humming is louder here. "
            "A heavy door at the end stands slightly ajar and cold air leaks out."
        ),
        choices=[
            Choice("Approach the heavy door (the source of the sound)", target=7),
            Choice(
                "Search the storage shelves",
                target=6,
                requiresFlag={"searched_shelves": False},
                effectsInv={"moldy_rag": 1},
                effectsFlag={"searched_shelves": True},
                sound="sounds/shelf_clatter.wav",
            ),
            Choice("Go back upstairs", target=4),
        ],
    )

    # 7 - Threshold (right before the possessed room)
    nodes[7] = Node(
        id=7,
        title="Threshold",
        description=(
            "The door opens into a small, sparsely furnished room. Chains hang on one wall, "
            "and on a low table are strange symbols that look like a rushed ritual. "
            "The humming resolves into a voice—something inside is awake."
        ),
        choices=[
            # Different confrontation options become available depending on inventory:
            Choice(
                "Sprinkle holy water and attempt an exorcism",
                target=8,
                requiresInv={"holy_water": 1},
                effectsInv={"holy_water": -1, "used_exorcism": 1},
                sound="sounds/holy_splash.wav",
            ),
            Choice(
                "Use the ritual notes you found to try to bind the thing",
                target=8,
                requiresInv={"ritual_notes": 1},
                effectsInv={"ritual_notes": -1, "used_ritual": 1},
                sound="sounds/chant.wav",
            ),
            Choice(
                "Rush in with the knife and try to fight",
                target=8,
                requiresInv={"knife": 1},
                effectsInv={"used_violence": 1},
                sound="sounds/knife_swipe.wav",
            ),
            Choice(
                "Burst in unprepared (no items)",
                target=8,
                effectsInv={"used_none": 1},
                sound="sounds/door_bang.wav",
            ),
            Choice("Step back quietly and rethink your approach", target=6),
        ],
    )

    # 8 - Confrontation / Ending node
    nodes[8] = Node(
        id=8,
        title="Confrontation",
        description=(
            "You enter the small room. The air is thick and the possessor locks eyes with you. "
            "How this ends depends on what you've prepared."
        ),
        choices=[Choice("Resolve the encounter", target=None)],
    )

    return nodes


# small narration templates keyed by effect keys or choice text snippets
NARRATION_MAP = {
    "rusty_key": "You pry the rusty key from the wood. It tastes of iron in your palm.",
    "letter": "You slide the brittle envelope free. The paper crackles.",
    "knife": "You take the small kitchen knife. The metal feels oddly warm.",
    "holy_water": "A vial of cloudy liquid hums faintly in your hands.",
    "ritual_notes": "You unfold the ritual notes; the handwriting shakes the page.",
    "opened_cabinet": "The padlock snaps loose with a shriek, revealing a small vial.",
    "opened_trunk": "The trunk lid gives way and inside you find handwritten notes.",
    "read_letter": "You read the letter. The handwriting is hurried and mentions a 'binding' in the basement.",
    "read_book": "The book's margins are full of frantic annotations and a map of the house.",
    "picked_knife": "The knife is small but serviceable; it's better than empty hands.",
}


def make_narration_for_choice(choice, inventory, flags):
    """
    Build a short narration string for the chosen action.
    Priority: check effectsInv keys -> effectsFlag -> fallback to simple echo of the choice text.
    """
    lines = []

    # check direct inventory effects
    for key in choice.effectsInv.keys():
        if key in NARRATION_MAP:
            lines.append(NARRATION_MAP[key])

    # check effect flags
    for key in choice.effectsFlag.keys():
        if key in NARRATION_MAP:
            lines.append(NARRATION_MAP[key])

    # provide some context-specific narration for reading the letter or book
    if choice.effectsFlag.get("read_letter"):
        lines.append(NARRATION_MAP.get("read_letter"))
    if choice.effectsFlag.get("read_book"):
        lines.append(NARRATION_MAP.get("read_book"))

    if not lines:
        # fallback: a small echo
        lines.append(f"You: {choice.text}")

    return "\n".join(lines)


def dynamic_room_description(node: Node, flags: dict, inventory: Inventory) -> str:
    """
    Return the node.description plus dynamic lines depending on flags/inventory.
    """
    desc = node.description + "\n"

    # example: foyer reacts to rusty key
    if node.id == 1:
        if flags.get("grabbed_rusty_key"):
            desc += "\nThe coat rack is empty now — the rusty key is gone."
        else:
            desc += "\nThe coat rack looks like it might hide something useful."

        if inventory.equipment.get("letter", 0) and not flags.get("read_letter"):
            desc += "\nYou have an unread letter in your pocket. You can read it."

    # kitchen reflects whether the cabinet was opened
    if node.id == 3:
        if flags.get("opened_cabinet"):
            desc += "\nYou already opened the cabinet — the vial is gone or in your inventory."
        else:
            desc += "\nThe cabinet is still locked with a padlock."

    # attic if trunk opened
    if node.id == 5:
        if flags.get("opened_trunk"):
            desc += "\nThe open trunk reveals torn cloth and a stack of pages."
        else:
            desc += "\nThe trunk's brittle tape waits to be cut."

    # basement hint if ritual notes have been found
    if node.id == 6 and inventory.equipment.get("ritual_notes", 0):
        desc += "\nYour mind remembers a phrase from the ritual notes — it might help later."

    return desc


def main():
    # build game data
    nodes = build_story()
    current_node = 1
    inventory = Inventory({})  # your Inventory class instance
    flags = {
        # default flags are False
    }
    audio = AudioManager()
    running = True

    # Ambient/effect maps (edit paths to match your sounds if you have them)
    ambient_map = {
        1: "sounds/creak_loop.wav",
        2: "sounds/room_hum_loop.wav",
        6: "sounds/basement_drip_loop.wav",
        7: "sounds/hum_build_loop.wav",
    }

    # print a small help on first run
    clear_screen()
    print("Haunted House — simple text game\nType the number of a choice and press Enter.")
    print("Hint: some choices are one-time and won't appear again once taken.\n")

    while running:
        # ensure nodes is a dict (quick runtime sanity)
        if not isinstance(nodes, dict):
            raise RuntimeError("nodes must be a dict mapping id->Node. build_story() returned something else.")

        node = nodes[current_node]

        # Print dynamic description that reflects flags & inventory
        print(f"\n=== {node.title} ===")
        print(dynamic_room_description(node, flags, inventory))

        # Play ambient if available
        if node.id in ambient_map:
            try:
                audio.play_ambient(ambient_map[node.id])
            except Exception:
                # audio is optional — don't crash if it fails
                pass

        # For node 8, compute the ending outcome using inventory markers (used_*)
        if node.id == 8:
            used_exorcism = inventory.equipment.get("used_exorcism", 0)
            used_ritual = inventory.equipment.get("used_ritual", 0)
            used_violence = inventory.equipment.get("used_violence", 0)
            used_none = inventory.equipment.get("used_none", 0)

            if used_exorcism:
                print("\nYou move carefully, whispering words as you sprinkle the holy water. "
                      "The room screams, light floods, and slowly the features in front of you soften. "
                      "The person collapses — alive, but freed. You survived; you saved them.")
            elif used_ritual:
                print("\nFollowing the notes precisely, you trace the sigils and speak the binding phrases. "
                      "The air convulses. For a terrible second you see something immense, then the voice is gone. "
                      "The person slumps — alive, the possession broken but the cost evident.")
            elif used_violence:
                print("\nYou lunge with the knife. For a moment it seems to work — the creature recoils — "
                      "but the wound burns your hands and the air turns cold. You manage to subdue the thing, "
                      "but the moral consequences linger. The body may recover; you are not sure.")
            else:
                print("\nYou rush in empty-handed. There is no time to think. The thing is faster. "
                      "It overwhelms you. Everything goes black.")
            running = False
            break

        # List available choices (Choice.is_available should use inv & flags)
        available_choices = [c for c in node.choices if c.is_available(inventory, flags)]
        for idx, choice in enumerate(available_choices, start=1):
            print(f"{idx}. {choice.text}")

        # show inventory briefly
        if getattr(inventory, "equipment", None):
            inv_list = [f"{k} x{v}" for k, v in inventory.equipment.items() if v]
            if inv_list:
                print("Inventory:", ", ".join(inv_list))

        # get input
        try:
            selection = int(input("\nChoose an option: ")) - 1
            if selection < 0 or selection >= len(available_choices):
                raise IndexError()
            choice = available_choices[selection]
        except (ValueError, IndexError):
            print("⚠️ Invalid option")
            continue

        # Play the choice's short effect sound (if any) BEFORE applying effects so the player hears the action
        if getattr(choice, "sound", None):
            try:
                audio.play_effect(choice.sound)
            except Exception:
                pass

        # Apply effects (add/remove items, mark items used, etc.)
        choice.apply_effects(inventory, flags)

        # Build and show narration for the action
        narration = make_narration_for_choice(choice, inventory, flags)
        print("\n" + narration)

        # Let the player see the narration before clearing the screen
        input("\n(Press Enter to continue...)")

        # Clear screen when a choice is made (as requested)
        clear_screen()

        # tiny additional feedback sounds based on effect keys (optional)
        try:
            if choice.effectsInv.get("used_exorcism"):
                audio.play_effect("sounds/holy_scream.wav")
        except Exception:
            pass

        # navigate to next node or end
        if choice.target is None:
            # print a short farewell/ending note
            print("The story ends here. Thanks for playing.")
            running = False
        else:
            current_node = choice.target

    # tidy up audio
    try:
        audio.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
