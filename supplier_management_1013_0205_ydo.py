# 代码生成时间: 2025-10-13 02:05:06
import numpy as np

"""
供应商管理系统
"""

class Supplier:
    # 供应商类，用于创建供应商对象
    def __init__(self, name, contact_info):
        self.name = name  # 供应商名称
        self.contact_info = contact_info  # 供应商联系方式

    def __str__(self):
        # 返回供应商信息的字符串表示
        return f"Supplier(Name: {self.name}, Contact Info: {self.contact_info})"


class SupplierManager:
    # 供应商管理器类，用于管理供应商信息
    def __init__(self):
        self.suppliers = []  # 存储供应商对象的列表

    def add_supplier(self, supplier):
        # 添加供应商
        if not isinstance(supplier, Supplier):
            raise ValueError("Invalid supplier type")
        self.suppliers.append(supplier)

    def remove_supplier(self, name):
        # 根据名称移除供应商
        for supplier in self.suppliers:
            if supplier.name == name:
                self.suppliers.remove(supplier)
                return
        raise ValueError(f"Supplier with name {name} not found")

    def find_supplier(self, name):
        # 根据名称查找供应商
        for supplier in self.suppliers:
            if supplier.name == name:
                return supplier
        raise ValueError(f"Supplier with name {name} not found")

    def list_suppliers(self):
        # 列出所有供应商
        return self.suppliers

# 示例用法
def main():
    manager = SupplierManager()
    
    # 添加供应商
    try:
        manager.add_supplier(Supplier("Supplier1", "Contact1"))
        manager.add_supplier(Supplier("Supplier2", "Contact2"))
    except ValueError as e:
        print(e)

    # 列出所有供应商
    suppliers = manager.list_suppliers()
    for supplier in suppliers:
        print(supplier)

    # 查找供应商
    try:
        supplier = manager.find_supplier("Supplier1")
        print(f"Found Supplier: {supplier}")
    except ValueError as e:
        print(e)

    # 移除供应商
    try:
        manager.remove_supplier("Supplier1")
    except ValueError as e:
        print(e)

    # 再次列出所有供应商
    suppliers = manager.list_suppliers()
    for supplier in suppliers:
        print(supplier)

if __name__ == "__main__":
    main()