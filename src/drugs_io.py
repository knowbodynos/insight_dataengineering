from drugs_transform import split_line, cost_to_string

def read_csv_to_drug_dict(file_name):
    """Read from csv to a dict of dicts given by {drug_name: {prescriber_name: total_cost}}."""
    drug_dict = {}
    with open(file_name, "r") as in_stream:
        header = in_stream.readline()
        for line in in_stream:
            id, prescriber_last_name, prescriber_first_name, drug_name, drug_cost = split_line(line.rstrip('\n'), delimiter=',')
            prescriber_name = '_'.join((prescriber_first_name, prescriber_last_name))
            drug_cost = float(drug_cost)
            if drug_name in drug_dict:
                if prescriber_name in drug_dict[drug_name]:
                    drug_dict[drug_name][prescriber_name] += drug_cost
                else:
                    drug_dict[drug_name][prescriber_name] = drug_cost
            else:
                drug_dict[drug_name] = {prescriber_name: drug_cost}
    return drug_dict


def write_drug_table_to_file(drug_table, file_name):
    """Write table (i.e. list of lists) given by [[drug_name, num_prescriber, total_cost], ...]
    to file, including appropriate header line."""
    with open(file_name, "w") as out_stream:
        out_stream.write("drug_name,num_prescriber,total_cost")
        for drug_name, num_prescriber, total_cost in drug_table:
            total_cost = cost_to_string(total_cost)
            out_stream.write("\n{0},{1},{2}".format(drug_name, num_prescriber, total_cost))