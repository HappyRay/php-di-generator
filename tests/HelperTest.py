import unittest
from helper import Helper


class TestHelper(unittest.TestCase):
    
    def test_parse_definition_string(self):
        data = ' * @var FooClass |  BarClass '
        class_list = Helper.parse_definition_string(data)
        expected = ['FooClass', 'BarClass']
        self.assertEqual(expected, class_list)

    def test_strip_extra(self):
        data = ' * @var FooClass  '
        class_def = Helper.strip_extra(data)
        expected = 'FooClass'
        self.assertEqual(expected, class_def)

    def test_get_var_name(self):
        data = 'FooClass'
        var_name = Helper.get_var_name(data)
        expected = 'fooClass'
        self.assertEquals(expected, var_name)


if __name__ == '__main__':
    unittest.main()
