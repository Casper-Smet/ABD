import random
import itertools


class DirtyCarpetEnv():
    def __init__(self, n_tiles: int) -> None:
        self.n_tiles = n_tiles
        self.reset()

    def step(self, action):
        "Makes one step in the (episodic) environment. Only makes a new tile dirty, if current action == `Suck`."
        if action == "Suck":
            self.suck_total += 1
            if self.tiles[self.current_tile] == "Dirty":
                self.clean_total += 1  # Only add one if tile was dirty

            self.tiles[self.current_tile] = "Clean"

        elif action == "Left":
            self.current_tile = max(0, self.current_tile - 1)
        elif action == "Right":
            self.current_tile = min(self.n_tiles - 1, self.current_tile + 1)

        return self.tiles[self.current_tile]

    def make_a_mess(self):
        """Set a random tile to a 'Dirty' state. This tile could already be dirty."""
        self.tiles[random.randint(0, self.n_tiles-1)] = "Dirty"

    def reset(self):
        """Resets environment and returns state of the current tile of the environment."""
        self.tiles = ["Clean"] * self.n_tiles
        self.current_tile = random.randint(0, self.n_tiles-1)
        self.make_a_mess()
        self.suck_total = 0
        self.clean_total = 0

        return self.tiles[self.current_tile]


class SimpleReflexVacuumCleanerAgent():
    def __init__(self, actions) -> None:
        self.actions = actions

    def __call__(self, percept):
        """Returns action based on current perception."""
        if percept == "Dirty":
            return self.actions[2]
        elif percept == "Clean":
            return random.choice(self.actions[:2])


if __name__ == "__main__":
    env = DirtyCarpetEnv(2)
    agent = SimpleReflexVacuumCleanerAgent(["Left", "Right", "Suck"])

    tile_configs = [["Clean", "Clean"], ["Clean", "Dirty"], ["Dirty", "Clean"], ["Dirty", "Dirty"]]
    start_configs = [0, 1]

    total_score = 0
    for tile_conf, start_tile in itertools.product(tile_configs, start_configs):  # Run each configuration
        env.reset()
        env.tiles = tile_conf.copy()
        env.current_tile = start_tile
        state = start_tile

        [state := env.step(agent(state)) for _ in range(10)]  # Make 10 steps in the environment, more than enough
        total_score += env.clean_total
        print(f"{tile_conf=}, {start_tile=}, score={env.clean_total}")

    print(f"Average score: {total_score / (len(tile_configs) * len(start_configs))}")
