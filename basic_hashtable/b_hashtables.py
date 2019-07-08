# '''
# Basic hash table key/value pair
# '''


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string):
    hash = 0
    for x in string:
        hash += ord(x)
    return hash % len(string)


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):

    # '''
    # Fill this in.

    # If you try to remove a value that isn't there, print a warning.
    # '''
    hash_key = hash(key)
    if hash_table.storage[hash_key] is None:
        hash_table.storage[hash_key] = list(value)
        return True
    else:
        for pair in hash_table.storage[hash_key]:
            if pair[0] == key:
                pair[1] = value
                return True
        hash_table.storage[hash_key].append(value)
        return True


def hash_table_remove(hash_table, key):
    hash_key = hash(key)

    if hash_table.storage[hash_key] is None:
        return False
    else:
        hash_table.storage.pop(hash_key)


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hash_key = hash(key)

    if hash_table.storage[hash_key] is None:
        print("ERROR: " + str(key) + " could not be found!")
        return None
    else:
        return hash_table.storage[hash_key]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
