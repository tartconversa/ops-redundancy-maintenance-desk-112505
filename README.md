# 共享故障域内的维护准入与停机接力

机柜服务维护演练。时钟单位为分钟。设备 capacity 为可接纳的吞吐单位，故障域是可能共同失效的电力单元，站点只用于限制可服务区域。

## 在本地查看资料

运行环境使用 Python 3.11.2 和标准库。启动资料浏览器无需安装额外包。

```sh
python materials.py
python materials.py cells
python -m unittest discover -s tests -v
```

资料浏览器也接受下方的其他资料名。JSONL 使用 UTF-8 编码，每行是一个对象。表内的顺序对应来源记录，事件时间与接收时间的区别以资料说明为准。各入口可以在无外网的环境中运行。

资料字段和业务口径见[演练资料格式](materials/README.md)。
