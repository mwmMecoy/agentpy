from functions.get_files_info import get_files_info

def test():
    # Test 1: current directory
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    # ... add the other test cases
    result2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result2)

    result3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result3)

    result4 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result4)

if __name__ == "__main__":
    test()