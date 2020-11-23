* python3 环境

~~~~~
Python 3.8.5
pip3 20.2.4
~~~~~

* 安装 Scrapy 可能提示 [Twisted](https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/Twisted-20.3.0-cp38-cp38-win_amd64.whl) 安装异常需要手动下载安装。安装时注意自己python版本

> [下载地址](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted)
* Python 3.8 下载的
> https://download.lfd.uci.edu/pythonlibs/z4tqcw5k/Twisted-20.3.0-cp38-cp38-win_amd64.whl

* 1、安装Twisted依赖
~~~~~
pip3 install Twisted-20.3.0-cp38-cp38-win_amd64.whl
~~~~~
* 2、安装Scrapy
~~~~~
pip3 install Scrapy
~~~~~

* 运行

~~~~
# scrapy crawl scrapy
python main.py
~~~~~

* 添加 mongo:4.2.7 [tag v0.0.1](https://github.com/yanxianhe/scrapy/tree/v0.0.1)

~~~~~
mongo_host = '127.0.0.1'          # 本地安装 mongo:4.2.7 安装过程略过
mongo_port = 27017                # 默认端口号
mongo_db_user = 'mongoadmin'      # 使用mongo 用户名
mongo_db_pwd = 'mongoadmin'       # 使用mongo 密码
mongo_db_name = 'test'            # 创建test库
mongo_db_collection = 'test_info' # test库下创建test_info 表
~~~~~

* 添加 mysql:5.7.26

~~~~~
mysql_host = '127.0.0.1'            # 本地安装 mysql:5.7.26 安装过程略过
mysql_port = 4306                   # 默认端口号
mysql_db_user = 'root'              # 使用root 用户名
mysql_db_pwd = 'root'               # 使用root 密码
mysql_db_name = 'test'              # 创建test库
mysql_db_collection = 'test_info'   # test库下创建test_info 表
~~~~~ 

* cmdline.py 文件根据自己python 安装路径查找
* 比较特殊需要将本地安装python目录下 ~\Python38\Lib\test\libregrtest\cmdline.py 拷贝到 testscrapy 下
* sql 脚本在 /sql/目录下
