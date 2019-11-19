def shot_count_from_dict_of_results(dict_of_results):
    first_dict = dict_of_results[next(iter(dict_of_results))]
    total = 0
    for value in first_dict.values():
        total += value
    return total
