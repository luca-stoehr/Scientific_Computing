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

  def test_check_syntax(self):
    case1 = "32 + 698"
    self.assertTrue(arithmetic_arranger.check_syntax(case1, True))
    case2 = "3801 - 2"
    self.assertTrue(arithmetic_arranger.check_syntax(case2, False))
    with self.assertRaises(ValueError):
      case3 = "12A3 + 4b9"
      arithmetic_arranger.check_syntax(case3, True)
      case4 = "123 + 4b9"
      arithmetic_arranger.check_syntax(case4, True)
      case5 = "12A3 + 49"
      arithmetic_arranger.check_syntax(case5, True)
      case2 = "38013 - 2"
      arithmetic_arranger.check_syntax(case2, False)

  def test_calc_separator(self):
    case1 = "32 + 698"
    self.assertEqual(arithmetic_arranger.calc_separator(case1, True),('32','698'))
    case2 = "3801 - 2"
    self.assertEqual(arithmetic_arranger.calc_separator(case2, False),('3801','2'))
    with self.assertRaises(ValueError):
      case3 = "3801- 2"
      arithmetic_arranger.calc_separator(case3, False)




if __name__ == '__main__':
  unittest.main()
