#Python Program for the purpose of the DevOps Assignment 2

import unittest

class MarksCalculator:
    def calculateGrade(self, a1, a2, a3):
        if isinstance(a1, int) and isinstance(a2, int) and isinstance(a3, int):
            total_marks = (a1 * 20 + a2 * 40 + a3 *40)/100  
            grade = "F"
            if total_marks > 85 and total_marks <= 100:
             grade = "HD"
            elif total_marks > 75 and total_marks <=85:
             grade = "D"
            elif total_marks > 65 and total_marks <=75:
             grade = "C"
            elif total_marks >= 50 and total_marks <= 65:
             grade = "P"
            elif total_marks >= 0 and total_marks < 50:
             grade = "F"
            else:
             grade = "ERROR"
            return grade
        else:
            return "ERROR"
    

class tes1TestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = MarksCalculator()

    def test_pass_marks(self):
        result = self.calculator.calculateGrade(50, 50, 50)
        self.assertEqual(result, "P")

    def test_full_marks(self):
        result = self.calculator.calculateGrade(100, 100, 100)
        self.assertEqual(result, "HD")

    def test_fail_marks(self):
        result = self.calculator.calculateGrade(50, 50, 40)
        self.assertEqual(result, "F")

    def test_negative_integers(self):
        result = self.calculator.calculateGrade(-5, -6, -10)
        self.assertEqual(result, "F")

    def test_absent_string(self):
        result = self.calculator.calculateGrade("A", "A", "A")
        self.assertEqual(result, "F")


if __name__ == "__main__":
    unittest.main()