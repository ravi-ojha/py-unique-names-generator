import random

from .data import ANIMALS
from .data import COLORS


def get_random_name(
    combo=[COLORS, ANIMALS], separator: str = " ", style: str = "capital"
):
    if not combo:
        raise Exception("combo cannot be empty")

    random_name = []
    for word_list in combo:
        part_name = random.choice(word_list)
        if style == "capital":
            part_name = part_name.capitalize()
        if style == "lowercase":
            part_name = part_name.lower()
        if style == "uppercase":
            part_name = part_name.upper()
        random_name.append(part_name)
    return separator.join(random_name)
