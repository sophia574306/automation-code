
import re

from apitestframework.utils import parse

if __name__ == '__main__':
        s = """
        {
        "username":"sophia",   "password":"111",
"captcha":"1512", 
"uuid":"qwertttlk"
    }
        """
        res = re.findall(r'\$\{\{(.+?)\((.+?)\)\}\}', s)
        for func in res:
            func_name,func_params = func[0],func[1]
            if hasattr(parse,func_name):
                value = getattr(parse,func_name)(func_params)
                s = re.sub(r'\$\{\{(.+?)\}\}',value,s)
        print(s)
