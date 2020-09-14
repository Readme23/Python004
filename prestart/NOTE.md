如何系统的学习 Python：
  - 相关链接：
    - 《提问的智慧》： https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md
    - Python 3.7.7 官方文档： https://docs.python.org/zh-cn/3.7/
    - GitHub 搜索帮助： https://help.github.com/cn/github/searching-for-information-on-github
    - 编码规范：
      - PEP8： https://www.python.org/dev/peps/pep-0008/
      - Google Python Style Guides： http://google.github.io/styleguide/pyguide.html

H1常用 pip 源地址:
  - 豆瓣： https://pypi.doubanio.com/simple/
  - 清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
  - 中科大： https://pypi.mirrors.ustc.edu.cn/simple/
  - 阿里云： https://mirrors.aliyun.com/pypi/simple/
   
  - 修改方式:
    - 临时替换：
      - pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
    - 永久替换（先升级 pip：pip install pip -U ）：
      - pip config set global.index-url
        https://pypi.tuna.tsinghua.edu.cn/simple
    
虚拟环境：
  - python3 -m venv venvname (注：venv 是 Python 的一个模块)
  - 进入某个虚拟环境：source venvname/bin/activate 