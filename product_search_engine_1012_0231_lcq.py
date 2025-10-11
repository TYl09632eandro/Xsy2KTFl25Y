# 代码生成时间: 2025-10-12 02:31:24
import numpy as np

"""
商品搜索引擎
===============

该程序实现了一个简单的商品搜索引擎，能够根据用户输入的查询词，
从预定义的商品库存中查找匹配的商品。

Attributes:
    products (list of dict): 存储商品信息的列表。

Methods:
    search_products(query): 根据查询词搜索商品。
"""

# 预定义的商品库存
products = [
    {'id': 1, 'name': 'Apple iPhone 13', 'category': 'Electronics', 'price': 799},
    {'id': 2, 'name': 'Samsung Galaxy S22', 'category': 'Electronics', 'price': 899},
    {'id': 3, 'name': 'Google Pixel 6', 'category': 'Electronics', 'price': 599},
    {'id': 4, 'name': 'Dell XPS 13', 'category': 'Electronics', 'price': 999},
    {'id': 5, 'name': 'Apple MacBook Pro', 'category': 'Electronics', 'price': 1299},
    {'id': 6, 'name': 'Nike Air Zoom Pegasus', 'category': 'Clothing', 'price': 110},
    {'id': 7, 'name': 'Adidas Ultraboost', 'category': 'Clothing', 'price': 180},
    {'id': 8, 'name': 'Levi's 501 Jeans', 'category': 'Clothing', 'price': 50},
    {'id': 9, 'name': 'Ray-Ban Aviator Sunglasses', 'category': 'Accessories', 'price': 150}
]


def search_products(query):
    """
    根据查询词搜索商品。
    
    Args:
        query (str): 用户输入的查询词。
    
    Returns:
        list of dict: 匹配的商品列表。
    
    Raises:
        ValueError: 如果查询词为空或无效。
    """
    if not query:
        raise ValueError("查询词不能为空。")
    
    # 将查询词转换为小写，以便进行不区分大小写的搜索
    query = query.lower()
    
    # 使用列表推导式搜索匹配的商品
    matched_products = [product for product in products if query in product['name'].lower()]
    
    return matched_products

# 示例用法
if __name__ == '__main__':
    try:
        query = input("请输入查询词：")
        results = search_products(query)
        if results:
            print("搜索结果：")
            for product in results:
                print(f"ID: {product['id']}, 名称：{product['name']}, 类别：{product['category']}, 价格：{product['price']}")
        else:
            print("没有找到匹配的商品。")
    except ValueError as e:
        print(e)