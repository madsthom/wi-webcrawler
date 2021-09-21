import pickle
from pathlib import Path


def save_list(your_list: list, name):
    try:
        with open(name + '.pkl', 'wb') as f:
            pickle.dump(your_list, f)
    except:
        print("Could not open file")
        path = Path(name + '.pkl')
        path.touch(exist_ok=True)
        return []


def diff_list(your_list: list, name):
    stored_list = load_list(name)
    new_list = list(set(stored_list + your_list))
    save_list(new_list, name)


def load_list(name) -> list:
    try:
        with open(name + '.pkl', 'rb') as f:
            return pickle.load(f)
    except:
        print("Could not open file")
        return []
