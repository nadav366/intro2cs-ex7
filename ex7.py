EMPTY_STRING = ""

OPENER = "("
CLOSER = ")"

UP = "u"
RIGHT = "r"

EMPTY = "."
FULL = "*"


def print_to_n(n):
    """
    Recursive function, prints all numbers up to n in ascending order
    :param n: int number
    :return: None
    """
    if n > 1:
        print_to_n(n-1)
    if n >= 1:
        print(n)


def print_reversed(n):
    """
    Recursive function, prints all numbers up to n in descending order
    :param n: int number
    :return: None
    """
    if n >= 1:
        print(n)
    if n > 1:
        print_reversed(n-1)


def is_prime(n):
    """
    A function that checks if number is prime
    :param n: int number
    :return: Boolean, whether the number is prime
    """
    if n <= 1:
        return False
    return not has_divisor_smaller_then(n, int(n**0.5))


def has_divisor_smaller_then(n, i):
    """
    A recursive function that checks whether the number has a divisor smaller
    then another number
    :param n: int number, to check if divisible by i
    :param i: int number, to check whether divides n
    :return: Boolean, does n have a divisor smaller then i
    """
    if n % i == 0 and i > 1:
        return True
    if i > 2:
        return has_divisor_smaller_then(n, i-1)
    return False


def exp_n_x(n, x):
    """
    A recursive function that calculates the exponential amount
    :param n:
    :param x:
    :return:
    """
    if n <= 0:
        return (x ** n) / fact(n)
    else:
        return (x ** n) / fact(n) + exp_n_x(n-1, x)


def fact(n):
    """
    Recursive function calculates the n! (factorial)
    :param n: int number
    :return: int number (n!)
    """
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    A recursive function that plays the game "hanoi towers"
    :param hanoi: An object that represents the graphical interface
    :param n: An integer, the number of disks to be moved from tower to tower
    :param src: Represents the tower from which it is transferred
    :param dest: Represents the tower you want move to
    :param temp: Represents the spire tower
    :return: None
    """
    if n == 1:
        hanoi.move(src, dest)
    elif n > 1:
        play_hanoi(hanoi, n-1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)


def print_sequences(char_list, n, str=EMPTY_STRING):
    """
    Recursive function that prints the whole length-n string with values
     ​​from the list
    :param char_list: List of characters
    :param n: The length of the strings you want
    :param str: optional. A string that is up to this step is running.
    Default is empty string.
    :return: None
    """
    if n <= 0:
        if str == EMPTY_STRING:  # Check if n is smaller than one
            return
        print(str)
        return
    for char in char_list:
        print_sequences(char_list, n-1, str+char)


def print_no_repetition_sequences(char_list, n, str=EMPTY_STRING):
    """
    Recursive function that prints the whole length-n string with values ​​
    from the list, No rehearsals.
    :param char_list: List of characters
    :param n: The length of the strings you want
    :param str: optional. string, Print value up to this step is running.
    Default is empty string.
    :return: None
    """
    if n <= 0:
        if str == EMPTY_STRING: # Check if n is smaller than one
            return
        print(str)
        return
    for char in char_list:
        if char not in str:
            print_no_repetition_sequences(char_list, n-1, str+char)


def parentheses(n):
    """
    A function that prints all valid strings of n parentheses pairs
    :param n: Integer number, number of pairs
    :return: list whit all valid strings of n parentheses pairs
    """
    lst = []
    if n <= 0:  # Check if n is smaller than one
        return lst
    return parentheses_helper(n, n, EMPTY_STRING, lst)


def parentheses_helper(open_to_fill, close_to_fill, stri, lst):
    """
    A recursive auxiliary function to the parentheses function.
    Adds a parenthesis string legally, depending on the quantity given.
    When the string length is correct, print it.
    :param open_to_fill: The number of openings that must be filled
    :param close_to_fill: The amount of casings to fill
    :param stri: string, Print value up to this step is running.
    :param lst: list, Collects all the appropriate combinations
    :return:list whit all valid strings of n parentheses pairs
    """
    if open_to_fill > 0:
        lst = parentheses_helper(open_to_fill - 1,
                                 close_to_fill, stri + OPENER, lst)
    if close_to_fill > open_to_fill:
        lst = parentheses_helper(open_to_fill,
                                 close_to_fill - 1, stri + CLOSER, lst)

    if open_to_fill == 0 and close_to_fill == 0:
        lst.append(stri)
    return lst


def up_and_right(n, k, stri=EMPTY_STRING):
    """
    Recursive function, prints all possible ways from (0,0) to (n, k)
    adding them to a string.
    :param n: The number of steps there is another go right
    :param k: The number of steps there is another go up
    :param stri: optional. string, Print value up to this step is running.
    Default is empty string.
    :return: None
    """
    if n > 0:
        up_and_right(n-1, k, stri + RIGHT)
    if k > 0:
        up_and_right(n, k-1, stri + UP)

    if n == 0 and k == 0:
        if stri == EMPTY_STRING:
            return
        print(stri)


def flood_fill(image, start):
    """
    A recursive function that "fills" all the empty cells
    attached to the opening chamber.
    :param image: List of lists, represents a image
    :param start: tuple, coordinates of the starting point in the image
    :return: None
    """
    image[start[0]][start[1]] = FULL

    if image[start[0]-1][start[1]] == EMPTY:
        flood_fill(image, (start[0]-1, start[1]))
    if image[start[0]+1][start[1]] == EMPTY:
        flood_fill(image, (start[0]+1, start[1]))
    if image[start[0]][start[1]-1] == EMPTY:
        flood_fill(image, (start[0], start[1]-1))
    if image[start[0]][start[1]+1] == EMPTY:
        flood_fill(image, (start[0], start[1]+1))

