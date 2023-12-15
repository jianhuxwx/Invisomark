import requests
import json

def upload_to_ipfs(file_path):
    url = "https://api.nft.storage/upload"
    headers = {
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDljNzAyNDM4NjQ4MTg0NERCN2FkQzdEMDhjNzYyRjY1NEFEOWY5NGQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY5OTkzODUyNTQ5MSwibmFtZSI6IjEyMyJ9.6GRy_UZoDeA78QdRiADStFZLnuZkRof5qKlLmhMR0-4",
        "Content-Type": "application/octet-stream"
    }

    with open(file_path, 'rb') as f:
        response = requests.post(url, headers=headers, data=f)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return f"Error: {response.status_code}"

# 使用示例
#api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDljNzAyNDM4NjQ4MTg0NERCN2FkQzdEMDhjNzYyRjY1NEFEOWY5NGQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY5OTkzODUyNTQ5MSwibmFtZSI6IjEyMyJ9.6GRy_UZoDeA78QdRiADStFZLnuZkRof5qKlLmhMR0-4"  # 替换为您的API密钥
#file_path = "/Users/david/Desktop/Code/ATP/vulpinium_1.jpeg"       # 替换为您要上传的文件路径

#result = upload_to_ipfs(file_path)
#print(result)
