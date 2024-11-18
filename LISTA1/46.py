def inverte_string_recursiva(s):
    if len(s) == 0:
        return s
    return inverte_string_recursiva(s[1:]) + s[0]
