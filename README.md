### 目录结构

##### 最近开始总结，有些不完善的地方后面会补充，主要思路是通过excel表格数据生成testcase, 然后根据业务需要进行填充，完善接口用例，后续还会补充覆盖率检测，diff插件之类的
```
.
├── api # 根据各个psm封装接口层
    ├── http
    ├── rpc
├── auto_schema_builder # 自动生成case
    ├── generate_http http接口生成
    ├── generate_rpc rpc接口生成
    ├── run 
├── common # 通用方法
    ├── web_flask 测试平台登录界面
        ├── app web平台登录主入口
    ├── date_util.py 封装，可以调用的日期
    ├── log 日志文件
    ├── sql 数据库相关信息
    ├── utilt 底层包
├── conf # 配置层
    ├── query_const # 请求信息
├── datas # 数据层
    ├── data # 接口模版
    ├── output # 输出日志
├── testcase # 用例层
├── utils # 工具类
    ├── http_utils 封装的HTTP请求
    ├── sql 封装SQL脚本