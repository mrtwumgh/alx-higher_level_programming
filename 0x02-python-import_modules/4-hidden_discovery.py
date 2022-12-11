#!/usr/bin/python3
if __name__ == '__main__':
    import importlib.util
    import os
    import sys

    module_path = "hidden_4.pyc"

    if not os.path.exists(module_path):
        sys.exit(1)

    spec = importlib.util.spec_from_file_location("hidden_4", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = dir(module)

    filtered_names = []
    for name in names:
        if not name.startswith("__"):
            filtered_names.append(name)
    filtered_names.sort()

    for name in filtered_names:
        print(name)
