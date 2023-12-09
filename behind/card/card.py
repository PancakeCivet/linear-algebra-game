from enum import IntEnum, unique
from typing import Any, List
import copy


@unique
class Effect(IntEnum):
    doubling = 0
    swap = 1
    adding = 2
    chang_number = 3


class Card:
    def __init__(self, effect: Effect, number: int) -> None:
        self._effect = effect
        self._number = number

    def get_Card(self) -> Effect:
        return (self._effect, self._number)


class CardSet:
    _cards: List[Card]

    def __init__(self, cards) -> None:
        self._cards = copy.deepcopy(cards)

    def __repr__(self) -> str:
        return str(self.get_cards())

    def is_empty(self) -> bool:
        if len(self._cards) != 0:
            return False
        return True

    def get_cards(self):
        return copy.deepcopy(self._cards)


class Hand(CardSet):
    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card: Card) -> None:
        if card in self._cards:
            self._cards.remove(card)
