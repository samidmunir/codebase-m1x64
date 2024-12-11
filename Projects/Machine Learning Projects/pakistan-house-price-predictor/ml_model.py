import matplotlib.pyplot as PLT
import numpy as NP
import pandas as PD
import seaborn as SNS

"""
    function read_data(filename: str) -> PD.DataFrame
"""
def read_data(filename: str) -> PD.DataFrame:
    print(f'\nread_data({filename}) called -->')
    print(f'\treading data from <{filename}>...')
    data = PD.read_csv(filepath_or_buffer = filename, sep = '|')
    return data

def print_data_info(data: PD.DataFrame) -> None:
    print('\nprint_data_info() called -->')
    print('\tData Info:')
    print('\t', data.info())
    
def main() -> None:
    DATA_FILENAME = 'data.csv'
    DATA = read_data(DATA_FILENAME)
    
    print_data_info(DATA)
    
if __name__ == '__main__':
    main()