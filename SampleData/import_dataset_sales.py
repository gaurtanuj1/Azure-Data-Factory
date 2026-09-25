import kagglehub

# Download latest version
path = kagglehub.dataset_download("anairamcosta/sales-csv")

print("Path to dataset files:", path)