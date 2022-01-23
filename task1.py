def files_to_dictionary(common_name_dict, synonyms_dict, common_name_file_path, synonyms_name_file_path):
    with open(common_name_file_path, 'r') as name_file:
        with open(synonyms_name_file_path, 'r') as synonyms_file:
            common_name = name_file.read().split(',')
            for x in common_name:
                common_name_dict[x[0: x.index('(') - 1].strip()] = int(x[x.index('(') + 1:x.index(')')])
            synonyms = synonyms_file.read().split("), (")
            for synonym in synonyms:
                synonyms_dict[synonym.replace('(', '').replace(')', '').split(',')[0].strip()] = \
                    synonym.replace('(', '').replace(')', '').split(',')[1].strip()


def calculate_the_real_amount(common_name_dict, synonyms_dict):
    for key in synonyms_dict:
        if key in common_name_dict:
            sum = common_name_dict[key]
            common_name_to_remove = []
            synonym_key = synonyms_dict[key]
            if synonym_key in common_name_dict:
                sum += common_name_dict[synonym_key]
                common_name_to_remove.append(synonym_key)
                while synonym_key in synonyms_dict:
                    synonym_key = synonyms_dict[synonym_key]
                    if synonym_key in common_name_dict:
                        sum += common_name_dict[synonym_key]
                        common_name_to_remove.append(synonym_key)
            common_name_dict[key] = sum
            for k in common_name_to_remove:
                common_name_dict.pop(k)
    print(common_name_dict)


def main():
    common_name_dict = {
    }
    synonyms_dict = {
    }
    files_to_dictionary(common_name_dict, synonyms_dict, 'common_name.txt', 'Synonyms.txt')
    calculate_the_real_amount(common_name_dict, synonyms_dict)


if __name__ == "__main__":
    main()
