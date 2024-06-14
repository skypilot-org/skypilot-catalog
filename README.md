# SkyPilot Catalogs

**Latest catalog schema version**: v5

**Supported catalog schema versions**: v1, v2, v3, v4, v5

## Automatic Catalog Fetching

Catalogs for AWS, GCP, and Lambda are automatically fetched & refreshed from the cloud provider, implemented as GitHub Actions. Other clouds can implement [catalog fetchers](https://github.com/skypilot-org/skypilot/tree/master/sky/clouds/service_catalog/data_fetchers) and a corresponding [Action](./.github/workflows/) to add auto-refresh.

Catalogs are updated **every 7 hours**.





## Schema V5

The catalogs for each cloud in [v5](v5) include the following files:
1. `vms.csv`: the catalog for the VMs, including the instance and the accelerators.
2. `images.csv`: the catalog for the images, which contains the mapping from the SkyPilot image tag to the image ID that can be used to find the image in the clouds. 

To supply your own custom pricing or custom regions/zones, you can update vms.csv according to the schema below.

### vms.csv

| Field | Type | Description |
| ----- | ---- | ----------- |
| `InstanceType` | string | The type of instance. |
| `vCPUs` | float | The number of virtual CPUs. |
| `MemoryGiB` | float | The amount of memory in GiB. |
| `AcceleratorName` | string | The name of accelerators (GPU/TPU). |
| `AcceleratorCount` | float | The number of accelerators (GPU/TPU). |
| `GPUInfo` | string | The human readable inforomation of the GPU (used for, e.g., parsing device memory). |
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


#### Update Images

For AWS, the images are automatically updated by the catalog fetcher. To update those images, please update the [fetch_aws.py](https://github.com/skypilot-org/skypilot/blob/master/sky/clouds/service_catalog/data_fetchers/fetch_aws.py) in SkyPilot repository.

For GCP, the images are updated manually. To check the latest images, please run the following command:
```bash
gcloud compute images list \
    --project deeplearning-platform-release \
    --no-standard-images --uri 
```
A common case for updating the images is to support a latest CUDA driver. To do so, we can change the image link for tag `skypilot:gpu-debian-11` in [images.csv](./catalogs/v5/gcp/images.csv) according to the command above. For tracking the history, we can add another tag `skypilot:cu<version>-debian-11` that also points to the latest image link.
```csv
skypilot:cuda121-debian-11,,debian,11,projects/deeplearning-platform-release/global/images/common-cu121-v20231105-debian-11-py310,20231105
skypilot:gpu-debian-11,,debian,11,projects/deeplearning-platform-release/global/images/common-cu121-v20231105-debian-11-py310,20231105
```
