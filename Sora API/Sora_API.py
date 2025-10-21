from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QMessageBox
)
from Ui_Sora_API import Ui_Sora2_API
from Task import Create_Task, Get_Status
from VideoDownload import DownloadThread  # 导入下载线程

class TaskThread(QThread):
    """处理任务创建和状态查询的子线程"""
    result_signal = Signal(str)  # 用于发送结果到主线程

    def __init__(self, prompt, url):
        super().__init__()
        self.prompt = prompt
        self.url = url

    def run(self):
        """子线程执行函数，避免阻塞UI"""
        try:
            # 执行耗时的任务创建
            task_id = Create_Task(self.prompt, self.url)
            if not task_id:
                self.result_signal.emit("任务创建失败，请检查参数")
                return
            
            # 执行耗时的状态查询
            message = Get_Status(task_id)
            self.result_signal.emit(message)
        except Exception as e:
            self.result_signal.emit(f"操作失败: {str(e)}")

class MainWindow(QWidget, Ui_Sora2_API):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bind()
        # 初始化下载线程
        self.setWindowTitle("Sora2 API") 
        self.download_thread = None

    def bind(self):
        self.Submit_Button.clicked.connect(self.submit_task)
        self.Download_Button.clicked.connect(self.start_download)
        self.Download_Button.setEnabled(False)


    def submit_task(self):
        """提交任务（使用子线程避免UI阻塞）"""
        prompt = self.Prompt_Text.toPlainText().strip()
        url = self.Image_Adress.text().strip()

        if not prompt:
            QMessageBox.warning(self, "输入错误", "请输入提示词")
            return

        # 禁用提交按钮防止重复点击
        self.Submit_Button.setEnabled(False)
        self.Download_Button.setEnabled(False)
        self.Out_Put.setText("正在处理任务...")

        # 创建并启动任务线程
        self.task_thread = TaskThread(prompt, url)
        self.task_thread.result_signal.connect(self.update_task_result)
        self.task_thread.finished.connect(lambda: self.Submit_Button.setEnabled(True))  # 线程结束后恢复按钮
        self.task_thread.start()

    def update_task_result(self, message):
        """更新任务结果到UI（主线程中执行）"""
        self.Out_Put.setText(message)
        # 检查任务状态
        if "视频URL: " in message:
            self.Download_Button.setEnabled(True)

    def start_download(self):
        """开始下载视频（使用下载线程）"""
        output_text = self.Out_Put.text().strip()
        
        # 检查任务状态
        if "任务失败" in output_text:
            QMessageBox.warning(self, "下载失败", "任务未成功完成，无法下载")
            return
        
        # 提取视频URL（假设成功信息格式为："任务成功，视频URL: https://xxx.mp4"）
        url_prefix = "视频URL: "
        if url_prefix not in output_text:
            QMessageBox.warning(self, "解析失败", "未找到视频下载地址")
            return
        
        video_url = output_text.split(url_prefix)[-1].strip()

        # 选择保存路径
        save_path, _ = QFileDialog.getSaveFileName(
            self, "保存视频", "", "MP4文件 (*.mp4);;所有文件 (*)"
        )
        if not save_path:
            return  # 用户取消选择

        # 确保下载线程已停止
        if self.download_thread and self.download_thread.isRunning():
            QMessageBox.information(self, "提示", "已有下载任务正在进行")
            return

        # 创建并启动下载线程
        self.download_thread = DownloadThread(video_url, save_path)
        # 连接下载信号
        self.download_thread.progress_signal.connect(self.update_download_progress)
        self.download_thread.finished_signal.connect(self.download_finished)
        self.download_thread.error_signal.connect(self.download_error)
        
        # 禁用下载按钮并显示进度
        self.Download_Button.setEnabled(False)
        self.Out_Put.setText("开始下载视频...")
        self.download_thread.start()

    def update_download_progress(self, progress):
        """更新下载进度（主线程中执行）"""
        self.Out_Put.setText(f"正在下载... {progress}%")

    def download_finished(self):
        """下载完成处理"""
        self.Download_Button.setEnabled(True)
        self.Out_Put.setText("视频下载完成！")
        QMessageBox.information(self, "成功", "视频已保存到指定路径")

    def download_error(self, error_msg):
        """下载错误处理"""
        self.Download_Button.setEnabled(True)
        self.Out_Put.setText(f"下载失败: {error_msg}")
        QMessageBox.warning(self, "下载错误", error_msg)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()