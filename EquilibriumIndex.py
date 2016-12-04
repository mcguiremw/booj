# Sites used:
#   - https://rosettacode.org/wiki/Equilibrium_index#Python
#   - https://docs.python.org/2/library/functions.html#xrange
#   - http://www.geeksforgeeks.org/equilibrium-index-of-an-array/

# I have studied this problem in school and remember solving it by
#   splitting the list at a moving index and comparing the sum of both sides
#   of the list.
#
# I used the resources above to confirm my thoughts on solving
#   the problem and researching xrange()


def eqindex(data):
    # do code here
    return filter(None, [i if (sum(data[:i]) == sum(data[i + 1:])) else None
                         for i in xrange(len(data))])
