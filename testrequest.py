import requests
import json
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

# 测试用例数据
test_cases = [
    {
        "project_name": "Project_1",
        "data": {
            "job_name": "Task_5",
            "job_num": 1001,
            "job_status": "Completed",
            "fail_reason": "",
            "owner": "Alice",
        }
    },
    {
        "project_name": "Project_1",
        "data": {
            "job_name": "Task_7",
            "job_num": 1002,
            "job_status": "Failed",
            "fail_reason": "Resource limit exceeded",
            "owner": "Bob",
        }
    },
    {
        "project_name": "Project_2",
        "data": {
            "job_name": "Task_9",
            "job_num": 1003,
            "job_status": "Running",
            "fail_reason": "",
            "owner": "Charlie",
        }
    }
]

# 测试服务器地址
base_url = "http://localhost:5000"

# 执行测试用例
for test_case in test_cases:
    project_name = test_case["project_name"]
    data = test_case["data"]
    # 构造 URL
    url = f"{base_url}/projects/{project_name}"
    # 发送 POST 请求
    response = requests.post(url, json=data)
    # 检查响应状态码
    if response.status_code == 201:
        print(f"Test case passed for project '{project_name}': {response.json()}")
    else:
        print(f"Test case failed for project '{project_name}': {response.status_code}, {response.text}")
