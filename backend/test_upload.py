from pathlib import Path

import requests

url = "http://127.0.0.1:8000/resumes/upload"

pdf_file = Path(__file__).parent / "sample.pdf"

with open(pdf_file, "rb") as file:
    files = [
        (
            "resumes",
            (
                pdf_file.name,
                file,
                "application/pdf",
            ),
        )
    ]

    response = requests.post(url, files=files)

print("Status:", response.status_code)
print(response.json())