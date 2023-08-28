Godot 笔记
####################

:date: 2022-07-19 17:09
:category: game-dev 
:tags: godot
:slug: godot-study


代码基于Godot 4.0


GdScript脚本
------------

类似Python


示例:

.. code-block:: python

   # 一个文件就是一个类

   # 继承

   extends BaseClass

   # (可选) 可自定义图标的类定义

   class_name MyClass, "res://path/to/optional/icon.svg"


   # 成员变量

   var a = 5
   var s = "Hello"
   var arr = [1, 2, 3]
   var dict = {"key": "value", 2: 3}
   var typed_var: int
   var inferred_type := "String"

   # 常数

   const ANSWER = 42
   const THE_NAME = "Charly"

   # 枚举

   enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
   enum Named {THING_1, THING_2, ANOTHER_THING = -1}

   # 内建向量类型

   var v2 = Vector2(1, 2)
   var v3 = Vector3(1, 2, 3)


   # 函数

   func some_function(param1, param2):
       var local_var = 5

       if param1 < local_var:
           print(param1)
       elif param2 > 5:
           print(param2)
       else:
           print("Fail!")

       for i in range(20):
           print(i)

       while param2 != 0:
           param2 -= 1

       var local_var2 = param1 + 3
       return local_var2


   # 重写父级函数,如果要调用父级函数,可以使用'.', 就像python的super

   func something(p1, p2):
       .something(p1, p2)


   # 内类

   class Something:
       var a = 10


   # 构造函数

   func _init():
       print("Constructed!")
       var lv = Something.new()
       print(lv.a)


关键字(只列出部分):

=============    ==============================================================
关键字           描述
=============    ==============================================================
match             用于分支程序的执行 
class_name        为脚本定义类名称和可选图标 
extends           定义用当前类扩展什么类
as                如果可能, 将值转换为给定类型
self              引用当前类实例
tool              在编辑器中执行脚本
signal            定义信号
onready           一旦脚本附加到的节点及其子级成为场景树的一部分, 就初始化变量
export            保存一个变量及其附加的资源, 并使其在编辑器中可见和可修改
setget            为变量定义setter和getter函数
preload           预加载一个类或变量
INF               无穷大常数. 用于比较
NAN               NAN(不是一个数字)常数. 用于比较
=============    ==============================================================


字面量(只列出部分):


===============    =====================================
字面量               类型
===============    =====================================
`@"Node/Label"`      `NodePath` 或 StringName
`$NodePath`          `get_node("NodePath")` 的简写
===============    =====================================


API
------

API相关


性能监控
===========

.. code-block:: python
   
   # 比如FPS
   Performance.get_monitor(Performance.TIME_FPS)


UDP网络监控
===========

.. code-block:: python
   
   # 比如RTT
   # 先初始话Enet
   enet = ENetMultiplayerPeer.new()
   # 再根据id获取ENetPacketPeer
   peer = enet.get_peer(id)
   peer.get_statistic(ENetPacketPeer.PEER_ROUND_TRIP_TIME)

