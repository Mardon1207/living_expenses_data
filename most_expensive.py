import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f=open('data.json')
    x=json.load(f)
    m=0
    for i in x.values():
        if m<i:
            m=i
    return m
# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)