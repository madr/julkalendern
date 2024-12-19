from collections import deque


def solve(data):
    blocks_checksum = defrag(data)
    files_checksum = defrag(data, True)
    return blocks_checksum, files_checksum


def defrag(data, move_files=False):
    expected_seq_len = sum(map(int, data[::2]))
    seq = dict()
    gaps = dict()
    q = deque([])
    i = 0
    for fileid, pair in enumerate(zip(data[::2], data[1::2] + "0")):
        size, free = map(int, pair)
        q.append((i, fileid, size))
        for _ in range(int(size)):
            seq[i] = fileid
            i += 1
        gaps[i] = free
        i += int(free)
    while q:
        i, fileid, size = q.pop()
        if move_files:
            updated = False
            for pos, space in gaps.items():
                if pos > i:
                    continue
                if size <= space:
                    rem = space - size
                    updated = True
                    break
            if updated:
                for k in range(size):
                    seq[pos + k] = fileid
                for k in range(i, i + size):
                    del seq[k]
                del gaps[pos]
                gaps[pos + size] = rem
                gaps = dict(sorted(gaps.items(), key=lambda x: x[0]))
        else:
            move = False
            for j in range(size):
                for k in range(expected_seq_len):
                    if k not in seq:
                        seq[k] = fileid
                        del seq[i + j]
                        move = True
                        break
            if not move:
                break
    return sum(
        pos * id
        for pos, id in enumerate(seq.get(fileid, 0) for fileid in range(max(seq) + 1))
    )


if __name__ == "__main__":
    with open("./input/09.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
