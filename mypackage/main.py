from mypackage.parameters import parameters
from mypackage.module_3 import module_3


results = list(map(module_3.wrapper_for_print_and_type, parameters.package_data))
print(results)
