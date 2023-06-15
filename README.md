# SkyPilot Catalogs

**Latest catalog schema version**: v5

**Supported catalog schema versions**: v1, v2, v3, v4, v5


## Schema V5

### vms.csv
| Field | Type | Description |
| ----- | ---- | ----------- |
| `InstanceType` | string | The type of instance. |
| `vCPUs` | float | The number of virtual CPUs. |
| `MemoryGiB` | float | The amount of memory in GB. |
| `AcceleratorName` | string | The name of accelerators (GPU/TPU). |
| `AcceleratorCount` | float | The number of accelerators (GPU/TPU). |
| `GPUInfo` | string | The human readable inforomation of the GPU (not used in code). |
| `Region` | string | The region of the resource. |
| `AvailabilityZone` | string | The availability zone of the resource (can be empty if not supported in the cloud). |
| `Price` | float | The price of the resource. |
| `SpotPrice` | float | The spot price of the resource. |

### images.csv
| Field | Type | Description |
| ----- | ---- | ----------- |
| `Tag` | string | The SkyPilot tag of the image, starting with `skypilot:`. |
| `Region` | string | The region of the image (if the image is available across regions, this field should be empty). |
| `OS` | string | The OS of the image, e.g. ubuntu. |
| `OSVersion` | string | The OS version of the image, e.g. 2004. |
| `ImageId` | string | The ID of the image that is used to launch the instance in the cloud. |
| `CreationDate` | string | The creation date of the image (mainly for tracking purpose). |

