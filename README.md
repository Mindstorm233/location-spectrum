# 基于PlutoSDR与flask框架的位置-频谱记录系统

## 功能说明

本系统支持向后端回传经纬度后，利用ADALM-Pluto采集频谱数据，存储到/data目录内。同时，系统还支持发送、可视化信号的功能，详见/PySDR-Related。

## 上次更新时间

2024年5月7日

## 作者

+ Mindstorm from BUPT-International School, Majoring in Telecommunication Engineering with Management.
+ Jenny from BUPT-International School, Majoring in Telecommunication Engineering with Management.

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

## 使用方法

1. 配置完成后，运行app.py文件，在浏览器打开<http://127.0.0.1:5000/>，显示网页。
2. 输入所需信息后（经纬度精度受限于设备，请利用手机等设备进一步完善），程序将记录该经纬度点的频谱数据，重复10次。
3. 您可以在不同时间、不同地点反复运行，以获得频谱地图。
