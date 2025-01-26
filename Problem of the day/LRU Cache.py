from collections import OrderedDict

class LRUCache:
    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.cache = OrderedDict()  # Initialize an ordered dictionary
        self.capacity = cap         # Set the capacity of the cache

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end (mark as recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1  # Key not found

    # Function for storing key-value pair.
    def put(self, key, value):
        if key in self.cache:
            # Update the value and mark it as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the least recently used item (first item in the OrderedDict)
            self.cache.popitem(last=False)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends