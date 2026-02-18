# Kubernetes Pricing Catalog

## pricing.csv

This file configures per-resource pricing for the Kubernetes cloud in SkyPilot.

### Default behavior

The default row sets all costs to $0.00 using a wildcard entry (empty `Region`, `Zone`, and `AcceleratorName` fields match everything). This preserves the pre-pricing behavior where Kubernetes resources have no associated cost.

### Custom pricing

To configure pricing for your cluster, add rows to `~/.sky/catalogs/v8/kubernetes/pricing.csv`. More specific rows take priority over wildcard rows. Lookup priority (highest to lowest):

1. Exact `Region` + exact `Zone`
2. Exact `Region` + any `Zone` (empty)
3. Any `Region` (empty) + exact `Zone`
4. Any `Region` (empty) + any `Zone` (empty) — wildcard

### Schema

| Field | Type | Description |
| ----- | ---- | ----------- |
| `Region` | string | Region identifier (empty = wildcard, matches all regions) |
| `Zone` | string | Zone identifier (empty = wildcard, matches all zones) |
| `PricePerVCPU` | float | Hourly price per vCPU |
| `PricePerMemoryGB` | float | Hourly price per GiB of memory |
| `AcceleratorName` | string | Accelerator name to match (empty = wildcard, matches all) |
| `PricePerAccelerator` | float | Hourly price per accelerator unit |
