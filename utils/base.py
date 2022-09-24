# _*_ coding:utf-8 _*-
# @Time：2022/9/21 22:14
# 作者：qianwulin
from configparser import ConfigParser
from conf.const import CONF_PATH, join


class ConfFile:
    def __init__(self):
        self.config = ConfigParser()

    def read_conf(self, paths, section, keys):
        self.config.read(paths)
        value = self.config.get(section, keys)
        return value

    def set_conf(self,):
        # # 将数据写入到ini文件中
        # config.add_section('login')  # 首先添加一个新的section
        # config.set('login', 'username', 'admin')  # 写入数据
        # config.set('login', 'password', '123456')  # 写入数据
        # config.write(open(path, 'a'))  # 保存数据
        pass
        # 读取ini文件中所有的section
        # section = config.sections()
        # print(section)

def get_env(envs="env"):
    """
    通过setup.ini配置文件，读取需要运行的env（boe,ppe,online）和分支变量，待完善部分
    :return:
    """
    paths = join(CONF_PATH, "conf.ini")
    value = ConfFile().read_conf(paths, "common", envs)
    return value




if __name__ == '__main__':
    print(get_env())
























