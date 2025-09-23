# 代码生成时间: 2025-09-23 21:27:58
import numpy as np

"""
# TODO: 优化性能
Access Control System using Python and NumPy.
# 优化算法效率
This module provides a simple access control mechanism that can be used to manage
user permissions in a system.

Attributes:
    users_permissions (dict): A dictionary mapping usernames to their permissions.

Methods:
    check_permission(username, permission): Check if a user has a specific permission.
"""
# 添加错误处理

# Define a dictionary to store user permissions
users_permissions = {
    "alice": ["read", "write"],
# NOTE: 重要实现细节
    "bob": ["read"],
    "charlie": ["write"],
}


def check_permission(username, permission):
    """
    Check if a user has a specific permission.
# NOTE: 重要实现细节

    Args:
        username (str): The username to check.
        permission (str): The permission to check for.

    Returns:
# 增强安全性
        bool: True if the user has the permission, False otherwise.
# 优化算法效率
    
    Raises:
        ValueError: If the username is not found in the permissions dictionary.
    """
    if username not in users_permissions:
        raise ValueError(f"User '{username}' not found.")
    return permission in users_permissions[username]

# Example usage
if __name__ == "__main__":
    try:
        # Check if Alice has write permission
        if check_permission("alice", "write"):
            print("Alice has write permission.")
        else:
            print("Alice does not have write permission.")
# NOTE: 重要实现细节

        # Check if Bob has write permission
        if check_permission("bob", "write"):
            print("Bob has write permission.")
        else:
            print("Bob does not have write permission.")
# NOTE: 重要实现细节

        # Try to check a non-existent user's permission
        check_permission("dave", "read")
    except ValueError as e:
        print(e)