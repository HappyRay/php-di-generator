"""
Helper methods
"""
class Helper(object):
    
    @classmethod
    def parse_definition_string(cls, definition):
        '''
        Parse the definition string and return the list of dependent classes.
        
        :type definition: str
        :param definition: string with a list of dependent classes 
        :return: a list of class strings
        '''
        class_list_raw = definition.split('|')
        class_list = [cls.strip_extra(class_def) for class_def in class_list_raw]
        
        return class_list

    @classmethod
    def strip_extra(cls, one_def):
        """
        Remove extra characters around the class name.
        
        :type one_def: str
        """
        no_var = one_def.replace('@var', '')
        no_star = no_var.replace('*', '')
        class_def = no_star.lstrip().rstrip()
        
        return class_def

    @classmethod
    def get_var_name(cls, class_name):
        """
        Return the variable name based on the class name
        
        The name is the same with the first letter turned 
        into local case.
        
        :type class_name: str
        """
        var_name = class_name[0].lower() + class_name[1:]
        
        return var_name
    
