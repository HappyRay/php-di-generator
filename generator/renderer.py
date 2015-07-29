"""
Generate PHP code
"""
from helper import Helper


class Renderer(object):
    @classmethod
    def gen_member_statement(cls, class_name):
        '''
        Generate member variable definition.
        
        :type class_name: str
        '''
        var_name = Helper.get_var_name(class_name)
        result = "    /** @var %s */\n    private $%s;\n" % (
            class_name, var_name
        )

        return result

    @classmethod
    def gen_all_members(cls, class_list):
        '''
        Generate all member variable definitions.
        
        :type class_list: list
        '''
        members = [cls.gen_member_statement(class_name) for class_name in class_list]
        result = '\n'.join(members)

        return result


    @classmethod
    def gen_constructor_statement(cls, class_name_list):
        '''
        Generate constructor statement.
        
        :type class_name_list: list
        '''
        params = cls._gen_constructor_all_params(class_name_list)
        assignments = cls._gen_constructor_all_assignments(class_name_list)
        resultFormat = '''
    function __construct(
%s
    )
    {
%s
    }    
'''
        result = resultFormat % (
            params,
            assignments
        )
    
        return result
    
    
    @classmethod
    def _gen_constructor_param(cls, class_name):
        '''
        Generate one parameter statement for the constructor.
        
        :type class_name: str
        '''
        var_name = Helper.get_var_name(class_name)
        result = '        %s $%s' % (
            class_name,
            var_name
        )
    
        return result
    
    
    @classmethod
    def _gen_constructor_all_params(cls, class_name_list):
        '''
        Generate all parameter statements for the constructor.
        
        :type class_name_list: list
        '''
        param_statements = [
            cls._gen_constructor_param(class_name) for class_name in class_name_list
        ]
        result = ',\n'.join(param_statements)
    
        return result
    
    
    @classmethod
    def _gen_constructor_assignment(cls, class_name):
        '''
        Generate one assignment statement for the constructor.
        
        :type class_name: str
        '''
        var_name = Helper.get_var_name(class_name)
        result = '        $this->%s = $%s;' % (
            var_name,
            var_name
        )
    
        return result
    
    
    @classmethod
    def _gen_constructor_all_assignments(cls, class_name_list):
        '''
        Generate all assignment statements for the constructor.
        
        :type class_name_list: list
        '''
        statements = [
            cls._gen_constructor_assignment(class_name) for class_name in class_name_list
        ]
        result = '\n'.join(statements)
    
        return result
