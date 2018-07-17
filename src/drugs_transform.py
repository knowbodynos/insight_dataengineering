def split_line(line, delimiter=','):
    """Split a line by a given delimiter, accounting for the 
    fact that that line may contain a quoted string literal with the
    delimiter character that shouldn't be counted as a delimiter."""
    line = line.rstrip('\n')
    fields = []
    field_end = line.find(delimiter)
    while field_end > -1:
        temp_field = line[:field_end]
        line = line[field_end + 1:]
        if temp_field.count('"') % 2 == 1:
            field_end = line.find(delimiter)
            temp_field += delimiter + line[:field_end]
            line = line[field_end + 1:]
        fields.append(temp_field)
        field_end = line.find(delimiter)
    fields.append(line)
    return fields


def cost_to_string(total_cost):
    """If total_cost is an integer, convert to string with no decimal
    places. If it is a float, round to two decimal places (i.e. a dollar amount)."""
    int_total_cost = int(total_cost)
    if total_cost - int_total_cost == 0:
        return str(int_total_cost)
    return "{0:.2f}".format(total_cost)


def drug_dict_to_table(drug_dict):
    """Reshape the dict of dicts into a list of lists by accumulating
    the number of unique prescribers of each drug, and the total cost
    of that drug from all prescribers."""
    drug_table = []
    for drug_name, drug_val in drug_dict.items():
        num_prescriber = 0
        total_cost = 0
        for drug_cost in drug_val.values():
            num_prescriber += 1
            total_cost += drug_cost
        drug_row = [drug_name, num_prescriber, total_cost]
        drug_table.append(drug_row)
    return drug_table


def sort_drug_table(drug_table):
    """Sort the list of lists by first the total cost of all prescriptions
    of each drug, and then if there is a tie, by the drug name."""
    return sorted(drug_table, key = lambda x: (x[2], x[0]), reverse = True)


