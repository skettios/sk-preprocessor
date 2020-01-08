import sys
import pygments
import pygments.lexers
from pygments.token import Token
from cpp_tokenizer import CPPTokenizer
import threading
import multiprocessing


def generate_code(file_path):
    in_file = open(file_path, 'r')
    contents = in_file.read()
    in_file.close()

    tokenizer = CPPTokenizer(contents)

    gl_functions = {}

    while True:
        token_type, token_value = tokenizer.next()
        if token_type == None or token_value == None:
            break
        elif token_type is Token.Name and token_value == 'OPENGL_GENERATE_BEGIN':
            while True:
                gl_type_token_type, gl_type_token_value = tokenizer.next()
                if gl_type_token_type is Token.Keyword and gl_type_token_value == 'extern':
                    continue
                elif gl_type_token_type is Token.Name and gl_type_token_value == 'OPENGL_GENERATE_END':
                    break
                else:
                    gl_func_token_type, gl_func_token_value = tokenizer.next()
                    gl_functions.update(
                        {f"{gl_type_token_value}": f"{gl_func_token_value}"})

    dot_index = file_path.index('.')
    generated_file_name = file_path[0:dot_index]
    generated_file_name += '_generated.h'

    new_header = open(generated_file_name, 'w+')
    print(f"#define OPENGL_FUNCTION_VARIABLES() \\", file=new_header)
    for index in range(len(gl_functions.items())):
        key = list(gl_functions.keys())[index]
        value = gl_functions[key]
        if index == len(gl_functions.items()) - 1:
            print(f"{key} {value};", file=new_header)
        else:
            print(f"{key} {value}; \\", file=new_header)
    new_header.flush()
    print(f"\n#define OPENGL_FUNCTION_LOAD(Func) \\", file=new_header)
    for index in range(len(gl_functions.items())):
        key = list(gl_functions.keys())[index]
        value = gl_functions[key]
        if index == len(gl_functions.items()) - 1:
            print(f"{value} = ({key})Func(\"{value}\");",
                  file=new_header)
        else:
            print(f"{value} = ({key})Func(\"{value}\"); \\",
                  file=new_header)
    new_header.flush()
    print(f"\n#define OPENGL_FUNCTION_POPULATE_TO_STRUCT(Variable) \\", file=new_header)
    for index in range(len(gl_functions.items())):
        key = list(gl_functions.keys())[index]
        value = gl_functions[key]
        if index == len(gl_functions.items()) - 1:
            print(f"Variable.{value} = {value};", file=new_header)
        else:
            print(f"Variable.{value} = {value}; \\", file=new_header)
    new_header.flush()
    print(f"\n#define OPENGL_FUNCTION_POPULATE_FROM_STRUCT(Variable) \\",
          file=new_header)
    for index in range(len(gl_functions.items())):
        key = list(gl_functions.keys())[index]
        value = gl_functions[key]
        if index == len(gl_functions.items()) - 1:
            print(f"{value} = Variable.{value}", file=new_header)
        else:
            print(f"{value} = Variable.{value}; \\", file=new_header)
    new_header.close()

    print(generated_file_name)


def f(x):
    print(x)


def main(args):
    count = len(args)
    max_procs = int(multiprocessing.cpu_count() / 2)
    procs = max_procs if count > max_procs else count
    pool = multiprocessing.Pool(procs)
    for i in range(1, len(args)):
        pool.apply_async(generate_code, args=(args[i],))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main(sys.argv)
