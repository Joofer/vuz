def ShiftRight3(A, B, C):
    TEMP = B
    B = A
    A = C
    C = TEMP
    return A, B, C
    
print(ShiftRight3(1, 2, 3))