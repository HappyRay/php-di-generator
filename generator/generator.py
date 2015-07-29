"""
Main class for doing the work.
"""

from helper import Helper
from renderer import Renderer
from pyperclip.pyperclip import copy

class Generator(object):
    
    @classmethod
    def generate_statements(cls, class_list_def):
        """

        :type class_list_def: str
        """
        class_def_list = Helper.parse_definition_string(class_list_def)
        member_def_statement = Renderer.gen_all_members(class_def_list)
        constructor_statement = Renderer.gen_constructor_statement(class_def_list)
        result = member_def_statement + constructor_statement
        copy(result)

        return result
        
