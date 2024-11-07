SQL排序确定性
#################

:date: 2024-11-07 17:02
:category: db
:tags: mysql
:slug: sql-sort-order


容易遗忘的规则
--------------------

关于SQL数据库，无序查询可以按任何顺序返回结果，即`非确定性排序顺序`。每次执行查询时，顺序都无法保证。


.. code-block:: bash

    mysql> SELECT * FROM ratings ORDER BY category;
    +----+----------+--------+
    | id | category | rating |
    +----+----------+--------+
    |  1 |        1 |    4.5 |
    |  5 |        1 |    3.2 |
    |  3 |        2 |    3.7 |
    |  4 |        2 |    3.5 |
    |  6 |        2 |    3.5 |
    |  2 |        3 |    5.0 |
    |  7 |        3 |    2.7 |
    +----+----------+--------+


以上查询按category列排序，但对于id和rating列是不确定的。

如果多次运行此查询，理论上每次都会得到不同顺序的结果。实际上，可能会得到看起来像隐式排序的结果，并且每次运行查询时都会得到一致的结果。


总结
-------

在不同的MySQL版本中，由于隐式排序逻辑的不一致，导致返回的结果顺序有可能不一致。但同一版本中是一致的(不要依赖它)。

因此，如果返回顺序结果很重要，请使用`确定性排序顺序`查询。


.. code-block:: bash

    mysql> SELECT * FROM ratings ORDER BY category, id;
    +----+----------+--------+
    | id | category | rating |
    +----+----------+--------+
    |  1 |        1 |    4.5 |
    |  5 |        1 |    3.2 |
    |  3 |        2 |    3.7 |
    |  4 |        2 |    3.5 |
    |  6 |        2 |    3.5 |
    |  2 |        3 |    5.0 |
    |  7 |        3 |    2.7 |
    +----+----------+--------+


Ref: `LIMIT Query Optimization`_


.. _`LIMIT Query Optimization`: https://dev.mysql.com/doc/refman/8.0/en/limit-optimization.html
