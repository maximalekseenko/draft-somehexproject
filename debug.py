_class_info_deepness=0


def _class_info(value):
    return f"{'│ '*(_class_info_deepness-1)}├{value}"


def class_info(title:str, variables:dict):
    global _class_info_deepness
    _class_info_deepness += 1

    # title
    ret = title
    # values
    for variable_title, variable_value in variables.items():
        ret += '\n'
        ret += _class_info(variable_title)
        ## value is not list
        if type(variable_value) is not list:
            ret += ': '
            ret += repr(variable_value)
            continue
        ## value is list
        _class_info_deepness += 1
        for index in range(len(variable_value)):
            ret += f'\n'
            ret += _class_info(f'[{index}]: '+repr(variable_value[index]))
        _class_info_deepness -= 1
    # return
    _class_info_deepness-=1
    return ret