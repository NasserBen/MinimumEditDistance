def minEditDistance(x: str, y: str):
    len_x = len(x)
    len_y = len(y)
    table = []
    
    # Create an (m+1) x (n+1) table
    for i in range(len_x + 1): 
        row = []
        for j in range(len_y + 1):
            row.append(0)
        table.append(row)

    # Fill out the first column with indices
    for i in range(1, len_x + 1):
        table[i][0] = i
    
    # Fill out the first row with indices
    for j in range(1, len_y + 1):
        table[0][j] = j
    
    for i in range(1, len_x + 1):
        for j in range(1, len_y + 1):
            if x[i - 1] == y[j - 1]: # If the characters are the same, choose the top-left corner value
                table[i][j] = table[i - 1][j - 1]
            else:
                substitute_cost = table[i - 1][j - 1] + 1
                delete_cost = table[i - 1][j] + 1
                insert_cost = table[i][j - 1] + 1
                
                min_cost = min(substitute_cost, delete_cost, insert_cost) # Recurrence relation
                table[i][j] = min_cost
                
                if min_cost == insert_cost:
                    print(f"Insert \"{y[j - 1]}\"")
                elif min_cost == delete_cost:
                    print(f"Delete \"{x[i - 1]}\"")
                elif min_cost == substitute_cost:
                    print(f"Substitute \"{x[i - 1]}\" into \"{y[j - 1]}\"")
               
    return table[len_x][len_y]

x = input()
y = input()
print("Minimum edit distance:" + str(minEditDistance(x, y)))