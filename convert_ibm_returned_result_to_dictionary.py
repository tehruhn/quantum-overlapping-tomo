

def convert_ibm_returned_result_to_dictionary(returned_result):
    results_dict = {}
    names = []
    for result in returned_result.results:
        temp_name = getattr(getattr(result, 'header', None),'name', '')
        if not temp_name in names:
            names.append(temp_name)
            
    for name in names:
        results_dict[name] = returned_result.get_counts(name)
        
    return results_dict