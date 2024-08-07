from dfp import parse_file
import os

# pip install pytest in the terminal
# pytest -v dfp_test.py


def test_01_parse_function_declared():
    """Verify the parseFile function is defined."""
    assert callable(parse_file)  # Check if parseFile is a callable function

def test_02_basic_operation():
    """Test parsing a simple CSV file."""
    test_input = "./testing/testdata_5.csv"
    test_output = "./testing/outputfile_test.csv"
    test_exported_records = 5

    # Ensure test file exists
    assert os.path.exists(test_input)
    
    result = parse_file(test_input, test_output)
    assert result == test_exported_records

def test_03_export_created():
    """Verify that the output file is created."""
    test_input = "./testing/testdata_5.csv"
    test_output = "./testing/outputfile_test.csv"
    test_exported = 5

    # Ensure test file exists
    assert os.path.exists(test_input)
    
    # Remove if file exists
    if os.path.exists(test_output):
        os.remove(test_output)

    result = parse_file(test_input, test_output)
    assert result == test_exported
    assert os.path.exists(test_output)

def test_04_export_file_size():
    """Test if output file size remains consistent after multiple calls."""
    test_input = "./testing/testdata_5.csv"
    test_output = "./testing/outputfile_test.csv"
    test_exported = 5

    # Ensure test file exists
    assert os.path.exists(test_input)

    # Remove if file exists
    if os.path.exists(test_output):
        os.remove(test_output)

    parse_file(test_input, test_output)
    initial_size = os.stat(test_output).st_size  # Get initial file size

    parse_file(test_input, test_output)  
    final_size = os.stat(test_output).st_size  # Get final file size

    assert initial_size == final_size

def test_05_source_file_exists():
    """Check behavior when the source file doesn't exist."""
    test_input = "./testing/DOESNOTEXIST.csv"
    test_output = "./testing/outputfile_test.csv"
    test_exported = -1

    result = parse_file(test_input, test_output)
    assert result == test_exported

def test_06_export_results_confirmation():
    """Verify that the parsed output matches the expected string."""
    test_input = "./testing/testdata_1.csv"
    test_output = "./testing/outputfile_test.csv"
    test_output_string = "positive;Alpha Beta Gamma Del\n"  
    test_exported = 1

    if os.path.exists(test_output):  
        os.remove(test_output)  # Remove existing output file

    result = parse_file(test_input, test_output)  
    assert result == test_exported

    with open(test_output, "r") as f:
        output_content = f.read()
    assert output_content == test_output_string  

def test_07_export_results_comma_delimiter_confirmation():
    """Verify output with comma delimiter."""
    test_input = "./testing/testdata_1_comma.csv"
    test_output = "./testing/outputfile_test.csv"
    test_output_string = "positive,Alpha Beta Gamma Del\n" 
    test_exported = 1

    if os.path.exists(test_output):
        os.remove(test_output)  

    result = parse_file(test_input, test_output, ",") 
    assert result == test_exported

    with open(test_output, "r") as f:
        output_content = f.read()
    assert output_content == test_output_string