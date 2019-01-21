def count_ephemeral(n1,n2,k):
    ephemerals = 0
    list =[]
    for n in range(n1,n2):
        # print(n)
        numstring = str(n)
        sequence = []

        repeated = 0
        sum = 0
        while 1 not in sequence and repeated == 0:
            digits=[]
            # print('looping')
            sequence.append(sum)
            # print(sequence)
            if sequence.count(sum) > 1:
                # print('repeat')
                repeated = 1
            sum = 0
            for i in range(0,len(numstring)):
                digits.append(numstring[i])
                # print(digits)
            for j in range(0,len(digits)):
                sum += int(digits[j])**k
            numstring = str(sum)
            # print(numstring)
            if 1 in sequence:
                list.append(n)
                ephemerals += 1
    # print(list)
    return ephemerals


