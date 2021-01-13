"""Assignment 1

Fill in the following function skeletons (deleting the 'raise NotImplementedError' lines as you go) - descriptions are provided in the PDF, and briefly in the docstring (the triple quote thing at the top of each function).

Some assert statements have been provided - write more of them to test your code!
"""

from typing import List, TypeVar


def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built
    in function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if n < 0:
        return -1*n
    else:
        return n
    
    #alternate method
    #x = (n**2)**(1/2)
    #return x
    
    raise NotImplementedError("absolute")

assert absolute(-1) == 1, "absolute of -1 failed"

def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed
    in number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    if n == 0:
        return 1
    else: 
        result = 1
        for i in list(range(1,n+1)):
            result= result*i
        return result
            
        
    raise NotImplementedError("factorial")

assert factorial(4) == 24, "factorial of 4 failed"


T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list,
    starting with the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the
            returned list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    nlst = []
    for i in range(len(lst)): 
        if i%2 == 0:
            nlst.append(lst[i])
    return nlst
            
    raise NotImplementedError("every_other")

assert every_other([1, 2, 3, 4, 5]) == [1,3,5], "every_other of [1,2,3,4,5] failed"

def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list.
    Cannot use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
    result = 0
    for i in lst:
        result = result+i
    
    return result

    raise NotImplementedError("sum_list")

assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"


def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    return sum_list(lst)/len(lst)
    
    raise NotImplementedError("mean")

assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"

def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.
    If the list has an even number of values, it computes the mean of the two
    center values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    if len(lst)%2 == 1:
        x = int(len(lst)/2)
        return float(lst[x])
    else:
        x = int(len(lst)/2)
        return mean([lst[x-1],lst[x]])
    
    raise NotImplementedError("median")

assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it,
    knocking out every third name (wrapping around) until only two names are
    left. In other words, when you hit the end of the list, wrap around and keep
    counting from where you were.

    For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd
    first knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on
    Nathan and 'goose' on Sasha - knocking him out and leaving only Nathan and
    Jennie.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    i = 2
    while len(lst) != 2:
        try:
            lst.pop(i)
            i = i+2
        except:
            i = i - len(lst)
            
    return lst

    raise NotImplementedError("duck_duck_goose")


names = ["sasha", "nathan", "jennie", "shane", "will", "sara"]
assert duck_duck_goose(names) == ["sasha", "will"]

print("All tests passed!")

