from typing import List, Iterator

def split_sequence(sequence: str, n: int) -> Iterator[List[str]]:
    for k in range(n):
        yield [sequence[i : i + n] for i in range(k, len(sequence) - n, n]