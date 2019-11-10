import sys
from typing import Any, Tuple


def _is_rgb_tuple(item: Any) -> bool:
    return isinstance(item, Tuple) \
        and len(item) == 3 \
        and all((isinstance(x, int) and 0 <= x <= 255)
                for x in item)


def printc(*args, color=15, file=sys.stdout, **kwargs):
    """Print text in one of 16 base colors, or in any RGB color

    Colors are only added if the output is to stdout and not
    piped or redirected.

    Colors:
        0 - black       8 - brightblack
        1 - red         9 - brightred
        2 - green      10 - brightgreen
        3 - yellow     11 - brightyellow
        4 - blue       12 - brightblue
        5 - magenta    13 - brightmagenta
        6 - cyan       14 - brightcyan
        7 - white      15 - brightwhite (default)

    Colors:
        (0, 0, 0) - black ...               ...
        ...               ...               ...
        ...               ...   (255, 255, 255) - white
    """
    is_base = isinstance(color, int) and color in range(16)
    is_rgb = _is_rgb_tuple(color)

    if not is_base and not is_rgb:
        raise ValueError('color has to be a number in range 0..15'
                         ' or a tuple of 3 integers in range 0..255')

    if color != 15 and file is sys.stdout and sys.stdout.isatty():
        args = list(args)
        if is_base:
            args[0] = f"\033[38;5;{color}m{args[0]}"
        else:
            color = ";".join(map(str, color))
            args[0] = f"\033[38;2;{color}m{args[0]}"
        args[-1] = f"{args[-1]}\033[0m"

    print(*args, file=file, **kwargs)


def main():
    import argparse
    from printc import demos

    demo_funs = [item for item in dir(demos) if item.startswith("demo_")]

    parser = argparse.ArgumentParser()
    parser.add_argument("--color", "-c", help="[0..15]", type=int, default=15,
                        required=False)
    parser.add_argument("--demo", required=False, default=None, type=int,
                        choices=range(len(demo_funs)), help="print some colors")
    parser.add_argument("-n", action="store_true", required=False,
                        default=False, help="do not output the trailing newline")
    parser.add_argument("text", nargs="*")
    args = parser.parse_args()

    if args.demo is not None:
        try:
            getattr(demos, demo_funs[args.demo])()
        except KeyboardInterrupt:
            pass
        finally:
            print()

    if args.text:
        if args.n:
            printc(*args.text, color=args.color, end="")
        else:
            printc(*args.text, color=args.color)


if __name__ == '__main__':
    main()
