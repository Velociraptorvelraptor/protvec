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
    :param fasta_fname: Path to fasta extension data file.
    :param n: N in n-grams.
    """
    with open(fasta_fname, 'r') as file:
        for seq_record in SeqIO.parse(file, format='fasta'):
             yield from split_sequence(str(seq_record.seq), n)


def create_corpus(fasta_fname: str, corpus_fname: str, n: int) -> None:
    """
    :param fasta_fname: Path to fasta extension data file.
    :param corpus_fname: Path to file where corpus data should be written.
    :param n: N in n-grams
    """
    with open(corpus_fname, 'w') as corpus_file:
        for ngrams_list in generate_ngrams_from_file(fasta_fname, n):
            corpus_file.write(' '.join(ngrams_list))
            corpus_file.write('\n')