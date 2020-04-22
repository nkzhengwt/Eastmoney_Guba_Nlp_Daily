# Eastmoney_Guba_Nlp_Daily
A web crawler and nlp to analyze the public sentiments of A shares
# 安装与配置：
- 双击运行.\configure.bat（若之前安装过，则需先运行configure_uninstall.bat）
- 修改程序运行状态通知邮箱（以文本文档打开.\guba_daily.py，修改第42行邮箱）
- 设置代理IP账号（以文本文档打开.\guba_daily.py，第9行，proxyUser为用户名，proxyPass为密码）
- 设置进程个数（根据代理ip并发上限来定，第11行，默认为10次并发）
# 每日更新：
- 每天运行前需更新文件：
.\guba\info\Code.txt;
.\guba\info\Calendar_SSE.txt
- 每日运行：
.\daily.bat
# 路径文件说明：
- .\guba\backup 为历史备份数据及文件，定期可清理一次
- .\guba\history 为历史原始文本及数据（有_txt后缀为原始文本，无后缀为自然语言处理模型后的数据）
- .\guba\info\datelog.txt 为更新时间记录
- .\guba\log 为运行日志
