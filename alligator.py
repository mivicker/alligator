from dataclasses import dataclass, field
from warnings import warn


Cursor = tuple[int, int]


def down(pos: Cursor) -> Cursor:
    one, two = pos
    return (one + 1, two)


def right(pos: Cursor) -> Cursor:
    one, two = pos
    return (one, two + 1)


Allocation = dict[Cursor, int]


@dataclass
class Unallocated:
    needs: list[int] = field(default_factory=list)
    supplies: list[int] = field(default_factory=list)


@dataclass
class Allocating:
    remaining: Unallocated = field(default_factory=Unallocated)
    cursor: Cursor = (0, 0)
    allocation: Allocation = field(default_factory=dict)


def allocation_step(current: Allocating) -> Allocating:
    n, *needs = current.remaining.needs
    s, *supplies = current.remaining.supplies

    if n > s:
        return Allocating(
            cursor=down(current.cursor),
            remaining=Unallocated(
                needs=[n - s] + needs,
                supplies=supplies,
            ),
            allocation={
                current.cursor: s,
                **current.allocation,
            }
        )

    elif n < s:
        return Allocating(
            cursor=right(current.cursor),
            remaining=Unallocated(
                needs=needs,
                supplies=[s - n] + supplies,
            ),
            allocation={
                current.cursor: n,
                **current.allocation,
            }
        )

    return Allocating(
        cursor=down(right(current.cursor)),
        remaining=Unallocated(
            needs=needs,
            supplies=supplies,
        ),
        allocation={
            current.cursor: n,
            **current.allocation,
        }
    )


def _allocate(current: Allocating) -> Allocation:
    match current.remaining:
        case (Unallocated(needs=[], supplies=[]) 
              | Unallocated(needs=[], supplies=[*_])):
            return current.allocation

        case Unallocated(needs=[*_], supplies=[]):
            warn("This allocation doesn't cover all the need")
            return current.allocation

        case Unallocated(needs=[*_], supplies=[*_]):
            return _allocate(allocation_step(current))

        case _:
            raise ValueError("Input must be type Unallocated")

def allocate(a: list, b: list) -> dict[Cursor, int]:
    return _allocate(Allocating(remaining=Unallocated(needs=a, supplies=b)))

if __name__ == "__main__":
    allocation = allocate([8, 16, 6], [10, 10, 10])
    print(allocation)

