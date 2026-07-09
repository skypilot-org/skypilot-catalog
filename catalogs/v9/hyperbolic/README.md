# Hyperbolic Catalog

The Hyperbolic catalog provides GPU instance information for the Hyperbolic cloud provider.

## Schema

The `vms.csv` file contains the following columns:
- `InstanceType`: The name of the instance type
- `AcceleratorName`: Name of the accelerator (e.g., T4, H100-SXM)
- `AcceleratorCount`: Number of accelerators (GPUs) in the instance
- `vCPUs`: Number of virtual CPUs
- `MemoryGiB`: Amount of memory in GiB
- `StorageGiB`: Amount of storage in GiB
- `Price`: Price per hour in USD
- `Region`: Region where the instance is available (default if not specified)
- `GpuInfo`: JSON string containing GPU specifications:
  ```json
  {
    "Gpus": [{
      "Name": "Tesla-T4",
      "Manufacturer": "NVIDIA",
      "Count": 1,
      "MemoryInfo": {"SizeInMiB": 15360}
    }],
    "TotalGpuMemoryInMiB": 15360
  }
  ```
- `SpotPrice`: Spot instance price (if available)

## Update Frequency

The catalog is automatically updated every 7 hours via GitHub Actions. 