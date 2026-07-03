from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    local_dir=r"E:\your\path\assets\mistral-7b"
)

print("TinyLlama downloaded!")