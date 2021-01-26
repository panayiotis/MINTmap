from mamba import describe, description, context, it, _it, fit  # noqa: F401
from expects import *

import random

from mintmap.sequence import Sequence
from mintmap.annotations import Annotations

with describe(Sequence) as self:
    with before.all:
        path = 'spec/support/tRNAspace.Spliced.Sequences.MINTmap_v1.fa'
        Annotations.load_trna_sequences(path)

    with description('Sequence()'):
        with it('creates a Sequence object'):
            Sequence('GGTAAATATAGTTTAAC')  # doesn't throw an exception

    with description('#annotations_of_a_trna'):
        with context('when a trna sequence starts with trf5ptrunc'):
            with it('contains the expected annotation'):
                s = Sequence('GGTAAATATAGTTTAAC')
                trna_name = 'trnaMT_HisGTG_MT_+_12138_12206'
                actual = s.annotations_of_a_trna(trna_name)
                expected = 'trnaMT_HisGTG_MT_+_12138_12206@-1G.16.17'
                expect(actual).to(contain(expected))

        with context('when a trna sequence contains the sequence'):
            with it('contains the expected annotation'):
                s = Sequence('AGATCAAGAGGTCCCCGG')
                trna_name = 'trna127_CysGCA_1_-_93981834_93981906'
                actual = s.annotations_of_a_trna(trna_name)
                expected = 'trna127_CysGCA_1_-_93981834_93981906@36.53.18'
                expect(actual).to(contain(expected))

    with description('#annotations'):
        with it('returns a populated array with annotation strings'):
            s = Sequence('AGATCAAGAGGTCCCCGG')
            actual = s.annotations
            expected = [
                'trna127_CysGCA_1_-_93981834_93981906@36.53.18',
                'trna26_CysGCA_17_-_37310744_37310815@35.52.18'
            ]
            expect(actual).to(contain(*expected))

    with description('.all_fragments'):
        with context('when all sequeces have the same reads_count'):
            with it('returns sequences ordered by sequence'):
                Sequence.reset()
                expected = ['AA', 'AT', 'CA', 'CT', 'GA', 'GT', 'TA', 'TG']
                shuffled = expected[:]
                random.shuffle(shuffled)
                for s in shuffled:
                    Sequence.all_fragments_index[s] = Sequence(s)
                actual = list(map(lambda i: i.sequence, Sequence.all_fragments))
                expect(actual).to(equal(expected))

        with context('when all sequeces have random reads_count'):
            with it('returns sequences ordered by reads_count'):
                Sequence.reset()
                sequences = ['AA', 'AT', 'CA', 'CT', 'GA', 'GT', 'TA', 'TG']
                random.shuffle(sequences)
                reads_counts = []
                for s in sequences:
                    Sequence.all_fragments_index[s] = Sequence(s)
                    Sequence.all_fragments_index[
                        s].reads_count = random.randint(1,
                                                        1000)
                actual = list(
                    map(lambda i: i.reads_count,
                        Sequence.all_fragments)
                )
                expected = sorted(actual, reverse=True)
                expect(actual).to(equal(expected))
