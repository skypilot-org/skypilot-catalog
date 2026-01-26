The Lambda catalog assumes each instance type is offered in every region.

Even if this assumption is not true (and it is not), this assumption is okay to
make because the first region tried will point to regions that actually offer
the desired instance type, e.g. `Not enough capacity to fulfill launch request.
Regions with capacity available: us-west-3`.
