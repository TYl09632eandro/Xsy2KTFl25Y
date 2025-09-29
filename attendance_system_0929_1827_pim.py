# 代码生成时间: 2025-09-29 18:27:47
import numpy as np
import datetime

"""
考勤打卡系统

该系统记录员工的打卡信息，并提供打卡功能。
"""

class AttendanceSystem:
    def __init__(self):
        """初始化考勤系统"""
        self.employees = {}
        self.records = []

    def add_employee(self, employee_id, name):
        """添加员工

        Args:
            employee_id (str): 员工ID
            name (str): 员工姓名
        """
        if employee_id in self.employees:
            raise ValueError(f"Employee {employee_id} already exists.")
        self.employees[employee_id] = name

    def clock_in(self, employee_id):
        """员工打卡

        Args:
            employee_id (str): 员工ID
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee {employee_id} does not exist.")
        record = {
            'employee_id': employee_id,
            'name': self.employees[employee_id],
            'clock_in_time': datetime.datetime.now()
        }
        self.records.append(record)
        print(f"Employee {employee_id} clocked in at {record['clock_in_time']}")

    def clock_out(self, employee_id):
        """员工打卡

        Args:
            employee_id (str): 员工ID
        """
        if employee_id not in self.employees:
            raise ValueError(f"Employee {employee_id} does not exist.")
        record = {
            'employee_id': employee_id,
            'name': self.employees[employee_id],
            'clock_out_time': datetime.datetime.now()
        }
        for i, existing_record in enumerate(self.records):
            if (existing_record['employee_id'] == employee_id and
                    'clock_out_time' not in existing_record):
                existing_record['clock_out_time'] = record['clock_out_time']
                print(f"Employee {employee_id} clocked out at {record['clock_out_time']}")
                break
        else:
            raise ValueError(f"No clock-in record found for employee {employee_id}.")

    def get_attendance_records(self, employee_id=None):
        """获取考勤记录

        Args:
            employee_id (str, optional): 员工ID. Defaults to None.

        Returns:
            list: 考勤记录列表
        """
        if employee_id:
            return [record for record in self.records if record['employee_id'] == employee_id]
        else:
            return self.records

# 示例用法
if __name__ == '__main__':
    system = AttendanceSystem()
    system.add_employee('001', 'John Doe')
    system.add_employee('002', 'Jane Doe')

    system.clock_in('001')
    system.clock_out('001')

    system.clock_in('002')
    system.clock_out('002')

    records = system.get_attendance_records('001')
    for record in records:
        print(record)