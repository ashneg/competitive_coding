def almostIncreasingSequence(sequence):
    dff_seq = [x>=y for x, y in zip(sequence[:-1], sequence[1:])]
    if sum(dff_seq) >=2:
        return False
    elif sum(dff_seq) == 0:
        return True
    else:
        ind = dff_seq.index(True)
        t_seq = list(sequence);
        t_seq.pop(ind+1)
        dff_seq1 = [x>=y for x, y in zip(t_seq[:-1], t_seq[1:])]
        t_seq = list(sequence);
        t_seq.pop(ind)
        dff_seq2 = [x>=y for x, y in zip(t_seq[:-1], t_seq[1:])]
        return sum(dff_seq1)<1 or sum(dff_seq2)<1
