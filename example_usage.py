from client import FlatCombiningPQ

def main():
    print("=== Testing Flat Combining Concurrent Priority Queue ===")
    pq = FlatCombiningPQ()
    pq.submit_request("INSERT", 50)
    pq.submit_request("INSERT", 20)
    pq.submit_request("INSERT", 30)

    min1 = pq.submit_request("EXTRACT_MIN")
    min2 = pq.submit_request("EXTRACT_MIN")
    print(f"Extracted minimums: {min1}, {min2}")

    assert min1 == 20
    assert min2 == 30
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
