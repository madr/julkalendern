import functools


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
                print(f" {part_index}) {formatted}")
            return answer

        return wrapper_aoc

    return decorator_aoc


def headline(n, title):
    print(f"\n--- Day {n}: {title} ---\n")
