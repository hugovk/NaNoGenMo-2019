#!/usr/bin/env python
"""
NaNoGenMo

What else could it stand for?

National Novel Generosity Month?

National Novelty Generosity Month?

Will just go through all the possibilities, and generate a catalogue of all different
kinds of NaNoGenMo.

A NaNaNoGenMoGenMo?

Usage.

To generate 12 days of plain text:

python nananogenmogenmo.py --words 12

To generate 50k words onto your Mac clipboard:

python nananogenmogenmo.py | pbcopy
"""
import argparse
import random
from collections import defaultdict, namedtuple
from pprint import pprint  # noqa: F401

import pronouncing  # pip install pronouncing


def initial_rhyming_part(phones):
    """Like pronouncing.rhyming_part but the bit at the start:
    Get the "initial rhyming part" of a string with CMUdict phones.
    "Initial rhyming part" here means everything from the vowel in the stressed
    syllable nearest the *start* of the word *down* to the *start* of the word.
    .. doctest::
        >>> phones = pronouncing.phones_for_word("purple")
        >>> pronouncing.initial_rhyming_part(phones[0])
        'P ER1'
    :param phones: a string containing space-separated CMUdict phones
    :returns: a string with just the "rhyming part" of those phones
    """
    phones_list = phones.split()
    for i in range(len(phones_list)):
        if phones_list[i][-1] in "12":
            return " ".join(phones_list[: i + 1])
    return phones


def main(args):
    Word = namedtuple("Word", "prefix word")

    WORDS = [
        Word("na", "national"),
        Word("no", "novel"),
        Word("gen", "generation"),
        Word("mo", "month"),
    ]

    word_store = defaultdict()
    for word in WORDS:
        phones = pronouncing.phones_for_word(word.word)
        part = initial_rhyming_part(phones[0])
        words = pronouncing.search(f"^{part}")
        # Keep those that start with the prefix
        # eg. ditch "gnatcatcher" for national's "na"
        # Also don't include "national", "novel", "generation", "month" or "nazism"
        words = {
            w
            for w in words
            if w.startswith(word.prefix) and not w.startswith(word.word)
        }
        word_store[word.word] = list(words - {"nazism"})
        # print(len(words))

    # Generate something
    total = 0
    while total < args.words:
        things = [random.choice(word_store[word.word]).capitalize() for word in WORDS]
        total += len(things)
        # print(" ".join(things))
        # ASCII code 11 (0x0B), soft newline in Word, good for Justify Text
        # print(" ".join(things), end="\x0b")
        print("\t".join(things))
    print(f"{total} words")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="National NaNoGenMo Generation Month",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-w",
        "--words",
        type=int,
        default=50000,
        help="Minimum number of words to output",
    )
    args = parser.parse_args()
    main(args)
