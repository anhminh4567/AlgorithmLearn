class HashSet:
    def __init__(self, capacity):
        self._capacity = capacity  # Number of buckets
        self._size = 0  # Number of elements in the set
        self._buckets = [[] for _ in range(capacity)]  # List of buckets (each bucket is a list)
    def _hash(self, value):
        """Compute the hash index for a given value."""
        return hash(value) % self._capacity
    def add(self, value):
        """Add a value to the set."""
        index = self._hash(value)
        bucket = self._buckets[index]
        # Check if the value already exists in the bucket
        for item in bucket:
            if item == value:
                return  # Value already exists, do nothing
        # Add the value to the bucket
        bucket.append(value)
        self._size += 1
        
    def remove(self, value):
        """Remove a value from the set."""
        index = self._hash(value)
        bucket = self._buckets[index]
        # Search for the value in the bucket
        for i, item in enumerate(bucket):
            if item == value:
                del bucket[i]  # Remove the value
                self._size -= 1
                return
        raise KeyError(f"Value {value} not found in HashSet")
    def contains(self, value):
        """Check if a value exists in the set."""
        index = self._hash(value)
        bucket = self._buckets[index]
        # Check if the value exists in the bucket
        for item in bucket:
            if item == value:
                return True
        return False
    
    def __iter__(self):
        """Allow iteration over the set."""
        for bucket in self._buckets:
            for item in bucket:
                yield item