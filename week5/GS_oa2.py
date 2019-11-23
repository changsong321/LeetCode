def girdGame(grid, k, rules):
    rules = [1 if rule == 'alive' else 0 for rule in rules]
    for rnd in range(k):
        new_grid = []
        for i in range(len(grid)):
            new_grid_row = []
            for j in range(len(grid[i])):
                node_cnt = 0
                for k in range(3):
                    for l in range(3):
                        if k == 1 and l == 1:
                            continue
                        if 0 <= i + (k-1) < len(grid) and 0 <= j + (l-1) < len(grid[i]):
                            node_cnt += grid[i+(k-1)][j+(l-1)]
                new_grid_row.append(rules[node_cnt])
            new_grid.append(new_grid_row)
        grid = new_grid
    return grid