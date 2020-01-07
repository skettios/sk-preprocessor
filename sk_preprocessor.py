import sys
import pygments
import pygments.lexers
from pygments.token import Token
from cpp_tokenizer import CPPTokenizer


def main(args):
    header = open(args[0], 'r')
    content = header.read()
    header.close()
    tokenizer = CPPTokenizer(content)

    gl_functions = {}

    while (tokenizer.has_next()):
        ttype, value = tokenizer.next()
        if ttype is Token.Name and value == 'OPENGL_GENERATE_BEGIN':
            while tokenizer.has_next():
                gl_type, gl_func = tokenizer.next()
                if gl_type is Token.Keyword and gl_func == 'extern':
                    continue
                elif gl_type is Token.Name and gl_func == 'OPENGL_GENERATE_END':
                    break
                else:
                    if (tokenizer.has_next()):
                        ngl_type, ngl_func = tokenizer.next()
                        gl_functions.update({f"{gl_func}": f"{ngl_func}"})

    new_header = open('test_generated.h', 'w+')
    print(f"#define OPENGL_FUNCTION_VARIABLES() \\", file=new_header)
    for index in range(len(gl_functions.items())):
        key = list(gl_functions.keys())[index]
        value = gl_functions[key]
        if index == len(gl_functions.items()) - 1:
            print(f"    {key} {value};", file=new_header)
        else:
            print(f"    {key} {value}; \\", file=new_header)
    new_header.close()


if __name__ == '__main__':
    arguments = ['test.h']
    main(arguments)
