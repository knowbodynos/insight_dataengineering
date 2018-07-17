import sys
from drugs_io import read_csv_to_drug_dict, write_drug_table_to_file
from drugs_transform import drug_dict_to_table, sort_drug_table

if __name__ == '__main__':
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    drug_dict = read_csv_to_drug_dict(input_file_path)
    drug_table = sort_drug_table(drug_dict_to_table(drug_dict))
    write_drug_table_to_file(drug_table, output_file_path)