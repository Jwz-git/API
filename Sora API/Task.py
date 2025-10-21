import http.client
import json
import time

def Create_Task(prompt, url):
    """
    创建一个任务
    :param prompt: 任务要求
    :param url: 图片地址
    :return: 任务ID
    """

    conn = http.client.HTTPSConnection("duomiapi.com")
    payload = json.dumps(
        {
            "model": "sora-2",
            # 要求
            "prompt": prompt,
            "aspect_ratio": "16:9",
            "duration": 10,
            "image_urls": [
                # 图片地址
                url
            ],
        }
    )
    headers = {
        "Authorization": "o9vfVkEkKfcuJhjdGXJwlfdvO1",
        "Content-Type": "application/json",
    }
    conn.request("POST", "/v1/videos/generations", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))

    task_json = json.loads(data)
    time.sleep(5)
    return task_json["id"]


# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------

def Get_Status(task_id):
    """
    获取任务状态
    :param task_id: 任务ID
    :return: 任务状态
    """
    
    conn = http.client.HTTPSConnection("duomiapi.com")
    headers = {
        "Authorization": "o9vfVkEkKfcuJhjdGXJwlfdvO1",
        "Content-Type": "application/json",
    }

    i = 0

    while True:
        conn.request("GET", f"/v1/videos/tasks/{task_id}", headers=headers)
        res = conn.getresponse()
        task_data = res.read().decode("utf-8")
        conn.close()

        task_json = json.loads(task_data)
        print("任务状态：", task_json)
        if task_json["state"] == "running" or task_json["state"] == "pending":
            # print(i)
            # i += 1
            time.sleep(5)
            continue
        elif task_json["state"] == "succeeded":
            # print(i, ":视频URL：", task_json["data"]["videos"][0]["url"])
            # i += 1
            return f'视频URL: {task_json["data"]["videos"][0]["url"]}'
        else:
            # print(i, ":任务失败", "失败原因：", task_json["message"])
            # i += 1
            return f"任务失败，失败原因：{task_json['message']}"
