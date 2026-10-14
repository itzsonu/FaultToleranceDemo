
import requests

for n in range(1, 10):
    try:
        response = requests.get(
            "http://127.0.0.1:8000/library",
            timeout=10
        )
        data = response.json()

        print(
            f"Request: {n} | "
            f"HTTP: {response.status_code} | "
            f"Instance: {data.get('instance_port', 'none')}"
        )
        print("Tried:", data.get("attempted_backends", []))
        print("-" * 60)

    except requests.exceptions.RequestException as error:
        print("Could not contact the load balancer:", error)
        break
