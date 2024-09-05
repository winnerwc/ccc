import requests
import json

# 定义 POST 请求的 URL
url = 'http://127.0.0.1:5000/projects/project_1'

# 插入测试数据
test_data = [
    {"baseline_name": "Test Baseline 1", "baseline_status": "Active", "owner": "Alice"},
    {"baseline_name": "Test Baseline 2", "baseline_status": "Inactive", "owner": "Bob"},
    {"baseline_name": "Test Baseline 3", "baseline_status": "Pending", "owner": "Charlie"},
    {"baseline_name": "Test Baseline 4", "baseline_status": "Active", "owner": "David"},
    {"baseline_name": "Test Baseline 5", "baseline_status": "Inactive", "owner": "Eve"},
    {"baseline_name": "Test Baseline 6", "baseline_status": "Pending", "owner": "Frank"},
    {"baseline_name": "Test Baseline 7", "baseline_status": "Active", "owner": "Grace"},
    {"baseline_name": "Test Baseline 8", "baseline_status": "Inactive", "owner": "Hannah"},
    {"baseline_name": "Test Baseline 9", "baseline_status": "Pending", "owner": "Ian"},
    {"baseline_name": "Test Baseline 10", "baseline_status": "Active", "owner": "Jack"}
]


# 将数据转换为 JSON 格式
headers = {'Content-Type': 'application/json'}

# 发送 POST 请求
response = requests.get(url, headers=headers)

# 输出响应的状态码和内容
print(f"Response Status Code: {response.status_code}")
print(f"Response Content: {response.json()}")