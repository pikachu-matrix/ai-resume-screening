import requests

url = "http://127.0.0.1:8000/resumes/upload"

files = [
    (
        "resumes",
        (
            "sample.pdf",
            open("sample.pdf", "rb"),
            "application/pdf",
        ),
    )
]

response = requests.post(url, files=files)

print("Status:", response.status_code)
print(response.json())