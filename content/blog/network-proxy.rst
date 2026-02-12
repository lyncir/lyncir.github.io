常见网络代理
############

:date: 2022-03-02 11:22
:category: linux
:tags: network, proxy
:slug: network-proxy

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

   $ echo "设置http代理"
   $ wget -e use_proxy=yes -e https_proxy=127.0.0.1:1080 [URL]


curl
----

.. code-block:: bash

   $ echo "设置http代理"
   $ export http_proxy=http://127.0.0.1:1080
   $ export https_proxy=https://127.0.0.1:1080


pip
----

.. code-block:: bash

   $ echo "设置http代理"
   $ pip install --proxy http://127.0.0.1:1080 -r requirements.txt


docker
------

.. code-block:: bash

   $ echo "设置http代理"
   $ HTTP_PROXY=http://127.0.0.1:1080 docker pull busybox


apt
------

.. code-block:: bash

   $ echo "设置http代理"
   $ cat /etc/apt/apt.conf.d/proxy.conf
   Acquire::http::Proxy "http://127.0.0.1:1080";
   Acquire::https::Proxy "http://127.0.0.1:1080";


tsocks_
-------

socks的代理库，可以把sock转为http


.. code-block:: bash

   $ tsocks git pull
   $ tsocks apt update


.. _tsocks: https://github.com/zouguangxian/tsocks
