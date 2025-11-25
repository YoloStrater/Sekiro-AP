
def add_sekiro_logic(world):
    # Example: if you have Grappling Hook, you can access Ashina Castle
    def has_grappling(state):
        return state.has("Grappling Hook", world.player)
    # connect regions (you will define Region objects and connections here)
    # region_castle.add_connection(region_outskirts, rule=has_grappling)

# Forbidden placement example function used during seeding:
PROGRESSIVE = {"Grappling Hook", "Prosthetic Arm Upgrade", "Fountainhead Tear"}
def is_forbidden_placement(item, location, world):
    # Do not put progression items in trivial early chests
    if item.name in PROGRESSIVE and location.region == "Tutorial":
        return True
    return False
