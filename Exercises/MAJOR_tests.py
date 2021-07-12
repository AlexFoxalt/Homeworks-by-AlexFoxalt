from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    return True if len(set(elements)) <= 1 else False


print(all_the_same([1, 1, 1]))