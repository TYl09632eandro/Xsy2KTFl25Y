# 代码生成时间: 2025-10-10 02:40:25
import numpy as np

"""
Skill Authentication Platform

This module provides a simple platform for skill certification. It allows
users to register their skills, check if their skills are certified, and
retrieve lists of certified skills.

Attributes:
    skills (dict): A dictionary to store the skills and their certifications.

Methods:
    register_skill(skill_id, skill_name): Registers a new skill.
    certify_skill(skill_id): Certifies a given skill.
    get_certified_skills(): Returns a list of all certified skills.
    check_certification(skill_id): Checks if a skill is certified.
"""

class SkillAuthPlatform:
    def __init__(self):
        # Initialize an empty dictionary to store skills and their certifications
        self.skills = {}

    def register_skill(self, skill_id, skill_name):
        """
        Registers a new skill with a unique ID and name.

        Args:
            skill_id (int): Unique identifier for the skill.
            skill_name (str): Name of the skill.

        Raises:
            ValueError: If a skill with the same ID already exists.
        """
        if skill_id in self.skills:
            raise ValueError(f"Skill with ID {skill_id} already exists.")
        self.skills[skill_id] = {"name": skill_name, "certified": False}

    def certify_skill(self, skill_id):
        """
        Certifies a given skill.

        Args:
            skill_id (int): Unique identifier for the skill to be certified.

        Raises:
            ValueError: If the skill ID does not exist.
        """
        if skill_id not in self.skills:
            raise ValueError(f"Skill with ID {skill_id} does not exist.")
        self.skills[skill_id]["certified"] = True

    def get_certified_skills(self):
        """
        Returns a list of all certified skills.

        Returns:
            list: A list of dictionaries containing the skill ID and name of certified skills.
        """
        return [skill for skill in self.skills.values() if skill["certified"]]

    def check_certification(self, skill_id):
        """
        Checks if a skill is certified.

        Args:
            skill_id (int): Unique identifier for the skill to check.

        Returns:
            bool: True if the skill is certified, False otherwise.
        """
        return self.skills.get(skill_id, {}).get("certified", False)

# Example usage
if __name__ == "__main__":
    platform = SkillAuthPlatform()
    try:
        platform.register_skill(1, "Python Programming")
        platform.register_skill(2, "Data Analysis")
        platform.certify_skill(1)
        certified_skills = platform.get_certified_skills()
        print("Certified Skills:", [(skill["name"], skill["certified"]) for skill in certified_skills])
        print("Is Skill 1 Certified?", platform.check_certification(1))
    except ValueError as e:
        print(e)