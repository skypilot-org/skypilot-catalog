# Hyperbolic Catalog

This directory contains the service catalog for Hyperbolic cloud provider.

## Files

- `vms.csv`: Contains the list of available VM instances with their specifications and pricing.

## Schema

The `vms.csv` file has the following columns:
- `InstanceType`: The name of the instance type
- `AcceleratorCount`: Number of accelerators (GPUs) in the instance
- `AcceleratorName`: Name of the accelerator (e.g., H100-SXM, A100-80GB-SXM)
- `MemoryGiB`: Amount of memory in GiB
- `StorageGiB`: Amount of storage in GiB
- `vCPUs`: Number of virtual CPUs
- `Price`: Price per hour in USD
- `GpuInfo`: JSON string containing GPU specifications including:
  - `clockSpeed`: GPU clock speed in MHz
  - `computePower`: GPU compute power
  - `interface`: GPU interface type
  - `model`: GPU model name
  - `ram`: GPU memory in MiB

## Update Frequency

The catalog is automatically updated every 7 hours via GitHub Actions. 