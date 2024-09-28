'''from cx_Freeze import setup, Executable

setup(name="pythonCX_Freeze",
      version="0.1",
      description="",
      executables=[Executable("Camera_VI_Tablet.py")])'''
'''# The cx_Freeze setup.py script
from cx_Freeze import setup, Executable

setup(
    name="",
    version="0.1",
    description="",
    executables=[Executable("D:\\Manh\\Source\\Python\\CameraVITablet\\Camera_VI_Tablet.py")],
)'''
from distutils.core import setup
from Cython.Build import cythonize

setup(name='Module',
      ext_modules=cythonize("dannyview.py"))#("Camera_VI_Tablet.py"))#,
      #zip_safe = False)
#python setup.py build_ext --inplace
