def find_pattern(code_list, target_num):
    matching_positions = []
    for code in code_list:
        if target_num in code:
            matching_positions.append(code.index(target_num))
    return matching_positions
