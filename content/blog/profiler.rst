python性能分析工具
###################

:date: 2022-03-08 11:40
:category: python
:tags: profiler
:slug: profiler


py-spy_
-------

比较好用的功能是使用 ``record`` 命令生成火焰图


.. code-block:: bash

   $ py-spy record -o profile.svg -- python run.py


.. image:: images/violy-profile.svg


或者生成 speedscope_ 格式进行分析



.. code-block:: bash

   $ py-spy record --format speedscope -o profile.speedscope.json -- python run.py


cProfile
---------


.. code-block:: bash

   $ cat test.py
   import cProfile
   pr = cProfile.Profile()
   pr.enable()

   code...

   pr.disable()
   pr.dump_stats("pipeline.prof")

   $ flameprof pipeline.prof > pipeline.svg
   or
   $ snakeviz pipeline.prof



line_profiler_
--------------


.. code-block:: bash

   $ cat test.py
   from line_profiler import LineProfiler
   lp = LineProfiler()

   lp_wrapper = lp(func)
   lp_wrapper(**kwargs)
   print(lp.print_stats())


.. _speedscope: https://www.speedscope.app/
.. _py-spy: https://github.com/benfred/py-spy
.. _line_profiler: https://github.com/pyutils/line_profiler
