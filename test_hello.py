from hello import toyou, add, substract

def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10

def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x

def test_hello_substract():
    assert substract(test_hello_substract.x) == 9
