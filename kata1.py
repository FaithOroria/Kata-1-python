def largest_lexicographic_string(S):
    S = list(S)  

    y = 0
    while y < len(S) - 1:
        if int(S[y]) + int(S[y + 1]) <= 9:
            S[y:y + 2] = str(int(S[y]) + int(S[y + 1]))  
            y = max(0, y - 1)  
        else:
            y += 1  

    return ''.join(S)

print(largest_lexicographic_string("32581")) 
print(largest_lexicographic_string("1119812"))  
