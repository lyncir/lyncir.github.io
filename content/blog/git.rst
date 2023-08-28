Git常用命令
#################

:date: 2023-08-28 09:43
:category: git 
:tags: git
:slug: git


Git Config
------------

.. code-block:: bash

   # 显示更美观
   ll = log --graph --pretty=format:'%C(yellow)%h%Creset -%C(cyan)%d%Creset %s %Cgreen(%an, %cr)' --abbrev-commit


   # 显示unicode文件名
   $ git config --global core.quotePath false


Git Use
------------


.. code-block:: bash

    1. 查看commit log中的修改
    $ git ll -p

    2. git生产patch和使用patch
    $ git diff > /tmp/patch.txt
    $ git apply /tmp/patch.txt

    3. 查看消失的log并撤销rebase
    # undo git rebase
    $ git reflog
    $ git reset --hard HEAD@{5}

    4. 撤销未提交的更改
    # show what will be deleted
    $ git clean -n

    # To remove directories
    $ git clean -f -d

    # To remove ignored files
    $ git clean -f -X

    # To remove ignored and non-ignored files
    $ git clean -f -x

    5. 对上一次的提交做修改
    $ git commit --amend -am "test"

    6. 查看已提交的diff
    $ git diff COMMIT^!

    7. 撤销merge
    $ git checkout <merge所在的分支>
    $ git reset --hard HEAD~1

    8. 撤销某次提交
    $ git revert --strategy resolve <commit>

    9. 批量删除本地分支
    $ git branch | grep -v "feature/xxx" | grep -v "yyy" | xargs git branch -d

    10. 撤销comit
    $ git reset --soft HEAD^

    11. 撤销add
    $ git reset HEAD .


项目开发流程
------------

.. code-block:: bash

    # 获取主干最新代码
    $ git clone <repo>
    $ git checkout develop # 开发分支
    $ git pull # 同步分支

    # 新建一个开发分支my_feature
    $ git checkout -b feature/my_feature

    # 确认已切换到当前分支
    $ git branch

    # 保存所有的修改变化
    $ git add --all
    # 查看发生变动的文件
    $ git status
     
    # 编辑备注
    $ git commit -m "implement api architecture"
    # 将分支代码push到服务器
    $ git push origin -u feature/my_feature

    # 分支开发过程中，为了减少冲突，尽量要多与主干同步
    $ git fetch origin
    $ git rebase origin/develop
    $ git add .  # 解决冲突后add
    $ git rebase --continue

    #删除分支
    $ git branch -d feature/my_feature

    #取消commit
    $ git reset --hard <commit log>

git 存储验证
------------

.. code-block:: bash

    $ git config --global credential.helper wincred
