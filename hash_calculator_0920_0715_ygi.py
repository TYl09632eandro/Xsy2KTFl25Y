# 代码生成时间: 2025-09-20 07:15:18
import hashlib
import numpy as np

"""
哈希值计算工具

这个工具使用Python和Numpy框架来计算给定输入的哈希值。它支持多种哈希算法，
并且可以处理字符串和Numpy数组类型的输入。

Attributes:
    None

Methods:
    calculate_hash(input_data, algorithm): 计算给定输入的哈希值

Example:
    >>> hash_calculator = HashCalculator()
    >>> result = hash_calculator.calculate_hash("Hello, world!", "sha256")
    >>> print(result)
"""

class HashCalculator:
    def __init__(self):
        """初始化哈希计算器"""
        pass

    def calculate_hash(self, input_data, algorithm="sha256"):
        """
        计算给定输入的哈希值

        Args:
            input_data (str or np.ndarray): 要计算哈希值的输入数据（字符串或Numpy数组）
            algorithm (str): 使用的哈希算法，默认为sha256

        Returns:
            str: 计算得到的哈希值（十六进制字符串）

        Raises:
            ValueError: 如果算法不支持或输入数据类型不正确
        """
        # 支持的哈希算法
        supported_algorithms = [
            "md5",
            "sha1",
            "sha224",
            "sha256",
            "sha384",
            "sha512",
        ]

        # 检查算法是否支持
        if algorithm not in supported_algorithms:
            raise ValueError(f"不支持的哈希算法: {algorithm}")

        # 将输入数据转换为字节串
        if isinstance(input_data, str):
            input_bytes = input_data.encode("utf-8")
        elif isinstance(input_data, np.ndarray):
            # 确保输入数组是字节类型
            if input_data.dtype != np.uint8:
                raise ValueError("输入Numpy数组必须是uint8类型")
            input_bytes = input_data.tobytes()
        else:
            raise ValueError("输入数据类型不正确，必须是字符串或Numpy数组