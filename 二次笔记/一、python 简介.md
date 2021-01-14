## 一、如何系统的学习 Python：
  - 相关链接：
    - 《提问的智慧》： https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md
    - Python 3.7.7 官方文档： https://docs.python.org/zh-cn/3.7/
    - GitHub 搜索帮助： https://help.github.com/cn/github/searching-for-information-on-github
    - 编码规范：
      - PEP8： https://www.python.org/dev/peps/pep-0008/
      - Google Python Style Guides： http://google.github.io/styleguide/pyguide.html

## 二、常用 pip 源地址:
  - 豆瓣： https://pypi.doubanio.com/simple/
  - 清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
  - 中科大： https://pypi.mirrors.ustc.edu.cn/simple/
  - 阿里云： https://mirrors.aliyun.com/pypi/simple/
   
  - 修改方式:
    - 临时替换：
      - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package -U
      - -U 表示升级某个包
    - 永久替换（先升级 pip：pip install pip -U ）：
      - pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
      - 修改配置文件：
        - Linux：~/.pip/pip.conf
        - 配置文件格式：
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
## 三、vscode 必备插件：
  - Rainbow Fart
  
## 四、虚拟环境：
  - python3 -m venv venvname (注：venv 是 Python 的一个模块)
  - 进入某个虚拟环境：source venvname/bin/activate
  - 虚拟环境中第三方包位置：/Users/apple/venv1/lib/python3.7/site-packages
  - 查看依赖包，进入虚拟环境：pip3 freeze ； pip3 freeze > requirements.txt

## 五、python 基本数据类型：
|  基本数据类型 | |
|  ----  | ----  |
| None | 空对象 |
| Boll | 布尔值 |
| 数值 | 整数、浮点数、复数 |
| 序列 | 字符串、列表、元组 |
| 结合 | 字典 |
| 可调用 | 函数 |

## 六、python 高级数据类型
|  高级数据类型 | |
|  ----  | ----  |
| collections | 容器数据类型 |
| nametuple() | 命名元组 |
| deque | 双端队列 |
| Counter | 计数器 |
| OrderedDict | 有序字典 |
1. 官网链接：[文档地址](https://docs.python.org/zh-cn/3.7/library/collections.html)