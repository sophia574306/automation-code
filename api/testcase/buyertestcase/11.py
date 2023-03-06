from apitestframework import setting
from apitestframework.utils.excel_opetator import read_excel

buy_now_data = read_excel((setting.DIR_NAME + '/data/test_data.xlsx'), '立即购买')
print(buy_now_data)
