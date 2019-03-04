import rubrik_cdm

rubrik = rubrik_cdm.Connect()

# Monitor the progress of a On-Demand Snapshot
job_type = "CREATE_VMWARE_SNAPSHOT"
object_id = "fase1f32-3872-2982-a68c-6fe145982f48-vm-5008"
unique_key = "f7c393f3-383-4b44-920-8cde7a9ae2bd"  # On-Demand jobs create an additional key for uniqueness
instance_number = "0"
job_instance = job_type + "_" + object_id + "_" + unique_key + ":::" + instance_number
job_status_url = "https://172.21.8.52/api/v1/vmware/vm/request/" + job_instance

snapshot_status = rubrik.job_status(job_status_url)
