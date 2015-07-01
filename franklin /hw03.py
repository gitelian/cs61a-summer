def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n 
    else: 
        return g(n - 1) + 2*g(n - 2) + 3*g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n 
    else: 
        glll = 1 
        gll = 2
        gl = 3  
        for i in range(4, n+1):
            g_result = gl + 2*gll + 3*glll
            glll = gll
            gll = gl 
            gl = g_result 
        return g_result 

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"
    # Would be easy if I can subscript into numbers. 
    # It's possible if I just make them strings like this:
    strk = str(k)
    if not strk:
        return False
    elif strk[0] == '7':
        return True 
    elif len(strk) == 1:
        return False 
    else:
        return False or has_seven(int(strk[1:]))



def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    # can use def but not assignment! 
    
    #trying iterative soln first
    # cur = 1 
    # inc = 1 
    # for k in range(1, n):  
    #     if k % 7 == 0 or has_seven(k):
    #         inc = -inc
    #     cur = cur + inc 
    # return cur  

    # recursive soln
    def recur_pingpong(cur, inc, k):
        if k == n:
            return cur 
        elif k % 7 == 0 or has_seven(k):
            return recur_pingpong(cur - inc, -inc, k + 1)
        else:
            return recur_pingpong(cur + inc, inc, k + 1)

    return recur_pingpong(1, 1, 1)



def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    coinset = [2**x for x in range(0, amount) if 2**x <= amount]

    def count_change_recur(amount, coinset):
        if amount == 0:
            return 1 
        elif amount > 0 and coinset: 
            return (count_change_recur(amount, coinset[1:]) + 
            count_change_recur(amount - coinset[0], coinset))
        else:
            return 0

    return count_change_recur(amount, coinset) 


def towers_of_hanoi(n, start, end):
    # To move n disks from A to C: 
    # move n-1 top disks to B, 
    # move nth disk to C, 
    # move n-1 disks from B to C

    # if n is odd go from A to C 
    # if n is even go from A to B 
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    prefix = 'Move the top disk from rod '
    infix = ' to rod '
    if n == 1:
        print(prefix + str(start) + infix + str(end))
    else: 
        A = start
        # Figure out which pole is free to store disks on 
        B = list(set([1, 2, 3]) - set([start, end]))[0] 
        C = end 
        towers_of_hanoi(n - 1, A, B)
        towers_of_hanoi(1, A, C)
        towers_of_hanoi(n - 1, B, C)
    return 


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'
