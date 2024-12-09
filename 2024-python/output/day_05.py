from output import ints


def solve(data):
    rules, pagelists = data.split("\n\n")
    rules, pagelists = (
        set(map(lambda line: tuple(ints(line)), rules.splitlines())),
        list(map(lambda line: ints(line), pagelists.splitlines())),
    )
    corrects = []
    incorrects = []
    adjusted = []
    for pagelist in pagelists:
        ok = True
        for i, page in enumerate(pagelist):
            prevpages, nextpages = pagelist[:i], pagelist[i + 1 :]

            if not all((pp, page) in rules for pp in prevpages) or not all(
                (page, np) in rules for np in nextpages
            ):
                ok = False
                break
        if ok:
            corrects.append(pagelist)
        else:
            incorrects.append(pagelist)
    while incorrects:
        pagelist = incorrects.pop(0)
        changed = False
        for i, page in enumerate(pagelist):
            prevpages, nextpages = pagelist[:i], pagelist[i + 1 :]
            for prevpage in prevpages:
                if (prevpage, page) in rules:
                    continue
                nextpages.append(prevpages.pop())
                pagelist = prevpages + [page] + nextpages
                changed = True
                break
            if not changed:
                for nextpage in nextpages:
                    if (page, nextpage) in rules:
                        continue
                    prevpages.append(nextpages.pop())
                    pagelist = prevpages + [page] + nextpages
                    changed = True
                    break
            if changed:
                break
        if not changed:
            adjusted.append(pagelist)
        else:
            incorrects.append(pagelist)
    p1 = sum(c[len(c) // 2] for c in corrects)
    p2 = sum(r[len(r) // 2] for r in adjusted)
    return p1, p2


if __name__ == "__main__":
    with open("./input/05.txt", "r") as f:
        inp = f.read().strip()

    p1, p2 = solve(inp)

    print(p1)
    print(p2)
