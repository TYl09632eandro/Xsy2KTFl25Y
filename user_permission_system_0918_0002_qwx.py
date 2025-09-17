# 代码生成时间: 2025-09-18 00:02:08
import numpy as np

"""
A user permission management system that handles user permissions and roles.
"""

class UserPermissionSystem:
    """
    This class manages user permissions and roles.
    It provides functionality to add, update, and delete permissions.
    """

    def __init__(self):
        # Initialize a dictionary to store user permissions
        self.permissions = {}

    def add_user_permission(self, user_id, permission):
        """
        Add a permission to a user.
        :param user_id: The ID of the user.
        :param permission: The permission to be added.
        """
        if user_id not in self.permissions:
            self.permissions[user_id] = []
        self.permissions[user_id].append(permission)
        print(f"Permission '{permission}' added for user {user_id}.")

    def remove_user_permission(self, user_id, permission):
        """
        Remove a permission from a user.
        :param user_id: The ID of the user.
        :param permission: The permission to be removed.
        """
        if user_id in self.permissions and permission in self.permissions[user_id]:
            self.permissions[user_id].remove(permission)
            print(f"Permission '{permission}' removed from user {user_id}.")
        else:
            print(f"Permission '{permission}' not found for user {user_id}.")

    def update_user_permissions(self, user_id, new_permissions):
        """
        Update a user's permissions with a new set of permissions.
        :param user_id: The ID of the user.
        :param new_permissions: A list of new permissions.
        """
        if user_id in self.permissions:
            self.permissions[user_id] = new_permissions
            print(f"Permissions updated for user {user_id}.")
        else:
            print(f"User {user_id} not found.")

    def check_permission(self, user_id, permission):
        """
        Check if a user has a specific permission.
        :param user_id: The ID of the user.
        :param permission: The permission to check.
        :return: True if the user has the permission, False otherwise.
        """
        return permission in self.permissions.get(user_id, [])

    def list_user_permissions(self, user_id):
        """
        List all permissions of a user.
        :param user_id: The ID of the user.
        :return: A list of permissions.
        """
        return self.permissions.get(user_id, [])

# Example usage
if __name__ == '__main__':
    permission_system = UserPermissionSystem()
    permission_system.add_user_permission('user1', 'read')
    permission_system.add_user_permission('user1', 'write')
    print(permission_system.list_user_permissions('user1'))  # ['read', 'write']
    permission_system.remove_user_permission('user1', 'write')
    print(permission_system.list_user_permissions('user1'))  # ['read']
    permission_system.update_user_permissions('user1', ['read', 'delete'])
    print(permission_system.list_user_permissions('user1'))  # ['read', 'delete']
    print(permission_system.check_permission('user1', 'delete'))  # True
