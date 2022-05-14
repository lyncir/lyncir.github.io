python枚举
##########

:date: 2022-04-02 14:01:24
:category: python
:tags: python, enum
:slug: python-enum


python在3.4版本新加了对枚举的支持,那在此之前都是怎么来做枚举的呢?


1. 直接使用定义变量的方法

.. code-block:: python

   RED = 1
   GREEN = 2
   BLUE = 3

   assert RED == 1


2. 使用字典

.. code-block:: python

   color = {"RED": 1, "GREEN": 2, "BLUE": 3}
   
   assert color["RED"] == 1


3. 使用类变量

.. code-block:: python

   class Color:

      RED = 1
      GREEN = 2
      BLUE = 3

   assert Color.RED == 1


缺点:

1. 会出现同key不同值情况
2. 值可以被修改
3. 不能反向查询,例如: 1对应的就是RED


使用枚举示例:


.. code-block:: python

   from enum import IntEnum 

   class Color(IntEnum):

      RED = 1
      GREEN = 2
      BLUE = 3

   assert Color(1).name == "RED"
