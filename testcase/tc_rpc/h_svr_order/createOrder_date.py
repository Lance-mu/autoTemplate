#!/usr/bin/env python
# coding:utf-8
#!/usr/bin/env python
# coding:utf-8
create_order_normal_data = [
    {
        "title": "创建订单",
        "params": {
            "currency": 2,
            "totalOriginalPrice": 2,
            "totalPayPrice": 2,
            "comments": "自动化-测试A商品",

        },
        "expected": {
            'orderId': 1223,
            'BaseResp': {'StatusMessage': '', 'StatusCode': 0},

        },
    }
]


