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
    # Creating the list to return
    equilibrium_indices = []
    # Using xrange to save memory with very large lists
    for i in xrange(len(data)):
        # Logic to compare the sum of the two sublists, 'i' is the index that
        #   will be recorded as the equilibrium since it is not included in the
        #   sum  of the left sublist.
        if sum(data[:i]) == sum(data[i + 1:]):
            # When the two sublists are equal append 'i' to the list being
            #   returned.
            equilibrium_indices.append(i)
    return equilibrium_indices
