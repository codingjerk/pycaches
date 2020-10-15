# Things I want to implement

## Cache

□ Other cache policies (LFU, ARC, etc.)

□ Remove expired items from cache before running cache replacement policy

□ `cache` decorator options (expiration_timedelta, policy, copy_keys)

□ Cache hit/miss/size statistics

□ Allow cache to be persistent (use SQLite3 or whatever)

## Docs

□ Check English in docs and comments

□ Create RTD documentation

## Refactoring

□ Rename Map.from_collection to Map._hashable_items

## Performance

□ Speedup `Map` with dictionary based on string representation

□ Write more benchmarks for typical usage as a cache

## Testing

□ Use hypothesis to test what nothing can produce non-standart exceptions
