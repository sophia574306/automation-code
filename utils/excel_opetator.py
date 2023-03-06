import pandas as pd
from apitestframework import setting


def read_excel(filename,sheetname):
    sexcelfile = pd.read_excel(filename,sheetname,engine='openpyxl',keep_default_na=False)
    nrows = sexcelfile.shape[0]
    ncolumns = sexcelfile.shape[1]
    test_data = []
    for i in range(nrows):
        # data = []
        data = ()
        for j in range(ncolumns):
            data = data + (sexcelfile.iloc[i,j],)
        test_data.append(data)
    return test_data


if __name__ == "__main__":
    print(read_excel(setting.DIR_NAME + '/utils/mtxs_keywords.xlsx', '登录'))
