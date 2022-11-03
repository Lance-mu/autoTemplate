# _*_ coding:utf-8 _*-
# @Time：2022/9/21 22:14
# 作者：qianwulin
from configparser import ConfigParser
from conf.const import CONF_PATH, join


class Utils(object):
    # 设置一个类属性来判断这个类是否实例化过对象
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.config = ConfigParser()

    def get_conf(self, paths, section, keys):
        self.config.read(paths)
        try:
            # config[section][key]
            return self.config.get(section, keys)
        except KeyError:
            raise KeyError(f"conf.ini, section:{section},key:{keys} not found, please check!")

    def set_conf(self, ):
        # # 将数据写入到ini文件中
        # config.add_section('login')  # 首先添加一个新的section
        # config.set('login', 'username', 'admin')  # 写入数据
        # config.set('login', 'password', '123456')  # 写入数据
        # config.write(open(path, 'a'))  # 保存数据
        pass
        # 读取ini文件中所有的section
        # section = config.sections()
        # print(section)

    def get_env(self) -> str:
        """
        框架中底层所使用的方法，业务可以使用，用于获取当前的env环境，使用方法:Utils().get_env()
        :return:
        """
        file = join(CONF_PATH, "conf.ini")
        value = self.get_conf(file, "common", "env")
        return value

    def get_env_lable(self) -> str:
        """
        框架中底层所使用的方法，业务可以使用，用于获取当前的env_label标签，使用方法:Utils().get_env_label()
        :return:
        """
        file = join(CONF_PATH, "conf.ini")
        print(file)
        value = self.get_conf(file, "common", "env_label")
        return value


if __name__ == '__main__':
    print(Utils().get_env_lable())
