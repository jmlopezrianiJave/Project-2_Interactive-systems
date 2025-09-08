from audioManager import AudioManager
from inventory import Inventory
from choice import Choice
from node import Node

def build_story():
    ##TODO create the nodes with the story we are creating
    
    return 0

def main():
    nodes = build_story()
    current_node = 1
    inventory = Inventory({})
    flags = {}
    audio = AudioManager()
    running = True

    ambient_map = {
        #TODO aggregate all the ambient sounds for each node
        1: "sounds/cave_drip.wav",   # looping ambient
        2: "sounds/fire_torch.wav"   # torch crackling loop
    }
    effect_map = {
        #TODO aggregate all the effect sounds for each node
        "torch_lit": "sounds/torch_ignite.wav"   # one-shot effect
    }

    while running:
        node = nodes[current_node]

        print(f"\n=== {node.title} ===")
        print(node.description)

        # play ambient for current node
        if node.id in ambient_map:
            audio.play_ambient(ambient_map[node.id])

        available_choices = [c for c in node.choices if c.is_available(inventory, flags)]
        for idx, choice in enumerate(available_choices, start=1):
            print(f"{idx}. {choice.text}")

        try:
            selection = int(input("\nChoose an option: ")) - 1
            choice = available_choices[selection]
        except (ValueError, IndexError):
            print("⚠️ Invalid option")
            continue

        choice.apply_effects(inventory, flags)
        for f, val in choice.effectsFlag.items():
            if f in effect_map:
                audio.play_effect(effect_map[f])

        if choice.target is None:
            print("End of test story.")
            running = False
        else:
            current_node = choice.target

    audio.close()
main()
