import os
from typing import Optional

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

from utils import create_corpus

class ProtVec(Word2Vec):

    def __init__(self,
                 filename: Optional[str] = None,
                 iscorpus: bool = True,
                 n: int = 3,
                 size: int = 100,
                 sg: int = 1,
                 window: int = 25,
                 min_count: int = 1,
                 workers: int = 3,
                 **kwargs) -> None:
        """
        Either fasta_fname or corpus_file are required.
        """
        self.filename = filename
        self.n = n
        self.size = size

        if iscorpus:
            sentences = LineSentence(filename)
            print(sentences)
