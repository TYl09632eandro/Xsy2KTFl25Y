# 代码生成时间: 2025-10-03 17:52:58
import numpy as np

"""
用户权限管理系统
"""

class UserPermissionManager:
# 优化算法效率
    """
    用户权限管理类，提供权限验证和用户角色管理功能。
    """
    
    def __init__(self):
# 改进用户体验
        # 初始化用户权限数据结构
        self.permissions = {}

    def add_user(self, username, roles):
        """
        添加用户和对应的角色
        :param username: 用户名
        :param roles: 角色列表
        """
        if username in self.permissions:
            raise ValueError(f"用户 {username} 已经存在。")
        self.permissions[username] = roles

    def remove_user(self, username):
        """
        移除指定用户
        :param username: 用户名
        """
        if username not in self.permissions:
            raise ValueError(f"用户 {username} 不存在。")
        del self.permissions[username]

    def assign_role(self, username, role):
        """
        为用户分配角色
        :param username: 用户名
        :param role: 角色名
# NOTE: 重要实现细节
        """
        if username not in self.permissions:
            raise ValueError(f"用户 {username} 不存在。")
        if role not in self.permissions[username]:
            self.permissions[username].append(role)

    def remove_role(self, username, role):
        """
        从用户中移除角色
        :param username: 用户名
        :param role: 角色名
        """
        if username not in self.permissions:
            raise ValueError(f"用户 {username} 不存在。")
        if role in self.permissions[username]:
            self.permissions[username].remove(role)
# 扩展功能模块
        else:
            raise ValueError(f"用户 {username} 没有角色 {role}。")

    def check_permission(self, username, role):
        """
# 优化算法效率
        检查用户是否有指定角色
        :param username: 用户名
        :param role: 角色名
        :return: bool
        """
        if username not in self.permissions:
            return False
        return role in self.permissions[username]

    def get_permissions(self, username):
        """
        获取用户的所有角色
        :param username: 用户名
# TODO: 优化性能
        :return: 角色列表
        """
        if username not in self.permissions:
            raise ValueError(f"用户 {username} 不存在。")
# NOTE: 重要实现细节
        return self.permissions[username]


def main():
# FIXME: 处理边界情况
    # 创建用户权限管理实例
    manager = UserPermissionManager()
    
    try:
        # 添加用户
# TODO: 优化性能
        manager.add_user("alice", ["admin", "user"])
# 增强安全性
        manager.add_user("bob", ["user"])
        
        # 分配角色
# 优化算法效率
        manager.assign_role("alice", "editor")
# 增强安全性
        
        # 移除角色
        manager.remove_role("alice", "user")
        
        # 检查权限
        print(manager.check_permission("alice", "admin"))  # True
        print(manager.check_permission("bob", "admin"))   # False
        
        # 获取用户角色
        print(manager.get_permissions("alice"))  # ["admin", "editor"]
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
# 优化算法效率