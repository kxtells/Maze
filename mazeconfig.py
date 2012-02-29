import os

class project_path_not_found(Exception):
    pass

def getdatapath():
    """Retrieve test data path

    This path is by default <test_lib_path>/../data/ in trunk
    and /usr/share/test in an installed version but this path
    is specified at installation time.
    """

    pathname = os.path.dirname(__file__) + '/'

    abs_data_path = os.path.abspath(pathname)
    if os.path.exists(abs_data_path):
        return abs_data_path +'/'
    else:
        raise project_path_not_found


