import unittest
import numpy as np

from Library import get_input_array

class RecordSplitterTest(unittest.TestCase):
    # Construct the class variable
    def setUp(self): 
        self.valid_record_size=1000000
        self.output_batch_size=5000000
        self.output_record_number=500
        self.invalid_response_template="The input is empty/invalid"
        self.sample_data_address='Test/test_data/Book1.csv'
    
    # Create an array of records from a sample csv file.
    def create_few_records(self):
        with open(self.sample_data_address) as file:
            input_small_array=[]
            for i in file:
                input_small_array.append(i+",")
        return(input_small_array)
    
    # Create an array and then append records from a 
    # sample csv file until it meets the 1mb record size
    def create_large_record(self):
        large_record=[]
        large_record=np.array(large_record)
        
        record=self.create_few_records()
        large_record=np.append(large_record, record)

        while (large_record.nbytes<self.valid_record_size):
            large_record=np.append(large_record, record)
        return (large_record)

    # (to be completed)
    def create_large_batch(self):
        pass
# --------------------------------------------------------------
    '''
    Test cases 
    '''
    
    def test_empty_input(self):
        empty_response=get_input_array([])
        self.assertEqual(empty_response,self.invalid_response_template)

    def test_invalid_input(self):
        invalid_response=get_input_array(1)
        self.assertEqual(invalid_response, self.invalid_response_template)

    def test_one_small_record(self):
       success_response=get_input_array(["only one record"])
       self.assertEqual(len(success_response), 1)
    
    def test_few_records(self):
        input_array=self.create_few_records()
        success_response=get_input_array(input_array)
        self.assertEqual(success_response, input_array)
    
    # (to be completed)
    def test_one_large_record(self):
        large_record=self.create_large_record()
        empty_array=get_input_array(large_record, summary=True)

    # (to be completed)
    def test_heavy_file(self):
        pass

    # (to be completed)
    def test_many_record(self):
        pass