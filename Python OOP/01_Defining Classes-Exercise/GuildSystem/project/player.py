class Player:
    def __init__(self, name, hp, mp):
        self.name: str = name
        self.hp: int = hp
        self.mp: int = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills.keys():
            self.skills[skill_name] = mana_cost
            return f'Skill {skill_name} added to the collection of the player {self.name}'
        return f'Skill already added'

    def player_info(self):
        data = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
        for s, m in self.skills.items():
            data += f"==={s} - {m}\n"
        return data

