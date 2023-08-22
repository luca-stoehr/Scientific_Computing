import unittest
import arithmetic_arranger


class TestArithmetic_Arranger(unittest.TestCase):

  def test_limit_calculations(self):
    case1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    self.assertTrue(arithmetic_arranger.limit_calculations(case1))
    case2 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "45 + 43"]
    self.assertTrue(arithmetic_arranger.limit_calculations(case2))

    with self.assertRaises(ValueError):
      case3 = [
        "32 + 698", "3801 - 2", "45 + 43", "123 + 49", "45 + 43", "123 + 49"
      ]
      arithmetic_arranger.limit_calculations(case3)
      case4 = []
      arithmetic_arranger.limit_calculations(case4)

  def test_find_operator(self):
    case1 = "32 + 698"
    self.assertTrue(arithmetic_arranger.find_operator(case1))
    case2 = "3801 - 2"
    self.assertFalse(arithmetic_arranger.find_operator(case2))

    with self.assertRaises(ValueError):
      case3 = "45 / 43"
      arithmetic_arranger.find_operator(case3)
      case4 = "123  49"
      arithmetic_arranger.find_operator(case4)


if __name__ == '__main__':
  unittest.main()
