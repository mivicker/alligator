from typing import List, Tuple
from dataclasses import dataclass, field
import warnings


@dataclass
class Cursor:
    i: int = 0
    j: int = 0

    @property
    def tup(self) -> Tuple[int, int]:
        return (self.i, self.j)

    def down(self):
        self.i += 1

    def right(self):
        self.j += 1


@dataclass
class Allocation:
    needs: list
    supplies: list
    need_len: int = 0
    supply_len: int = 0
    need: int = 0
    supply: int = 0
    allocation: dict = field(default_factory=dict)
    cursor: Cursor = field(default_factory=Cursor)

    def __post_init__(self):
        self.need_len = len(self.needs)
        self.supply_len = len(self.supplies)
        self.need = self.needs.pop()
        self.supply = self.supplies.pop()

    def __str__(self) -> str:
        return str(self.allocation)

    @property
    def incomplete(self):
        return any(
            [
                bool(self.needs),
                bool(self.supplies),
                bool(self.need),
                bool(self.supply),
            ]
        )

    def advance_need(self):
        self.need = self.needs.pop()
        self.cursor.down()

    def advance_supply(self):
        self.supply = self.supplies.pop()
        self.cursor.right()

    def allocate(self):
        while self.incomplete:
            if self.need < self.supply:
                self.allocation[self.cursor.tup] = self.need
                self.supply -= self.need
                if not self.needs:
                    break
                self.advance_need()

            elif self.need == self.supply:
                self.allocation[self.cursor.tup] = self.need
                if not self.needs:
                    break
                self.advance_need()
                self.advance_supply()

            else:
                self.allocation[self.cursor.tup] = self.supply
                self.need -= self.supply
                if not self.supplies:
                    warnings.warn("Not enough supplies to meet need")
                    break
                self.advance_supply()

        return self.allocation

    def as_matrix(self):
        if self.incomplete:
            self.allocate()

        result = [
            [0 for _ in range(self.supply_len)] for _ in range(self.need_len)
        ]

        for (row, col), quantity in self.allocation.items():
            result[row][col] = quantity

        return result

def allocate(a:List[int], b:List[int]) -> List[List[int]]:
    return Allocation(
        needs=a,
        supplies=b
    ).as_matrix()

if __name__ == "__main__":
    print(allocate([1,2,3], [3,2,1]))
