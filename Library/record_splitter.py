import numpy as np
import logging


'''
Define global variables
These values are given in the assignment.
'''
valid_record_size=1000000
output_batch_size=5000000
output_record_number=500
empty_input_respoonse="The input is empty/invalid"
# -------------------------------------------------

# To understand if the input has the proper data type(i.e. array) and it is not empty.
def check_input_status(input_array):
    input_iterable, input_length =False, False
    if hasattr(input_array, '__iter__'):input_iterable=True
    if (np.size(input_array)!=0):input_length=True
    return(input_iterable, input_length)

# To check output batch is 5mb and number of records is 500.
def input_records_status(input_array):
    many_records, heavy_file= False, False
    if (input_array.size > output_record_number):many_records=True
    if (input_array.nbytes > output_batch_size):heavy_file=True
    return (many_records, heavy_file)

# Discard record that is larger than 1mb .
def discard_large_record(input_array):
    number_record_discarded=0
    allowed_record_size=valid_record_size

    for record in input_array:
            if (record.nbytes > allowed_record_size):
                index=np.where(input_array==record)
                input_array=np.delete(input_array,index)
                number_record_discarded+=1
    return (input_array, number_record_discarded)

# Split input array to 5mb size.
def chunk_heavy_file(input_array):
    chunk=input_array.nbytes/output_batch_size
    input_array=np.array_split(input_array, chunk)
    return (input_array)

# -------------------------------------------------

'''
The __main__ Function.

It takes input (array) and boolean summary. 
Summary is supposed to show the number of records which are larger than 1mb in log file(to be completed).
'''


def get_input_array(input, summary=False):
    
    output_array=[]
    temp_array=[]
    
    input_iterable, input_length= check_input_status(input)
    
    # Check if the input is acceptable.
    if (input_iterable==True and input_length==True):

        input_array=np.array(input)
        input_array, number_record_discarded=discard_large_record(input_array)
        many_records,heavy_file= input_records_status(input_array)
        
        # logging.info could be used to get the number(to be completed).
        if(summary==True ):print(f'{number_record_discarded} record discarded') 
        
        if heavy_file==True:
            input_array=chunk_heavy_file(input_array)
        
        # If input has more than 500 records, 
        # it creats a list and extend 499 records then append to the output array.
        # Otherwise append to the output directly.
        if many_records==True:
            for record in input_array:
                if(len(temp_array) < output_record_number-1):
                    temp_array.extend(record)
                else:
                    temp_array.extend(record)
                    output_array.append(temp_array)
                    temp_array=[]
            output_array.append(temp_array)
            return (output_array)
        else: 
            for record in input_array:
                output_array.append(record)
            return(output_array)

    else:
        return(empty_input_respoonse)