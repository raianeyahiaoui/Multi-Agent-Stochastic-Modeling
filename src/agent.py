from mesa import Agent

class MoneyAgent(Agent):
    """An agent with fixed initial wealth that can move and trade."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def move(self):
        # Stochastic movement in Moore neighborhood
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        # Interaction logic: Giving resource to a cellmate
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1 and self.wealth > 0:
            other = self.random.choice([a for a in cellmates if a is not self])
            other.wealth += 1
            self.wealth -= 1

    def step(self):
        self.move()
        self.give_money()
