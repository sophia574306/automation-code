import yaml
from apitestframework import setting


def load_yaml_file(yaml_file):
    with open(yaml_file,'r',encoding='utf-8') as f:
        yaml_content = yaml.load(f,Loader=yaml.FullLoader)  #yaml读取的用法，下面的方法也ok
        # yaml_content = yaml.load(f.read(),Loader=yaml.FullLoader)
        return yaml_content

if __name__== '__main__':
    print(load_yaml_file(setting.DIR_NAME + '/configs/host_url.yml'))

