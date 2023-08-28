Linux常用命令
#################

:date: 2022-07-09 15:42
:category: linux
:tags: command
:slug: linux-command


- 查看链路上的最大MTU大小

.. code-block:: bash

   $ size=1272
   while ping -s $size -c1 -M do google.com >&/dev/null; do 
     ((size+=4))
   done
   echo "Max MTU size: $((size-4+28))"


- 模拟常见网络问题



.. code-block:: bash

   # 使用 `iptables` 丢弃传入和传出的数据包
   $ iptables -A INPUT -m statistic --mode random --probability 0.1 -j DROP
   $ iptables -A OUTPUT -m statistic --mode random --probability 0.1 -j DROP

   # 使用 `tc` 支持一些附加选项
   $ tc qdisc add dev eth0 root netem delay 50ms 20ms distribution normal
   $ tc qdisc change dev eth0 root netem reorder 0.02 duplicate 0.05 corrupt 0.01

   # 重置
   $ tc qdisc del dev eth0 root netem
