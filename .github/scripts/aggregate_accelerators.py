#!/usr/bin/env python3
"""
Aggregate accelerators from SkyPilot catalog and export to CSV.

This script groups accelerators by case-insensitive names and merges their
cloud providers into a single entry.
"""

from sky import catalog
import pandas as pd
from collections import defaultdict


def main():
    # Group accelerators by lowercase name to handle case differences
    acc_groups = defaultdict(lambda: {'canonical_name': None, 'clouds': set()})

    for k, infos in catalog.list_accelerators().items():
        key_lower = k.lower()
        # Use the first occurrence as the canonical name
        if acc_groups[key_lower]['canonical_name'] is None:
            acc_groups[key_lower]['canonical_name'] = k
        # Collect all clouds for this accelerator (case-insensitive)
        acc_groups[key_lower]['clouds'].update(info.cloud for info in infos)

    # Build the final list with canonical names and sorted clouds
    acc_cloud = [
        [group['canonical_name'], sorted(list(group['clouds']))]
        for group in acc_groups.values()
    ]

    # Sort by accelerator name
    acc_cloud.sort(key=lambda x: x[0])

    pd.DataFrame({
        'AcceleratorName': [x[0] for x in acc_cloud],
        'Clouds': [x[1] for x in acc_cloud]
    }).to_csv('common/accelerators.csv', index=False)


if __name__ == '__main__':
    main()
