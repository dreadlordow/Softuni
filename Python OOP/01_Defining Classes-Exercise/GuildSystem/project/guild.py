class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild == self.name:
            return f'Player {player.name} is already in the guild.'

        elif not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f'Player {player.name} is in another guild.'

        player.guild = self.name
        self.list_of_players.append(player)
        return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for player in self.list_of_players:
            if player.name == player_name:
                self.list_of_players.remove(player)
                return f'Player {player_name} has been removed from the guild.'
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for player in self.list_of_players:
            result += player.player_info()
        return result

