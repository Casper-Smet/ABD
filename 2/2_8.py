import random


class DirtyCarpetEnv():
    def __init__(self, n_tiles: int) -> None:
        self.n_tiles = n_tiles
        self.reset()

    def step(self, action):
        "Makes one step in the (episodic) environment."
        if action == "Suck":
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

        return self.tiles[self.current_tile]


if __name__ == "__main__":
    env = DirtyCarpetEnv(2)

    state = env.reset()
    for i in range(10):
        action = random.choice(["Left", "Right", "Suck"])
        next_state = env.step(action)
        print(state, action)
        state = next_state
