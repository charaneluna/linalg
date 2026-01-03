def exchange_row(M,i,j):
    M[i], M[j]= M[j], M[i]


def scale(M,i,k):
    M[i]=[e*k for e in M[i]]

def combine(M,i,j,k):
    M[i]=[M[i][n]+M[j][n]*k for n in range(len(M[i]))]
