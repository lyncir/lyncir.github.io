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
