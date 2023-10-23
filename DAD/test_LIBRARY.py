import unittest
import sort_perc_library

class TestLibrary(unittest.TestCase):

    def test_CalculatePercentage(self):
        # result = sort_perc_library.CalculatePercentage(20, 40)
        # self.assertEqual(result, 50)
        # or
        self.assertEqual(sort_perc_library.CalculatePercentage(20, 40), 57)




    def test_SortName(self):
        result = sort_perc_library.SortNames(["Mansi", "Bindu", "Krish", "Vanshu"], order = "ascending")
        self.assertEqual(result, ["Bindu", "Krish", "jhg", "Vanshu"])




if __name__ == '__main__':
    unittest.main()




