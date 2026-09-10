import sys
import json
from client import FlatCombiningPQ

def main():
    pq = FlatCombiningPQ()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "insert":
            res = pq.submit_request("INSERT", params.get("val"))
        elif method == "extract_min":
            res = pq.submit_request("EXTRACT_MIN")
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
