def SumRange(A, B):
    if A < B:
        S = (A+B)*(B-A+1)/2
        return S
    else:
        return 0
        
print(SumRange(1, 10)+SumRange(10, 15))