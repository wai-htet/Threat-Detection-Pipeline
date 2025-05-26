import time
import requests

ELASTICSEARCH_URL = "http://elasticsearch:9200"

def query_failed_logins():
    query = {
        "query": {
            "match": {
                "message": "failed login"
            }
        }
    }
    try:
        response = requests.get(f"{ELASTICSEARCH_URL}/filebeat-*/_search", json=query)
        hits = response.json().get('hits', {}).get('hits', [])
        print(f"Found {len(hits)} failed login events")
        for hit in hits:
            print(hit['_source']['message'])
    except Exception as e:
        print(f"Error querying Elasticsearch: {e}")

def main():
    while True:
        query_failed_logins()
        time.sleep(60)  # Run every 60 seconds

if __name__ == "__main__":
    main()
