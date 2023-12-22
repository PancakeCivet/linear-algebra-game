from enum import IntEnum, unique
from typing import Any, List
import copy


@unique
class Effect(IntEnum):
    doubling = 0
    swap = 1
    adding = 2
    chang_number = 3
    passing = 4


from typing import Tuple


class Card:
    def __init__(
        self, effect: str, number: int = -1, sub: int = 0, obj: int = 0
    ) -> None:
        self.effect = effect
        self.number = number
        self.sub = sub
        self.obj = obj

    def __repr__(self) -> str:
        return f"Card({self.effect}, {self.number})"

    def get_card(self) -> Tuple[str, int]:
        return self.effect, self.number

    def __lt__(self, other: "Card") -> bool:
        if self.effect != other.effect:
            return self.effect < other.effect
        else:
            return self.number < other.number

    def __eq__(self, other: "Card") -> bool:
        return self.get_card() == other.get_card()


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


class Deck(CardSet):
    def get_next_card(self) -> Card:
        if self.is_empty():
            raise Exception("No Card Left")
        return self._cards.pop(0)
