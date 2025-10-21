from PySide6.QtCore import QThread, Signal
import requests
from requests.exceptions import RequestException

class DownloadThread(QThread):
    """视频下载线程，处理耗时的文件下载操作"""
    progress_signal = Signal(int)  # 发送下载进度（0-100）
    finished_signal = Signal()     # 下载完成信号
    error_signal = Signal(str)     # 错误信息信号

    def __init__(self, video_url, save_path):
        super().__init__()
        self.video_url = video_url
        self.save_path = save_path
        self.session = requests.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def run(self):
        """线程执行函数：下载视频文件"""
        try:
            # 获取文件大小
            response = self.session.head(self.video_url, allow_redirects=True)
            file_size = int(response.headers.get('Content-Length', 0))
            
            if file_size == 0:
                self.error_signal.emit("无法获取文件大小")
                return

            # 开始下载
            with self.session.get(self.video_url, stream=True, allow_redirects=True) as r:
                r.raise_for_status()  # 检查HTTP错误
                downloaded_size = 0
                
                with open(self.save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:  # 过滤空块
                            f.write(chunk)
                            downloaded_size += len(chunk)
                            # 计算并发送进度
                            progress = int((downloaded_size / file_size) * 100)
                            self.progress_signal.emit(progress)

            self.finished_signal.emit()

        except RequestException as e:
            self.error_signal.emit(f"网络错误: {str(e)}")
        except Exception as e:
            self.error_signal.emit(f"未知错误: {str(e)}")
        finally:
            self.session.close()