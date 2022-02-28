使用Pelican写Blog
#################

:date: 2022-02-28 10:20
:category: python
:tags: pelican


写一篇新文章
-------------

.. code-block:: bash

   $ cat content/文件名.rst

   标题
   ####

   :date: 日期,格式 2010-10-03 10:20
   :category: 分类,逗号分割
   :tags: 标签,逗号分割

   正文


使用 reStructuredText_ 标记语言

.. _reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html


生成静态文件
-------------

.. code-block:: bash

   $ make html
   $ echo "本地查看"
   $ make serve


上传到github
-------------

.. code-block:: bash

   $ pelican content -o output -s pelicanconf.py
   $ ghp-import output
   $ git push git@github.com:lyncir/lyncir.github.io.git gh-pages:pages
