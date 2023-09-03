import pstats
from pstats import SortKey


def main():
    p = pstats.Stats("fib_stats")
    # p.strip_dirs().print_stats()
    # p.strip_dirs().sort_stats(SortKey.NAME).print_stats()
    # p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
    # p.strip_dirs().sort_stats(SortKey.CALLS).print_stats()
    p.strip_dirs().sort_stats(SortKey.CALLS).print_stats("main")


if __name__ == "__main__":
    main()
