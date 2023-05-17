import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    f=open('data.json')
    x=json.load(f)
    m=100000
    for i in x.values():
        if m>i:
            m=i
    return m

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
