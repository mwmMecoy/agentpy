from functions.get_file_content import get_file_content
from config import MAX_CHARS  

def test():
    content = get_file_content("calculator", "lorem.txt")
    assert not content.startswith("Error:"), content

    assert isinstance(content, str)

    trunc_msg = f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
    assert content.endswith(trunc_msg)

    # Should be longer than MAX_CHARS because of the appended message
    assert len(content) > MAX_CHARS

    # Optional: ensure the returned prefix is exactly MAX_CHARS chars before the message
    assert len(content[:-len(trunc_msg)]) == MAX_CHARS

    # Then print the other required cases (no asserts needed unless you want them)
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test()