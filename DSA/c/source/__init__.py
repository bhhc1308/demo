import check50
import check50.c

@check50.check()
def exists():
    """sort.c exists"""
    check50.exists("sort.c")
    check50.include("../../source/3_input_input.txt", "../../source/3_input_output.txt")

@check50.check(exists)
def compiles():
    """sort.c compiles"""
    check50.c.compile("sort.c", lcs50=False)

@check50.check(compiles)
def 3_input():
    """3_input"""
    test_input_output("3_input_input.txt", "3_input_output.txt")

# Helpers
def test_input_output(input_file, output_file):
    """A function to test a single input/output pair"""
    executable = "./" + "DSA"
    check50.run(executable).stdin(open(input_file).read(), prompt=False).stdout(open(output_file).read(), regex=False).exit()
