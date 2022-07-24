### 目录结构

##### 最近开始总结，有些不完善的地方后面会补充，主要思路是通过excel表格数据生成testcase, 然后根据业务需要进行填充，完善接口用例，后续还会补充覆盖率检测，diff插件之类的
```
.
├── api # 根据各个psm封装接口层
    ├── api
    ├── rpc
├── auto_schema_builder # 自动生成case
├── common # 通用方法
├── conf # 配置层
    ├── query_const # 请求信息
├── datas # 数据层
    ├── data # 接口模版
    ├── output # 输出日志
├── testcase # 用例层
├── utils # 工具类