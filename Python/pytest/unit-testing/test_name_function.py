from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name("Alice", "Bob")
    assert formatted_name == "Alice Bob"
    
