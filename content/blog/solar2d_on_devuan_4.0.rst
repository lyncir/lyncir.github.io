安装Solar2D
####################

:date: 2022-08-23 15:27
:category: linux
:tags: solar2d
:slug: solar2d_on_devuan_4.0


要求
-----

* Devuan 4.0系统
* PlayOnLinux
* Solar2D-Windows-2022.3677.msi
* Wine(x86) 7.11


安装PlayOnLinux
----------------


.. code-block:: bash

   $ sudo apt install playonlinux


安装wine
----------------


.. code-block:: bash

   $ sudo apt install wine32


安装Solar2D
--------------

* 打开PlayOnLinux, **Tools** ->  **Manage Wine Versions**
* 选择安装最新的Wine(x86), 当前是 **7.11**
* 主界面 -> **Install** -> **Install a non-listed program** [底部] -> Next
* **Install a program in a new virtual drive** -> Next
* 输入名字: **Solar2D** -> Next
* 选择: **Install some libraries** -> Next
* **32 bits windows installation** -> Next
* 选择这些库安装: **POL-install-corefonts**, **POL-install-vcrun2013** 和 **POL-install-wmp10** -> Next
* 点击 **Browse**, 选择 **MSI** 文件 -> Next
* 和在Windows一样进行安装. 不要修改路径. 安装完后不启动! -> Finish
* 从列表中选择: **Corona Simulator.exe** -> Next
* Next
* 选择 **I don't want to make another shortcut** -> Next
* 完成
