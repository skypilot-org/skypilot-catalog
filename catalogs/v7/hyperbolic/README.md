# Hyperbolic Catalog

The Hyperbolic catalog provides GPU instance information for the Hyperbolic cloud provider.

## Schema

The `vms.csv` file contains the following columns:
- `InstanceType`: The name of the instance type
- `AcceleratorCount`: Number of accelerators (GPUs) in the instance
- `AcceleratorName`: Name of the accelerator (e.g., H100-SXM, A100-80GB-SXM)
- `MemoryGiB`: Amount of memory in GiB
- `StorageGiB`: Amount of storage in GiB
- `vCPUs`: Number of virtual CPUs
- `Price`: Price per hour in USD
- `GpuInfo`: JSON string containing GPU specifications (clockSpeed, computePower, interface, model, ram)

## Update Frequency

The catalog is automatically updated every 7 hours via GitHub Actions. 