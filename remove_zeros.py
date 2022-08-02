"""Write an algorithm that takes an array and moves all of the zeros to the end, preserving the
order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def remove_zeros():
    lst = [1, 0, 1, 2, 0, 1, 3]
    new_lst = [num for num in lst if num != 0]
    zeros = [num for num in lst if num == 0]
    return new_lst + zeros


print(remove_zeros())
