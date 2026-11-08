class AssociativeArray:
    def __init__(self, num_buckets: int) -> None:
        """Start with some empty buckets."""
        self.buckets: list[list[tuple[str | int, object]]] = [[] for _ in range(num_buckets)]
        self.num_buckets: int = num_buckets
        self.num: int = 0
        
    def quick_hash(self, val: str | int) -> int:
        """Get a number to use for the bucket."""
        if isinstance(val, str):
            key = hash(val)
        else: 
            key = val
        return key
    
    def set(self, key: str | int, value: object) -> None:
        """Add a key and value, or replace the old value."""
        self.rehash()
        if not self.contains(key):
            self.num +=1
            k1 = self.quick_hash(key)
            self.buckets[k1 % self.num_buckets].append((key, value))
        else: 
            self.remove(key)
            self.set(key, value)            
        
    
    def contains(self, key: str | int) -> bool:
        """Check if the key is here."""
        k1 = self.quick_hash(key)
        for k2, _ in self.buckets[k1 % self.num_buckets]:
            if key == k2: 
                return True
        return False
    
    def get(self, key: str | int) -> object | None:
        """Get the value for a key if it's here."""
        if self.contains(key):
            k1 = self.quick_hash(key)
            for k2, val in self.buckets[k1 % self.num_buckets]:
                if k2 == key:
                     return val
        return None
    
    def remove(self, key: str | int) -> bool:
        """Remove a key if it's here."""
        k1 = self.quick_hash(key)
        if self.contains(key):
            for idx, (k2, val) in enumerate(self.buckets[k1 % self.num_buckets]):
                    if k2 == key:
                        curr = self.buckets[k1 % self.num_buckets][-1]  # Move the last pair here.
                        self.buckets[k1 % self.num_buckets][-1] = (k2, val)
                        self.buckets[k1 % self.num_buckets][idx] = curr
                        self.buckets[k1 % self.num_buckets].pop()
                        self.num -=1
                        return True
        return False

    def size(self) -> int:
        """Count how many keys are stored."""
        return self.num

    def keyValuePairs(self) -> list[tuple[str | int, object]]:
        """Get all the key and value pairs."""
        pairs: list[tuple[str | int, object]] = []
        for values in self.buckets: 
            for pair in values: 
                pairs.append(pair)
        return pairs
    
    def load(self) -> float:
        """See how full the table is."""
        return self.num / self.num_buckets
    
    def rehash(self) -> None:
        """Make more buckets if the table is getting full."""
        if self.load() >= .8:
            kv = self.keyValuePairs()
            self.num_buckets = self.num_buckets*2
            self.buckets = [[] for _ in range(self.num_buckets)]
            self.num = 0
            for key, val in kv:  # Put the pairs back in the new buckets.
                self.set(key, val)
        
