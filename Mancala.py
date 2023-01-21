# Author: Elizabeth Ward
# GitHub username: menollycg
# Date: December 4, 2022
# Description: A program that allows 2 players to play a text-based version of the game Mancala.

class Mancala:
    """
    Represents the game as played.  Contains information about the players and information about the board.  Will work
    with the Player class to keep track of the player and their part of the game.
    """

    def __init__(self):
        self._players = []

    def create_player(self, name):
        """
        Creates a Player object and adds it to the list of players.
        """
        player = Player(name)
        self._players.append(player)
        return player

    def print_board(self):
        """
        Prints the Mancala board with first listing the information for player 1 and then for player 2.  The information
        will include the amount of seeds in each pit as well as the store.
        """
        player_1 = self._players[0]
        board_1 = player_1.get_board()
        print("player1:")
        print("store: " + str(board_1[6]))
        print(board_1[0:6])

        player_2 = self._players[1]
        board_2 = player_2.get_board()
        print("player2:")
        print("store: " + str(board_2[6]))
        print(board_2[0:6])

    def play_game(self, player, pit):
        """
        Takes 2 parameters and updates the game boards after verifying that the pit specified is within certain
        boundaries.
        """
        if pit > 6 or pit <= 0:
            return "Invalid number for pit index"

        if self.is_winner():
            board_1 = self._players[0].get_board()
            board_2 = self._players[1].get_board()

            if self.is_empty(self._players[0]):
                temp_2 = board_2[6]
                for ind in range(0, 6):
                    temp_2 += board_2[ind]
                    board_2[ind] = 0
                board_2[6] = temp_2
            self._players[1].update_board(board_2)

            if self.is_empty(self._players[1]):
                temp_1 = board_1[6]
                for ind in range(0, 6):
                    temp_1 += board_1[ind]
                    board_1[ind] = 0
                board_1[6] = temp_1
            return "Game is ended"

        self.update_player(player - 1, pit - 1)
        if self.is_winner():
            board_1 = self._players[0].get_board()
            board_2 = self._players[1].get_board()

            if self.is_empty(self._players[0]):
                temp_2 = board_2[6]
                for ind in range(0, 6):
                    temp_2 += board_2[ind]
                    board_2[ind] = 0
                board_2[6] = temp_2
            self._players[1].update_board(board_2)

            if self.is_empty(self._players[1]):
                temp_1 = board_1[6]
                for ind in range(0, 6):
                    temp_1 += board_1[ind]
                    board_1[ind] = 0
                board_1[6] = temp_1

        return self._players[0].get_board() + self._players[1].get_board()

    def update_player(self, player, pit):
        """
        Updates the individual game boards for the players based on it being turn.
        """
        arr0 = [0] * 14

        if player == 0:
            player_1 = self._players[player]
            player_2 = self._players[player + 1]
            board_1 = player_1.get_board()
            seeds = board_1[pit]
            board_1[pit] = 0
            combo_board = player_1.get_board() + player_2.get_board() + arr0
        else:
            player_1 = self._players[player - 1]
            player_2 = self._players[player]
            board_2 = player_2.get_board()
            seeds = board_2[pit]
            board_2[pit] = 0
            combo_board = player_2.get_board() + player_1.get_board() + arr0
        addition = 0
        ind = pit + 1
        for num in range(0, seeds):
            if ind == 13 or ind == 27:
                combo_board[ind] += 0
                ind += 1
                addition += 1
            else:
                combo_board[ind] += 1
            ind += 1
        for num2 in range(0, addition):
            combo_board[ind - 1] += 1

        if ind == 7 or ind == 21:  # special case 1
            if player == 0:
                print("player 1 take another turn")
            else:
                print("player 2 take another turn")
        ind -= 1
        if (0 <= ind <= 5) and combo_board[ind] == 1:  # special case 2
            if ind == 0:
                combo_board[6] += combo_board[ind] + combo_board[12]
                combo_board[ind + 12] = 0
                combo_board[ind] = 0
            elif ind == 1:
                combo_board[6] += combo_board[ind] + combo_board[11]
                combo_board[ind + 10] = 0
                combo_board[ind] = 0
            elif ind == 2:
                combo_board[6] += combo_board[ind] + combo_board[10]
                combo_board[ind + 8] = 0
                combo_board[ind] = 0
            elif ind == 3:
                combo_board[6] += combo_board[ind] + combo_board[9]
                combo_board[ind + 6] = 0
                combo_board[ind] = 0
            elif ind == 4:
                combo_board[6] += combo_board[ind] + combo_board[8]
                combo_board[ind + 4] = 0
                combo_board[ind] = 0
            elif ind == 5:
                combo_board[6] += combo_board[ind] + combo_board[7]
                combo_board[ind + 2] = 0
                combo_board[ind] = 0

        if (14 <= ind <= 19) and combo_board[ind] == 1:  # special case 2
            if ind == 14:
                combo_board[6] += combo_board[ind] + combo_board[12]
                combo_board[ind - 2] = 0
                combo_board[ind] = 0
            elif ind == 15:
                combo_board[6] += combo_board[ind] + combo_board[11]
                combo_board[ind - 4] = 0
                combo_board[ind] = 0
            elif ind == 16:
                combo_board[6] += combo_board[ind] + combo_board[10]
                combo_board[ind - 6] = 0
                combo_board[ind] = 0
            elif ind == 17:
                combo_board[6] += combo_board[ind] + combo_board[9]
                combo_board[ind - 8] = 0
                combo_board[ind] = 0
            elif ind == 18:
                combo_board[6] += combo_board[ind] + combo_board[8]
                combo_board[ind - 10] = 0
                combo_board[ind] = 0
            elif ind == 19:
                combo_board[6] += combo_board[ind] + combo_board[7]
                combo_board[ind - 12] = 0
                combo_board[ind] = 0

        half = len(combo_board) // 2
        half_1, half_2 = combo_board[:half], combo_board[half:]
        half_combo = []
        for ind in range(0, len(half_1)):
            half_combo.append(half_1[ind] + half_2[ind])
        qtr = len(half_combo) // 2
        qtr_1, qtr_2 = half_combo[:qtr], half_combo[qtr:]

        if player == 0:
            player_1.update_board(qtr_1)
            player_2.update_board(qtr_2)
        else:
            player_2.update_board(qtr_1)
            player_1.update_board(qtr_2)

    def is_winner(self):
        """
        Checks to see if there is a winner returns True if there is one and False if there isn't.
        """

        if self.is_empty(self._players[0]) or self.is_empty(self._players[1]):
            return True
        return False

    def is_empty(self, player_object):
        """
        Checks to see whether the specified Player's object's pits are empty or not.
        """

        board = player_object.get_board()

        for ind in range(0, 6):
            if board[ind] != 0:
                return False
        return True

    def return_winner(self):
        """
        Takes no parameters other than self checks to see whether there is a winner and returns a statement stating
        who has won, whether it's a tie, or that the game has not ended.
        """
        if self.is_winner():
            if self.is_empty(self._players[0]) or self.is_empty(self._players[1]):
                board_1 = self._players[0].get_board()
                board_2 = self._players[1].get_board()

                if self.is_empty(self._players[0]):
                    for ind in range(0, 6):
                        board_2[6] += board_2[ind]
                        board_2[ind] = 0
                self._players[1].update_board(board_2)

                if self.is_empty(self._players[1]):
                    for ind in range(0, 6):
                        board_1[6] += board_1[ind]
                        board_1[ind] = 0
                self._players[0].update_board(board_1)

                if board_1[6] > board_2[6]:
                    return "Winner is player 1: " + self._players[0].get_name()
                if board_1[6] < board_2[6]:
                    return "Winner is player 2: " + self._players[1].get_name()
                if board_1[6] == board_2[6]:
                    return "It's a tie"
        if not (self.is_empty(self._players[0]) or self.is_empty(self._players[1])):
            return "Game has not ended"


class Player:
    """
    Represents the player and the status of their part of the game board.  Works with the Mancala class.
    """

    def __init__(self, name):
        self._name = name
        self._board = [4, 4, 4, 4, 4, 4, 0]

    def get_name(self):
        """
        Returns the Player object's name.
        """
        return self._name

    def get_board(self):
        """
        Returns the Player's part of the game board as a list.
        """
        return self._board

    def update_board(self, board):
        """
        Updates the respective Player's board.
        """
        self._board = board
