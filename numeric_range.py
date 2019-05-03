# Trey Hunner <trey@truthful.technology>

from functools import reduce


def numeric_range(numbers):
    """Return difference between largest and smallest given numbers."""
    return max(numbers) - min(numbers)


def numeric_range_second(numbers):
    """Return difference between largest and smallest given numbers."""
    return max(numbers, default=0) - min(numbers, default=0)

def numeric_range_third(iterable):
    """Return difference between largest and smallest given numbers."""
    sequence = list(iterable)
    return max(sequence, default=0) - min(sequence, default=0)

def numeric_range_fourth(iterable):
    """Return difference between largest and smallest given numbers."""
    maximum = None
    minimum = None
    for n in iterable:
        if maximum is None or maximum < n:
            maximum = n
        if minimum is None or n < minimum:
            minimum = n
    return maximum - minimum

def numeric_range_fifth(iterable):
    """Return difference between largest and smallest given numbers."""
    maximum = None
    minimum = None
    for n in iterable:
        if maximum is None or maximum < n:
            maximum = n
        if minimum is None or n < minimum:
            minimum = n
    if maximum is None:
        return 0
    else:
        return maximum - minimum

def numeric_range_sixth(iterable):
    """Return difference between largest and smallest given numbers."""
    iterator = iter(iterable)
    try:
        minimum = maximum = next(iterator)
    except StopIteration:
        minimum = maximum = 0
    for n in iterable:
        if maximum < n:
            maximum = n
        if n < minimum:
            minimum = n
    return maximum - minimum


def accumulate_minmax(accumulator, value):
    current_min, current_max = accumulator
    return min(current_min, value), max(current_max, value)

def numeric_range_last(iterable):
    iterator = iter(iterable)
    try:
        first = next(iterator)
    except StopIteration:
        return 0
    smallest, biggest = reduce(accumulate_minmax, iterator, (first, first))
    return biggest - smallest