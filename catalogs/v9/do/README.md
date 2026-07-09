The DO catalog assumes each CPU instance type is offered in every region.

Even if this assumption is not true (and it is not), this assumption is okay to make because the first region tried will point to regions that actually offer the desired instance type, e.g. Not enough capacity to fulfill launch request. Regions with capacity available: i.e. `nyc2`.

GPU droplets `H100` and `H100:8` are currently early access and only available in `nyc2`. Quotas are not enabled by default and must be requested.
