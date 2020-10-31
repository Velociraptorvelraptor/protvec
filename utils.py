from typing import List, Iterator

from Bio import SeqIO

def split_sequence(sequence: str, n: int) -> Iterator[List[str]]:
    """
    :param sequence: Nucleotides or proteins string of characters.
    :param n: N in n-grams.
    """
    for k in range(n):
        yield [sequence[i : i + n] for i in range(k, len(sequence) - n, n)]

def generate_ngrams_from_file(fasta_fname: str, n: int) -> List[List[str]]:
    """
    Reads character sequences from file and split them into n-grams,
    then yield them.
    :param fasta_fname: Path to fasta extension data.
    :param n: N in n-grams.
    """
    with open(fasta_fname, 'r') as file:
        for seq_record in SeqIO.parse(file, format='fasta'):
             yield from split_sequence(str(seq_record.seq), n)

