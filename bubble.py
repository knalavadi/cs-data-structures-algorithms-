def bubble_sort(L):
    """Basic bubble sort."""

    for i in range(len(L) - 1):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                # Pair out-of-order, swap them
                L[j], L[j + 1] = L[j + 1], L[j]


def shorter_bubble_sort(L):
    """Shorter bubble sort."""

    for i in range(len(L) - 1):
        # don't re-check already-sorted
        for j in range(len(L) - 1 - i):
            if L[j] > L[j + 1]:
                # Pair out-of-order, swap them
                L[j], L[j + 1] = L[j + 1], L[j]


def best_bubble_sort(L):
    """Shorter and fast-win bubble sort."""

    for i in range(len(L) - 1):
        # keep track of whether we made a swap
        made_swap = False
        for j in range(len(L) - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                made_swap = True
        if not made_swap:
            # If no swap, list already sorted
            break
