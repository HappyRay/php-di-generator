import unittest
from generator.generator import Generator


class TestGenerator(unittest.TestCase):

    def test_generate_statements(self):
        data = ' * @var Foo |  Bar '
        statements = Generator.generate_statements(data)
        expected = '''    /** @var Foo */
    private $foo;

    /** @var Bar */
    private $bar;

    function __construct(
        Foo $foo,
        Bar $bar
    )
    {
        $this->foo = $foo;
        $this->bar = $bar;
    }    
'''
        self.assertEqual(expected, statements)

if __name__ == '__main__':
    unittest.main()

