import functools


def puzzleinput(n, **kwargs):
    filename = str(n).zfill(2)
    trim_input = kwargs.get("trim_input", True)
    filepath = f"./input/{filename}.txt"

    def decorator_pi(func):
        @functools.wraps(func)
        def wrapper_pi(*args, **kwargs):
            with open(filepath, "r") as f:
                data = f.read()
                if trim_input:
                    return func(data.strip(), *args, **kwargs)
                return func(data, *args, **kwargs)

        return wrapper_pi

    return decorator_pi


def answer(part_index, fmt_string):
    def decorator_aoc(func):
        @functools.wraps(func)
        def wrapper_aoc(*args, **kwargs):
            decorate = kwargs.get("decorate", False)
            if decorate:
                del kwargs["decorate"]
            answer = func(*args, **kwargs)
            if not decorate:
                print(answer)
            else:
                formatted = fmt_string.format(answer)
                print(f"[part {part_index}] {formatted}")
            return answer

        return wrapper_aoc

    return decorator_aoc


def headline(n, title):
    title = f"Day {n}: {title}"
    print("\n".join(["", title, "".join("-" for _ in title), ""]))
