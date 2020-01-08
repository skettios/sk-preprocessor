#define OPENGL_FUNCTION_VARIABLES() \
PFNGLGENVERTEXARRAYSPROC glGenVertexArrays; \
PFNGLBINDVERTEXARRAYPROC glBindVertexArray; \
PFNGLGENBUFFERSPROC glGenBuffers; \
PFNGLBINDBUFFERPROC glBindBuffer; \
PFNGLBUFFERDATAPROC glBufferData; \
PFNGLENABLEVERTEXATTRIBARRAYPROC glEnableVertexAttribArray; \
PFNGLDISABLEVERTEXATTRIBARRAYPROC glDisableVertexAttribArray; \
PFNGLVERTEXATTRIBPOINTERPROC glVertexAttribPointer; \
PFNGLCREATESHADERPROC glCreateShader; \
PFNGLDELETESHADERPROC glDeleteShader; \
PFNGLDETACHSHADERPROC glDetachShader; \
PFNGLSHADERSOURCEPROC glShaderSource; \
PFNGLLINKPROGRAMPROC glLinkProgram; \
PFNGLCREATEPROGRAMPROC glCreateProgram; \
PFNGLCOMPILESHADERPROC glCompileShader; \
PFNGLGETSHADERIVPROC glGetShaderiv; \
PFNGLGETSHADERINFOLOGPROC glGetShaderInfoLog; \
PFNGLGETPROGRAMIVPROC glGetProgramiv; \
PFNGLGETPROGRAMINFOLOGPROC glGetProgramInfoLog; \
PFNGLATTACHSHADERPROC glAttachShader; \
PFNGLUSEPROGRAMPROC glUseProgram;

#define OPENGL_FUNCTION_LOAD(Func) \
glGenVertexArrays = (PFNGLGENVERTEXARRAYSPROC)Func("glGenVertexArrays"); \
glBindVertexArray = (PFNGLBINDVERTEXARRAYPROC)Func("glBindVertexArray"); \
glGenBuffers = (PFNGLGENBUFFERSPROC)Func("glGenBuffers"); \
glBindBuffer = (PFNGLBINDBUFFERPROC)Func("glBindBuffer"); \
glBufferData = (PFNGLBUFFERDATAPROC)Func("glBufferData"); \
glEnableVertexAttribArray = (PFNGLENABLEVERTEXATTRIBARRAYPROC)Func("glEnableVertexAttribArray"); \
glDisableVertexAttribArray = (PFNGLDISABLEVERTEXATTRIBARRAYPROC)Func("glDisableVertexAttribArray"); \
glVertexAttribPointer = (PFNGLVERTEXATTRIBPOINTERPROC)Func("glVertexAttribPointer"); \
glCreateShader = (PFNGLCREATESHADERPROC)Func("glCreateShader"); \
glDeleteShader = (PFNGLDELETESHADERPROC)Func("glDeleteShader"); \
glDetachShader = (PFNGLDETACHSHADERPROC)Func("glDetachShader"); \
glShaderSource = (PFNGLSHADERSOURCEPROC)Func("glShaderSource"); \
glLinkProgram = (PFNGLLINKPROGRAMPROC)Func("glLinkProgram"); \
glCreateProgram = (PFNGLCREATEPROGRAMPROC)Func("glCreateProgram"); \
glCompileShader = (PFNGLCOMPILESHADERPROC)Func("glCompileShader"); \
glGetShaderiv = (PFNGLGETSHADERIVPROC)Func("glGetShaderiv"); \
glGetShaderInfoLog = (PFNGLGETSHADERINFOLOGPROC)Func("glGetShaderInfoLog"); \
glGetProgramiv = (PFNGLGETPROGRAMIVPROC)Func("glGetProgramiv"); \
glGetProgramInfoLog = (PFNGLGETPROGRAMINFOLOGPROC)Func("glGetProgramInfoLog"); \
glAttachShader = (PFNGLATTACHSHADERPROC)Func("glAttachShader"); \
glUseProgram = (PFNGLUSEPROGRAMPROC)Func("glUseProgram");
