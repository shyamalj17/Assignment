import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:

    def get_posts(self):
        return requests.get(f"{BASE_URL}/posts")

    def get_post(self, post_id):
        return requests.get(f"{BASE_URL}/posts/{post_id}")