def get_slices(row_count, column_count, min_ingredient, max_area, pizza):
    results = []
    for r in range(row_count):
        row = pizza[r]
        beg = 0
        end = 0
        m = 0
        t = 0
        while end < column_count:
            if row[end] == 'M':
                m += 1
            elif row[end] == 'T':
                t += 1
            end += 1
            if end - beg > max_area:
                if row[beg] == 'M':
                    m -= 1
                elif row[beg] == 'T':
                    t -= 1
                beg += 1
            if (end - beg <= max_area and m >= min_ingredient and t >= min_ingredient):
                results.append((r, beg, r, end - 1))
                beg = end
                t = 0
                m = 0
    return results
