内存数据库
####################

:date: 2026-02-12 14:23
:category: game-dev 
:tags: database
:slug: memory-database


背景
------------

最近在考虑如何使用python实现一个内存数据库来写有状态游戏服务器。
主要的流程是这样子的::

                    +-------------------------------+
                    |           世界服务            |
                    |                               |
    +-------+       |   +---------+                 |
    | 队列  | --->  |   | 业务处理|                 |
    +-------|       |   +---------+                 |
                    |   +---------+                 |
                    |   | 业务处理|                 |
                    |   +---------+                 |
                    +-------------------------------+

实现
------------

1. Python3.14t(自由线程)
2. PyO3绑定Rust的scc(Scalable Concurrent Containers)

示例:

.. code-block:: python


    from pyscc import Database, Document

    # 创建数据库
    db = Database()

    # 获取集合(如果不存在则创建集合)
    col = db.get_collection("User")

    # 为集合创建索引
    col.create_index("age")
    col.create_index("name")

    # 定义文档
    doc = Document(1, name="a", age=18)
    # 插入文档
    col.insert(doc)

    doc = Document(2, name="b", age=20)
    col.insert(doc)

    # 单列查询("查询名字为a")
    records = col.find("name", "a")
    for record in records:
        print(record.to_dict())

    # 范围查询("查询年龄19到20")
    records = col.find_range("age", 19, 20)
    for r in records:
        print(r.to_dict())

    # 复杂查询("查询18到20且名字为b")
    filters = [
        {"field": "age", "op": "range", "min": 18, "max": 20},
        {"field": "name", "op": "eq", "value": "b"}
    ]
    records = col.find_complex(filters, op="and")
    for r in records:
        print(r.to_dict())
