# Your code here

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    names_dict = {}
    result = []
    for name in queries:
        names_dict[name] = name
    for file in files:
        file_name = file.rsplit('/',1)[1]
        if file_name in names_dict:
            result.append(file)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
