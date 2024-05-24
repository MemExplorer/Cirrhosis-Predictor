class ClassifierBase:
    def __init__(self, id):
        self.__str_id = id

    def get_str_id(self):
        return self.__str_id
    
    def classify_data(self, unique_col_names, data_list, result_data_list):
        raise "Unreachable"
    
    def get_classifier(self, input_data):
        raise "Unreachable"

#classifier for labeled data
class NominalClassifier(ClassifierBase):
    def __init__(self, id):
        super().__init__(id)

        #returns dictionary table with counted data
    def classify_data(self, unique_col_names, data_list, result_data_list):
        #initialze empty data table
        tmp_dict = {}
        for i in range(len(data_list)):
            if data_list[i] not in tmp_dict:
                tmp_dict[data_list[i]] = [0] * len(unique_col_names)
            current_col_index = unique_col_names.index(result_data_list[i])
            tmp_dict[data_list[i]][current_col_index] += 1

        return tmp_dict
    
    def get_classifier(self, input_data):
        return input_data