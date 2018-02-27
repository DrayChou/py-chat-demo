import sys

# 设置窗口图标
from kivy.config import Config
Config.set('kivy', 'window_icon', 'data/favicon.ico')

if sys.version_info > (3, 5):  # determine if it's py3 or py2
    from asyncio_main import ChatApp
else:
    from asyncore_main import ChatApp

ChatApp().run()
