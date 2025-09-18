# 代码生成时间: 2025-09-19 04:25:11
import numpy as np
import threading
import time
from datetime import datetime, timedelta
from typing import Callable, Dict, List

"""
一个定时任务调度器，使用numpy和threading框架实现。
支持添加多个定时任务，并定期执行。
"""

class ScheduledTaskScheduler:
    def __init__(self, interval: int = 10):
        """
        初始化定时任务调度器
        :param interval: 任务执行间隔（秒）
        """
        self.interval = interval
        self.tasks: List[Dict] = []  # 存储任务
        self.scheduler_thread: threading.Thread = None  # 调度线程
        self.running = False  # 是否正在运行

    def add_task(self, name: str, task_func: Callable, delay: int = 0):
        """
        添加定时任务
        :param name: 任务名称
        :param task_func: 任务函数
        :param delay: 任务延迟执行时间（秒）
        """
        task = {'name': name, 'task_func': task_func, 'next_run_time': datetime.now() + timedelta(seconds=delay)}
        self.tasks.append(task)
        print(f"任务{name}添加成功，将在{delay}秒后执行。")

    def start(self):
        """
        启动调度器
        """
        if not self.running:
            self.running = True
            self.scheduler_thread = threading.Thread(target=self._run)
            self.scheduler_thread.start()
            print("调度器启动成功。")
        else:
            print("调度器已在运行中。")

    def stop(self):
        """
        停止调度器
        """
        if self.running:
            self.running = False
            self.scheduler_thread.join()
            print("调度器停止成功。")
        else:
            print("调度器未在运行中。")

    def _run(self):
        """
        调度器主循环
        """
        while self.running:
            current_time = datetime.now()
            for task in self.tasks:
                if current_time >= task['next_run_time']:
                    try:
                        task['next_run_time'] = current_time + timedelta(seconds=self.interval)
                        task['task_func']()
                        print(f"任务{task['name']}执行成功。")
                    except Exception as e:
                        print(f"任务{task['name']}执行失败：{str(e)}")
            time.sleep(self.interval)

# 示例用法
def task_func1():
    print("任务1执行。")

def task_func2():
    print("任务2执行。")

scheduler = ScheduledTaskScheduler(interval=5)
scheduler.add_task("任务1", task_func1)
scheduler.add_task("任务2", task_func2, delay=3)
scheduler.start()

# 模拟运行10秒后停止调度器
time.sleep(10)
scheduler.stop()