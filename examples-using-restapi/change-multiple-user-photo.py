import requests

def update_photo(file_path, token):
    url = "https://www.clubhouseapi.com/api/update_photo"
    file_name = file_path.split("/")[-1]
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "CH-AppBuild": "2029",
        "CH-AppVersion": "23.02.07",
        "User-Agent": "clubhouse/2029 (iPhone; iOS 16.3; Scale/3.00)",
        "Connection": "close",
        "Authorization": f"Token {token}"
    }
    data = {
        "file": (file_name, open(file_path, "rb")),
    }
    response = requests.post(url, headers=headers, files=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error uploading file:", response.text)

def update_photos(tokens, file_paths):
    for token, file_path in zip(tokens, file_paths):
        res = update_photo(file_path, token)
        print(res)

if __name__ == "__main__":
    # TODO change to import from .env for security
    tokens = [
        "3b3ddf2203e79b21e1cb002bc42f5e4e28e95975",
        "da74178ea8fab9e613746d7c013a306d525cda37"
    ]
    # TODO make it dynamic
    file_paths = [
        # path to photos
        "./profile-pics/pic01.jpeg",
        "./profile-pics/pic02.jpeg"
    ]
    update_photos(tokens, file_paths)