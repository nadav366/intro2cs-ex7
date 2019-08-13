from ex7 import *
import itertools
import math
import io
import contextlib


def capture_print(fun):
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        fun()
    retval = f.getvalue().strip().split("\n")
    if retval == [""]:
        return []
    return retval


def test_print_to_n():
    assert capture_print(lambda: print_to_n(0)) == []
    assert capture_print(lambda: print_to_n(10)) == [str(i) for i in
                                                     range(1, 11)]
    assert capture_print(lambda: print_to_n(1)) == ["1"]


def test_print_reversed():
    assert capture_print(lambda: print_reversed(0)) == []
    assert capture_print(lambda: print_reversed(10)) == [str(i) for i in
                                                         range(10, 0, -1)]
    assert capture_print(lambda: print_reversed(1)) == ["1"]


def test_factorial():
    for i in range(10):
        assert fact(i) == math.factorial(i)


def test_exp():
    for x in range(100):
        mine = exp_n_x(200, x)
        their = math.exp(x)
        assert math.isclose(mine, their)


def test_is_prime():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79,
              83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
              151, 157, 163, 167,
              173, 179, 181, 191, 193, 197, 199]
    not_primes = set(range(200)) - set(primes)
    assert all(is_prime(i) for i in primes)
    assert all(not is_prime(i) for i in not_primes)


def test_sequences_with_repetitions():
    alphabet = "abcdefgh"
    for n in range(1, len(alphabet)):
        correct_set = {"".join(tup) for tup in
                       itertools.product(alphabet, repeat=n)}
        my_set = set(capture_print(lambda: print_sequences(alphabet, n)))
        assert correct_set == my_set


def test_sequences_no_repetitions():
    alphabet = "abcdefgh"
    for n in range(1, len(alphabet) + 1):
        correct_set = {"".join(tup) for tup in
                       itertools.permutations(alphabet, n)}
        my_set = set(
            capture_print(lambda: print_no_repetition_sequences(alphabet, n)))
        assert correct_set == my_set


def test_parentheses():
    # a correct solution from stack overflow
    def compute_all_parens(n):
        def compute_parens(left, right, s):
            if right == n:
                yield s
                return
            if left < n:
                yield from compute_parens(left + 1, right, s + "(")
            if right < left:
                yield from compute_parens(left, right + 1, s + ")")

        yield from compute_parens(0, 0, "")

    for input in range(1, 11):
        assert set(compute_all_parens(input)) == set(parentheses(input))


def test_up_right():
    assert set(capture_print(lambda: up_and_right(2, 1))) == {
        "rru", "urr", "rur"
    }


def test_flood_fill():
    begin_image = [['*', '*', '*', '*', '*'],
                   ['*', '.', '*', '.', '*'],
                   ['*', '.', '*', '.', '*'],
                   ['*', '*', '*', '*', '*']
                   ]

    end_image = [['*', '*', '*', '*', '*'],
                 ['*', '*', '*', '.', '*'],
                 ['*', '*', '*', '.', '*'],
                 ['*', '*', '*', '*', '*']
                 ]

    flood_fill(begin_image, (1, 1))
    assert begin_image == end_image