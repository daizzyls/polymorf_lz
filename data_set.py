import os

import pandas as pd


class DataProcessing:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.data_set = {}
        self.delete_duplicates = {}
        self.total_deleted = 0

    def split(self):
        column = "Участники гражданского оборота"
        output_dir = "output"
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        saved_files = {}
        for value, subset in self.data.groupby(column):
            safe_name = str(value).replace(".", "").replace(" ", "_")
            file_name = f"data_set_{safe_name}.csv" 
            full_path = os.path.join(output_dir, file_name)

            subset.to_csv(full_path, index=False, encoding="utf-8-sig")
            self.data_set[str(value)] = subset
            saved_files[str(value)] = full_path
            
        return saved_files

    def __neg__(self):
        self.delete_duplicates = {}
        

        dup = self.data_set if self.data_set else {'all': self.data}
        new_data_set = {}
        
        for name, df in dup.items():
            first = len(df)
            df_remove = df.drop_duplicates().reset_index(drop=True)
            
            
            self.delete_duplicates[name] = first - len(df_remove)
            new_data_set[name] = df_remove 

        if "all" in new_data_set:
            self.data = new_data_set["all"]
        else:
            self.data_set = new_data_set

        self.total_deleted = sum(self.delete_duplicates.values())
        return self.delete_duplicates