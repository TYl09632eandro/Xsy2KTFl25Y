# 代码生成时间: 2025-10-09 18:28:37
import numpy as np

"""
家校沟通工具

该程序旨在通过numpy框架实现家校沟通的基本功能，包括学生信息管理、
成绩记录和家校通知。
"""

class Student:
    """学生信息类"""
    def __init__(self, name, grade, parent_name):
        self.name = name  # 学生姓名
        self.grade = grade  # 学生年级
        self.parent_name = parent_name  # 家长姓名
        self.scores = np.array([])  # 学生成绩，使用numpy数组存储

    def record_score(self, score):
        """记录学生成绩"""
        self.scores = np.append(self.scores, score)

    def get_average_score(self):
        """计算学生平均成绩"""
        if len(self.scores) == 0:
            raise ValueError("No scores recorded yet.")
        return np.mean(self.scores)

    def get_grade_level(self):
        """根据学生平均成绩确定年级水平"""
        if len(self.scores) == 0:
            raise ValueError("No scores recorded yet.")
        average_score = self.get_average_score()
        if average_score >= 90:
            return "A"
        elif average_score >= 80:
            return "B"
        elif average_score >= 70:
            return "C"
        else:
            return "D"

class SchoolCommunication:
    """家校沟通工具类"""
    def __init__(self):
        self.students = []  # 学生列表

    def add_student(self, student):
        """添加学生信息"""
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class.")
        self.students.append(student)

    def get_student_scores(self, student_name):
        """获取指定学生的成绩列表"""
        for student in self.students:
            if student.name == student_name:
                return student.scores
        raise ValueError(f"Student {student_name} not found.")

    def notify_parent(self, student_name, message):
        """向家长发送通知"""
        for student in self.students:
            if student.name == student_name:
                print(f"Dear {student.parent_name}, {message}")
                return
        raise ValueError(f"Student {student_name} not found.\)

# Example usage
if __name__ == '__main__':
    communication = SchoolCommunication()
    
    student1 = Student("Alice", 10, "John")
    student1.record_score(85)
    student1.record_score(90)
    student1.record_score(78)
    
    student2 = Student("Bob", 10, "Jane")
    student2.record_score(92)
    student2.record_score(88)
    student2.record_score(95)
    
    communication.add_student(student1)
    communication.add_student(student2)
    
    try:
        average_score = student1.get_average_score()
        print(f"Alice's average score: {average_score}")
        grade_level = student1.get_grade_level()
        print(f"Alice's grade level: {grade_level}")
        communication.notify_parent("Alice", "Your average score is {0}. Keep up the good work!".format(average_score))
    except Exception as e:
        print(f"Error: {e}")
