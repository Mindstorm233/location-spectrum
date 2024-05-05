# 基于PlutoSDR与flask框架的位置-频谱记录系统

## 功能说明

本系统支持向后端回传经纬度后，利用ADALM-Pluto采集频谱数据，存储到/data目录内。同时，系统还支持发送信号的功能，详见/PySDR-Related。

## 作者

+ Mindstorm from BUPT, 2024.05.
+ Jenny from BUPT, 2024.05.

## 配置方法(目前只支持Windows系统)

1. USB连接ADALM-Pluto设备。
2. 安装位于/PySDR-Related路径下的三个.exe文件：首先安装PlutoSDR-M2k-USB-Drivers.exe，然后安装libiio-0.25.gb6028fd-setup.exe和libad9361-setup.exe。
3. (此处仅说明Conda安装方法，其余方法近似)运行以下命令：

   ```bash
    conda create --name plutoSDR python=3.10
    conda activate plutoSDR
    conda install flask flask_cors numpy matplotlib jupyter scipy
    pip install pyadi-iio
   ```

4. 运行pySDR.ipynb的第一条代码，如果返回一个复数行向量，则配置成功。
