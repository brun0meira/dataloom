import unittest
import os
import pandas as pd
import core.data_processing as data_processing


class TestConvertFunctions(unittest.TestCase):

    def setUp(self):
        self.temp_folder = "temp_test"
        os.makedirs(self.temp_folder, exist_ok=True)

        self.csv_file = os.path.join(self.temp_folder, "test_file.csv")
        df = pd.DataFrame({
            "col1": [1, 2, 3],
            "col2": ["a", "b", "c"]
        })
        df.to_csv(self.csv_file, index=False)

    def tearDown(self):
        if os.path.exists(self.temp_folder):
            for file in os.listdir(self.temp_folder):
                file_path = os.path.join(self.temp_folder, file)
                os.remove(file_path)
            os.rmdir(self.temp_folder)

    # def test_convert_to_parquet(self):
    #     # Testando a função convert_to_parquet
    #     data_processing.convert_to_parquet(self.csv_file, self.temp_folder)

    #     parquet_file = os.path.join(self.temp_folder, "test_file.parquet")
    #     self.assertTrue(os.path.exists(parquet_file), f"Arquivo {parquet_file} não foi criado.")

    #     df_original = pd.read_csv(self.csv_file)
    #     df_parquet = pd.read_parquet(parquet_file)
    #     pd.testing.assert_frame_equal(df_original, df_parquet, check_like=True)

    # def test_convert_to_other_type(self):
    #     # Testando a função convert_to_other_type
    #     data_processing.convert_to_other_type(self.csv_file, self.temp_folder)

    #     json_file = os.path.join(self.temp_folder, "test_file.json")
    #     self.assertTrue(os.path.exists(json_file), f"Arquivo {json_file} não foi criado.")

    #     df_original = pd.read_csv(self.csv_file)
    #     df_json = pd.read_json(json_file)
    #     pd.testing.assert_frame_equal(df_original, df_json, check_like=True)

if __name__ == "__main__":
    unittest.main()
