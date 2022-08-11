#  read file with pandas from excel
#  should be run in python3
#  should be return unique email address

import pandas as pd

def read_excel_file():
    df = pd.read_excel('data.xls')
    return df['email'].unique()
    
if __name__ == '__main__':
    datos = read_excel_file()    
    print(datos)