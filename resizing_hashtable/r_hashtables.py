

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_key = hash(key, hash_table.capacity)
    pair = LinkedPair(key, value)
    if hash_table.storage[hash_key] is not None and hash_table.storage[hash_key].key != key:
        hash_table.storage[hash_key].next = pair
    elif hash_table.storage[hash_key] is not None and hash_table.storage[hash_key].key == key:
        hash_table.storage[hash_key].value = value
    elif hash_table.storage[hash_key] is None:
        hash_table.storage[hash_key] = pair
    elif hash_table.storage[hash_key].next is not None and hash_table.storage[hash_key].next.key == key:
        hash_table.storage[hash_key].next.value = value
    elif hash_table.storage[hash_key].next is not None and hash_table.storage[hash_key].next.key != key:
        print('Can not insert')
    else:
        hash_table.table.storage[hash_key].next = pair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''


def hash_table_remove(hash_table, key):
    hash_key = hash(key, hash_table.capacity)

    if hash_table.storage[hash_key] is None or hash_table.storage[hash_key].key != key:
        hash_table.storage[hash_key].next = None
    else:
        hash_table.storage[hash_key] = hash_table.storage[hash_key].next

# '''
# Fill this in.

# Should return None if the key is not found.
# '''


def hash_table_retrieve(hash_table, key):
    hash_key = hash(key, hash_table.capacity)

    if hash_table.storage[hash_key] is None:
        return None
    elif hash_table.storage[hash_key].next is not None and hash_table.storage[hash_key].key != key:
        return hash_table.storage[hash_key].next.value
    # elif hash_table.storage[hash_key].key != key or hash_table.storage[hash_key].next is None:
    #     return None
    else:
        return hash_table.storage[hash_key].value


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_capacity = hash_table.capacity * 2

    new_elements = [None] * new_capacity

    for i in range(len(hash_table.storage)):
        new_elements[i] = hash_table.storage[i]

    hash_table.storage = new_elements
    hash_table.capacity = new_capacity
    return hash_table


def Testing():
    ht = HashTable(8)

    hash_table_insert(ht, "key-0", "val-0")
    hash_table_insert(ht, "key-1", "val-1")
    hash_table_insert(ht, "key-2", "val-2")
    hash_table_insert(ht, "key-3", "val-3")
    hash_table_insert(ht, "key-4", "val-4")
    hash_table_insert(ht, "key-5", "val-5")
    hash_table_insert(ht, "key-6", "val-6")
    hash_table_insert(ht, "key-7", "val-7")
    hash_table_insert(ht, "key-8", "val-8")
    hash_table_insert(ht, "key-9", "val-9")

    hash_table_insert(ht, "key-0", "new-val-0")
    hash_table_insert(ht, "key-1", "new-val-1")
    hash_table_insert(ht, "key-2", "new-val-2")
    hash_table_insert(ht, "key-3", "new-val-3")
    hash_table_insert(ht, "key-4", "new-val-4")
    hash_table_insert(ht, "key-5", "new-val-5")
    hash_table_insert(ht, "key-6", "new-val-6")
    hash_table_insert(ht, "key-7", "new-val-7")
    hash_table_insert(ht, "key-8", "new-val-8")
    hash_table_insert(ht, "key-9", "new-val-9")
    return_value = hash_table_retrieve(ht, "key-0")
    return_value = hash_table_retrieve(ht, "key-1")
    return_value = hash_table_retrieve(ht, "key-2")
    return_value = hash_table_retrieve(ht, "key-3")
    return_value = hash_table_retrieve(ht, "key-4")
    return_value = hash_table_retrieve(ht, "key-5")
    return_value = hash_table_retrieve(ht, "key-6")
    return_value = hash_table_retrieve(ht, "key-7")
    return_value = hash_table_retrieve(ht, "key-8")
    return_value = hash_table_retrieve(ht, "key-9")
    # ht = HashTable(2)

    # hash_table_insert(ht, "line_1", "Tiny hash table")
    # hash_table_insert(ht, "line_2", "Filled beyond capacity")
    # hash_table_insert(ht, "line_3", "Linked list saves the day!")

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
