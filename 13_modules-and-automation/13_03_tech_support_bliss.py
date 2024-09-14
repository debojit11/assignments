# Use the built-in `platform` module to print out the following info:
import platform
placeholder = "remove me :)"
 
print(f"{'Platform:':>10} ,{platform.platform()}")
print(f"{'Compiler:':>10} ,{platform.python_compiler()}")
print(f"{'Python:':>10} ,{platform.python_version()}")
print(f"{'System:':>10} ,{platform.system()}")
print(f"{'Release:':>10} ,{platform.release()}")
print(f"{'System:':>10} ,{platform.processor()}")