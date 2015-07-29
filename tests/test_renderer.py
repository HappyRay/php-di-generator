import unittest
from generator.renderer import Renderer


class TestRenderer(unittest.TestCase):
    
    def test_gen_member_statement(self):
        data = 'Foo'
        member_def = Renderer.gen_member_statement(data)
        expected = "    /** @var Foo */\n    private $foo;\n"
        self.assertEqual(expected, member_def)

    def test_gen_all_members(self):
        data = ['Foo', 'Bar']
        member_def = Renderer.gen_all_members(data)
        expected = '''    /** @var Foo */
    private $foo;

    /** @var Bar */
    private $bar;
'''
        self.assertEqual(expected, member_def)

    def test_gen_constructor_param(self):
        data = 'Foo'
        param_def = Renderer._gen_constructor_param(data)
        expected = "        Foo $Foo"
        self.assertEqual(expected, param_def)

    def test_gen_constructor_param(self):
        data = ['Foo', 'Bar']
        params = Renderer._gen_constructor_all_params(data)
        expected = "        Foo $foo,\n        Bar $bar"
            
        self.assertEqual(expected, params)

    def test_gen_constructor_assignment(self):
        data = 'Foo'
        param_def = Renderer._gen_constructor_assignment(data)
        expected = "        $this->foo = $foo;"
        self.assertEqual(expected, param_def)

    def test_gen_constructor_all_assignments(self):
        data = ['Foo', 'Bar']
        params = Renderer._gen_constructor_all_assignments(data)
        expected = "        $this->foo = $foo;\n        $this->bar = $bar;"
            
        self.assertEqual(expected, params)

    def test_gen_constructor(self):
        data = ['Foo', 'Bar']
        params = Renderer.gen_constructor_statement(data)
        expected = '''
    function __construct(
        Foo $foo,
        Bar $bar
    )
    {
        $this->foo = $foo;
        $this->bar = $bar;
    }    
'''
        self.assertEqual(expected, params)

if __name__ == '__main__':
    unittest.main()
