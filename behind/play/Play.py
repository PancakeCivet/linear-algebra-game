from ..card import Card, CardSet, Hand, Deck, Effect
from ..creat import generate_full_rank_matrix, is_identity_matrix, add_rows, swap_rows
from typing import Tuple, List, Any
import numpy as np
import copy


class player(Hand):
    def sort_cards(self, cards: List[Card]) -> List[Card]:
        return sorted(cards, reverse=True)

    def action(self, cards: List[Card], player_number: int, this_matrix) -> Card:
        player_out = Card()
        """
        通过socket来接受player出的什么牌
        """
        return player_out

    """
                player_number: 当前玩家编号
                this_matrix: 当前矩阵形式
                cards: 当前玩家手牌
                player_out: 当前玩家出的牌
    """


class game:
    _player_hands: List[Hand]

    """保证传的cards是随机的"""

    def __init__(self, cards: List[Card], num_player: int, dealer_id: int, matrix):
        self._deck = Deck(cards)
        self._players = [player() for _ in range(num_player)]
        self._player_hands = []
        self._current_player_id = dealer_id - 1
        self._matrix = matrix

        for i in range(num_player):
            temp = []
            for j in range(len(cards) / num_player):
                temp.append(self._deck.get_next_card())
            self._player_hands.append(Hand(temp))

    def is_end(self) -> bool:
        for i in self._player_hands:
            if i.is_empty():
                return True
        if is_identity_matrix(self._matrix):
            return True
        return False

    def is_not_end(self) -> bool:
        return not self.is_end()

    def current_player_drop_card(self, card: Card) -> None:
        self._player_hands[self._current_player_id].remove_card(card)

    """在此处计算矩阵变化?"""

    def get_winner(self) -> int:
        if self.is_not_end():
            raise Exception("Game is not end")
        return self._current_player_id - 1

    def get_info(self) -> Tuple[int, List[Hand]]:
        return (self._current_player_id, self._player_hands)

    def turn(self):
        if self.is_end():
            raise Exception("Game is end")

        self._current_player_id = (self._current_player_id + 1) % len(self._players)
        hand = self._player_hands[self._current_player_id]
        action = self._players[self._current_player_id].action(
            self._player_hands[self._current_player_id].get_cards(),
            self._current_player_id,
            self._matrix,
        )
        if action.effect == Effect.adding:
            add_number = action.number
            add_sub = action.sub
            add_obj = action.obj
            add_rows(self._matrix, add_sub, add_obj, add_number)

        if action.effect == Effect.doubling:
            add_number = action.number - 1
            add_obj = action.obj
            add_rows(self._matrix, add_obj, add_obj, add_number)
        if action.effect == Effect.passing:
            pass
        if action.effect == Effect.swap:
            add_obj = action.obj
            add_sub = action.sub
            swap_rows(self._matrix, add_sub, add_obj)
        return action, self.get_info(), self.is_not_end()
