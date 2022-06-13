def FuncLD(s,t):
    n,m = len(t), len(s)
    q0 = [0]*(n+1)
    q1 = [0]*(n+1)

    for i in range(n):
        q0[i] = i
    for i in range(m):
        q1[0] = i+1
        for j in range(n):
            deletionCost = q0[j+1]+1
            insertionCost = q1[j]+1
            if s[i] == t[j]:
                substitutionCost = q0[j]
            else:
                substitutionCost = q0[j]+1

            q1[j+1] = min(deletionCost, insertionCost, substitutionCost)

        q0, q1 = q1, q0
    return q0[n]


