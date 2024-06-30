#-*- coding: utf-8 -*-
import sys
import webview, os
if getattr(sys, 'frozen', False):
    cwd = os.path.dirname(sys.executable)
else:
    file_path = os.path.abspath(__file__)
    cwd = os.path.dirname(file_path)
print(cwd)
import webview
text = """{
    "window": {
        "width": 480,
        "height": 360
    },
    "size": {
        "resizable": True,
        "fullscreen": False,
        "min_size": (240, 180)
    },
    "frameless": {
        "easy_drag": True
    },
    "state": {
        "minimized": False,
        "on_top": True,
    },
    "web": {
        "text_select": False,
    }
}
"""
exec("config=" + text)

# cwd = os.path.join(os.getcwd(), "file")
window = webview.create_window(
        title = 'Scratch Game',
        url=os.path.join(cwd, 'file/index.html'),
        width=config['window']['width'],
        height=config['window']['height'],
        resizable=config['size']['resizable'],
        text_select=config['web']['text_select'],
        easy_drag=config['frameless']['easy_drag'],
        on_top=config['state']['on_top'],
        fullscreen=config['size']['fullscreen'],
        min_size=config['size']['min_size']
)

def run_webview():
    webview.start(http_server=True)

def run_scratch(path):
    try: os.remove(os.path.join(cwd, "project.zip"))
    except: pass
    p = os.path.abspath(path)
    print(p)
    f = open(p, 'rb')
    file = f.read()
    #f.close()
    f1 = open(os.path.join(cwd, "file\project.zip"), 'wb')
    f1.write(file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_scratch(str(sys.argv[1]))
        run_webview()
    else:
        run_scratch("1.sb3")
        run_webview()