def hash_quadratic(d):
    """given a list d of integers returns a list of length 19
    describing the hash table obtained when the hash function
    h(k)= 6k+3 mod 19 is applied to each integer k in d"""
    # initialize table
    table = ["-"] * 19
    # consider each integer k in the input
    for k in d:
        # if k is already in the table this is a duplicate so move to next integer in the input
        # note this check for a duplicate is using the functionality of python rather than checking using a linear probe
        if k in table:
            continue
        # apply the hash function
        i = (6 * k + 3) % 19
        # initialize count that checks whether linear probe has considered each bucket and is now full
        count = 0
        # while bucket is already filled
        while table[i] != "-":
            # move to next bucket
            i = (i + (count + 1) ^ 2) % 19
            # increment count
            count += 1
            # if table is full
            if count == 18:
                # can return table as nothing further can be added
                return table
        # table[i] is empty so k can be added here
        table[i] = k
    # now each part of the input has been considered return the table
    return table


def hash_double(d):
    """given a list d of integers returns a list of length 19
    describing the hash table obtained when the hash function
    h(k)= 6k+3 mod 19 is applied to each integer k in d"""
    # initialize table
    table = ["-"] * 19
    # consider each integer k in the input
    for k in d:
        # if k is already in the table this is a duplicate so move to next integer in the input
        # note this check for a duplicate is using the functionality of python rather than checking using a linear probe
        if k in table:
            continue
        # apply the hash function
        i = (6 * k + 3) % 19
        # initialize count that checks whether linear probe has considered each bucket and is now full
        count = 0
        s = 11 - (k % 11)
        # while bucket is already filled
        while table[i] != "-":
            # move to next bucket
            i = (i + (count + 1) * s) % 19
            # increment count
            count += 1
            # if table is full
            if count == 18:
                # can return table as nothing further can be added
                return table
        # table[i] is empty so k can be added here
        table[i] = k
    # now each part of the input has been considered return the table
    return table
