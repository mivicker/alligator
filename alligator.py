from dataclasses import dataclass, field


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
    needs: list[int]
    supplies: list[int]


def id_unallocated(unallocated: Unallocated) -> str:
    match unallocated:
        case Unallocated(
            needs=[],
            supplies=[],
        ):
            return "perfect match"

        case Unallocated(
            needs=[],
            supplies=[*supplies]
        ):
            return "no need"

        case Unallocated(
            needs=[*needs],
            supplies=[],
        ):
            return "no supply"

        case Unallocated(
            needs=[*needs],
            supplies=[*supplies]
        ):
            return "continue"

        case _:
            raise ValueError("Input must be type Unallocated")


@dataclass
class Allocating:
    remaining: Unallocated
    allocation: Allocation = field(default_factory=dict)


def allocate(current: Allocating, cursor = (0,0)) -> Allocating:
    n, *needs  = current.remaining.needs
    s, *supplies = current.remaining.supplies

# Case x is zero & xs is empty
# Case x is zero & xs
# Case y is zero & ys is empty
# Case y is zero & ys
# Case both are zero & both
# Case both are zero & x
# Case both are zero & y
# Case both are zero & neither

un = Unallocated(
    needs=[1,2,3],
    supplies=[1,2,3]
)



# place the minimum at the location
# subtract the minimum from the other
# pop the next from the min list

# What am I struggling with? Testing for the minimum appropriately.

print(id_unallocated(un))
