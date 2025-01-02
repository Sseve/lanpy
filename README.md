### lanpy

* **描述**
1. 基础知识: [官网](https://python.org/)
2. [Python 发行版的压缩包](https://github.com/astral-sh/python-build-standalone/releases/download/20231002/cpython-3.10.13+20231002-x86_64_v2-unknown-linux-gnu-pgo+lto-full.tar.zst)
3. 项目代码组织结构
4. 项目打包和部署方式

* **打包**
1. 依赖: python -m pip install --upgrade build setuptools wheel
2. 构建: python -m build

* **部署**
1. 拷贝dist目录下的打包文件到目标机器上
2. 安装打包文件: python -m pip install lanpy-0.0.1-py3-none-any.whl -t lanpy
3. 设置 PYTHONPATH 环境变量: export PYTHONPATH=lanpy
4. 运行项目: python -m lanpy
5. 注意: 可以将上面第3步和第4步放在shell脚本中进行项目管理(例如: manage.sh脚本)