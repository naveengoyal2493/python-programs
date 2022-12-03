from collections import defaultdict
from email.policy import default


def group_anagrams(strings):
    res = defaultdict(list)

    