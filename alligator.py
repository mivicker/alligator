from dataclasses import dataclass, field
import warnings


def down(pos: tuple[int, int]) -> tuple[int, int]:
    one, two = pos
    return (one + 1, two)


def right(pos: tuple[int, int]) -> tuple[int, int]:
    one, two = pos
    return (one, two + 1)

# Case x is zero & xs is empty
# Case x is zero & xs
# Case y is zero & ys is empty
# Case y is zero & ys
# Case both are zero & both
# Case both are zero & x
# Case both are zero & y
# Case both are zero & neither

def pop(xs: list):
    match xs:
        case []:
            print("empty")
        case [x]:
            print("only", x)
        case [x, *xs]:
            print(x, "plus", xs)


def allocate(
    needs: list[int], supplies: list[int], location: tuple[int, int]
) -> dict[tuple[int, int], int]:
    n, *ns = needs
    s, *ses = supplies

    return {(0, 0): 0}


# place the minimum at the location
# subtract the minimum from the other
# pop the next from the min list

# What am I struggling with? Testing for the minimum appropriately.
pop([])
pop([1,2,3])
pop([3])
