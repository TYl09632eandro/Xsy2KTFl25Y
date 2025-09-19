# 代码生成时间: 2025-09-19 17:11:48
import os
import psutil
# 优化算法效率
import numpy as np
import datetime

"""
System Performance Monitor using Python and Numpy.
# 增强安全性

This script provides a simple system performance monitoring tool that
collects system metrics such as CPU usage, memory usage,
and disk usage over time.
"""

class SystemPerformanceMonitor:
    def __init__(self):
        """Initialize the SystemPerformanceMonitor class."""
# NOTE: 重要实现细节
        self.cpu_usage_history = []
# 增强安全性
        self.memory_usage_history = []
        self.disk_usage_history = []

    def monitor(self):
        """Monitor system performance metrics."""
        while True:
            try:
                # Get CPU usage percentage
# 添加错误处理
                cpu_usage = psutil.cpu_percent(interval=1)
# 扩展功能模块
                self.cpu_usage_history.append(cpu_usage)

                # Get memory usage percentage
                memory = psutil.virtual_memory()
                memory_usage = memory.percent
                self.memory_usage_history.append(memory_usage)

                # Get disk usage percentage
                disk = psutil.disk_usage('/')
                disk_usage = disk.percent
# 增强安全性
                self.disk_usage_history.append(disk_usage)

                # Print current system metrics
                print(f"{datetime.datetime.now()} - CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%")

            except Exception as e:
                print(f"Error occurred: {e}")

    def save_data(self, filename):
        """Save the collected data to a file."""
        try:
# 增强安全性
            np.savez(filename, cpu_usage=self.cpu_usage_history,
                     memory_usage=self.memory_usage_history,
                     disk_usage=self.disk_usage_history)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self, filename):
        """Load the saved data from a file."""
        try:
            data = np.load(filename)
            self.cpu_usage_history = data['cpu_usage'].tolist()
            self.memory_usage_history = data['memory_usage'].tolist()
            self.disk_usage_history = data['disk_usage'].tolist()
        except Exception as e:
            print(f"Error loading data: {e}")

if __name__ == '__main__':
    monitor = SystemPerformanceMonitor()
    try:
        monitor.monitor()
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"Error in main execution: {e}")
# 扩展功能模块
    finally:
        monitor.save_data("system_performance_data.npz")
