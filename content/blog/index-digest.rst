数据库schema优化工具
####################

:date: 2022-04-15 11:42
:category: python
:tags: database, index
:slug: index-digest


index-digest_: 分析数据库查询和schema并提供索引改进建议

.. _index-digest: https://github.com/macbre/index-digest


安装
-------------

.. code-block:: bash

   $ pip install indexdigest


数据库查询日志
----------------


示例:

.. code-block:: mysql

   -- A comment
   select * from 0002_not_used_indices order by id
   select * from 0002_not_used_indices where foo = 'foo' and id = 2
   select count(*) from 0002_not_used_indices where foo = 'foo'
   /* foo bar */ select * from 0002_not_used_indices where bar = 'foo'
   INSERT  IGNORE INTO `0070_insert_ignore` VALUES ('123', 9, '2017-01-01');


也可以使用MySQL慢查询日志,但需要进行前置处理

.. code-block:: mysql

   cat mysql-slow.log | egrep -v '^(SET timestamp|#|throttle: )' > queries.log


最后执行 `index_digest --sql-log=queries.log`


常用选项
---------

- `missing_primary_index`: 报告没有主键或唯一索引的表 `MySQL bug #76252`_
- `low_cardinality_index`: 报告使用基数较低的索引
- `queries_not_using_index`: 报告没有使用任何索引
- `queries_using_filesort`: 报告需要`filesort`的查询. `a sort can’t be performed from an index and quicksort is used`_
- `queries_using_temporary`: 报告需要临时表的查询
- `queries_using_full_table_scan`: 报告使用全表查询. `full table scan`_
- `selects_with_like`: 报告使用`LIKE %foo`查询
- `having_clause`: 报告 `queries using HAVING clause`_
- `high_offset_selects`: 报告 `SELECT queries using high OFFSET`_

.. _`MySQL bug #76252`: https://bugs.mysql.com/bug.php?id=76252
.. _`a sort can’t be performed from an index and quicksort is used`: https://www.percona.com/blog/2009/03/05/what-does-using-filesort-mean-in-mysql/
.. _`full table scan`: https://dev.mysql.com/doc/refman/5.7/en/table-scan-avoidance.html
.. _`queries using HAVING clause`: https://github.com/jarulraj/sqlcheck/blob/master/docs/query/3012.md
.. _`SELECT queries using high OFFSET`: https://www.percona.com/blog/2008/09/24/four-ways-to-optimize-paginated-displays/


.. code-block:: bash
   
   $ index_digest mysql://127.0.0.1/database --sql-log=queries.log --checks=missing_primary_index,low_cardinality_index,queries_not_using_index,queries_using_filesort,queries_using_temporary,queries_using_full_table_scan,selects_with_like,having_clause,high_offset_selects
   
