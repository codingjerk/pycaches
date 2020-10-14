# Things I want to implement

## Map

□ `Map` to store cache independent if items are `Hashable`

□ Speedup `Map` with dictionary based on string representation

## Cache

□ `Cache` class to handle caches

□ `CachePolicy` interface to allow to use different cache policies

□ LRU/LFU/ARC cache policies

□ Cache item expiration

□ Cache hit/miss/size statistics

□ `cache` decorator options (expiration_timedelta, policy, copy_keys)

□ Allow cache to be persistent (use SQLite3 or whatever)

## Etc

□ Add usage to README

□ Write more benchmarks for typical usage as a cache

□ Add deploy tests (to make sure package is installable and importable)
