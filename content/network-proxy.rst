常见网络代理
############

:date: 2022-03-02 11:22
:category: linux
:tags: network, proxy

git
----

.. code-block:: bash
   
   $ echo "设置http代理"
   $ git config --global http.proxy http://127.0.0.1:1080
   $ git config --global https.proxy https://127.0.0.1:1080

   $ echo "设置socks5代理"
   $ git config --global http.proxy socks5://127.0.0.1:1080
   $ git config --global https.proxy socks5://127.0.0.1:1080

   $ echo "取消代理"
   $ git config --global --unset http.proxy
   $ git config --global --unset https.proxy


wget
----

.. code-block:: bash

   $ wget -e use_proxy=yes -e https_proxy=127.0.0.1:1080 [URL]


pip
----

.. code-block:: bash

   $ pip install --proxy http://127.0.0.1:1080 -r requirements.txt
