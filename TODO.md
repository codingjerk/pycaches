# Things I want to implement

## Cache

□ Other cache policies (LFU, ARC, etc.)

□ (?) Count only not-expired items in `size` method

□ Cache hit/miss/size statistics

□ Allow cache to be persistent (use SQLite3 or whatever)

## Docs

□ Check English in docs and comments

□ Create RTD documentation

## Refactoring

□ Rename Map.from_collection to Map._hashable_items

□ Rename tests

## Performance

□ Speedup `Map` with dictionary based on string representation

□ Write more benchmarks for typical usage as a cache

□ Store items with expiration separately to speed up cleanup

## Testing

□ Use hypothesis to test what nothing can produce non-standart exceptions
