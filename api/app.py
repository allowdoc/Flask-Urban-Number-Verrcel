from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from functools import lru_cache
import concurrent.futures

app = Flask(__name__)
CORS(app)

# Decorate the function with caching
@lru_cache(maxsize=128)
def get_top_header_detail(id):
    url = f"https://www.urbanpro.com/dashboardApi/topHeaderDetail?id={id}"
    headers = {
        "Host": "www.urbanpro.com",
        "Connection": "keep-alive",
        "requestType": "xhr",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
        "DNT": "1",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "cache-control": "no-cache",
        "sec-ch-ua-platform": "\"Windows\"",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.urbanpro.com/register/needDetailAndMessage?id=5519213084",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Cookie": "JSESSIONID=C46472D31938E5CC10319B6217CEDCA4; vis=6431c5b4-791e-42dc-8a3a-396910d140c4; referrer=direct%7Cthinkvidya%7C%2FvirtualNumberAllocation%2FgetVirtualNumberToCall%7C%7C%7C; _gcl_au=1.1.847758473.1704575552; _cc=accept; grails_remember_me=eW9nYWF0ZG9vcnN0ZXBAZ21haWwuY29tOjE3MzU2Nzk2MTkwNjQ6NGU3Yjg1M2MxZTMyMzhjZDU2OTYzOWJlN2Y3MjRkYzA; city=Delhi; X-Auth-Token=eyJhbGciOiJIUzI1NiJ9.eyJwcmluY2lwYWwiOiJINHNJQUFBQUFBQUFBSlZTdjJcL1RRQmo5SEZJVktSSzBTQ0FZeWtLUkdKQ1RPR2tBWllGVUFRbTVMV3JJVWlUUXhUNmJhODkzNXU3Y0pndktCRU9ISXFBU2duK2hJeXRcL0FWMzRBeEFNckoxWitjNzk0Y0JTY2RQcHUrZjMzdmVlOXc1Z1NpdG94SW93cnQyVVp6RVRyazRWRTdHbVFhYVlHYm1acGlxa0prYzh5SUY5bk1EaGNVcmcrRkJpb1lFTFwvanJaSkZWT1JGeGRHYXpUd0xTSENqeXA0aVBHU0pHRWJrbTE0WjV3QjFMUnZ3UUthdWRqQ2FiWFlKWUVnY3lFV1phaU8weVpvdUVhekJRelh3WWJkblF4d0JjcURDTmNUMEtucVNBRFRrTWZLaVF6enlXcU1xb05uRDgwbXhuR3F6MXEyajZjVFluVzZPNmZUWHJHV3JmdjFxYkFEVjdBU3lnUFV3Y1BabmZkUWwzTDR5NUt6bkZySm9XZTc0dEVoaXhpVmh6NXgzTnZ2KzE4R3ZkTEFKakp6ZE9cL0tlWlhPakQrK3ZUMzFUeG9KekJ3YWNKNkFXc1BVM1F6V3pBXC9WdFFxZlwvXC93Nk4zdXdlc25aMURaSXU3XC9meFwvejk0NlNHeTNLSkNXS0dEblJFZEp1bGUwZHlUdW5reCszTUhKN0xFazV4VDlLR0JxZVNCVEV1RzVaU1g2Y3Q0SEs2b3JmZmJiVVhlcDBWNGNHYmtTdE96WFNvRjR6R2l6VXZWdE5XbXMwNjFHdHRWQ1BCaTB2Q0JxM3ZhaEpXNTZCeXlNWkUySkNLWlUyTkwwYko3Z2Mra25RODdrOE10dTE2MHRzZXZ2WG1cLzJkYXo5UVwveUZNYlJLZVVXeHNwZ0F0WjhtQXFsZDd1M09WOXorMzhcLzF6eTVcLzN2XC93QnRaRnlnVThEQUFBPSIsInN1YiI6InlvZ2FhdGRvb3JzdGVwQGdtYWlsLmNvbSIsInJvbGVzIjpbIlJPTEVfTUVNQkVSIl0sImV4cCI6MjAxNTYxNTYxOSwiaWF0IjoxNzA0NTc1NjE5fQ.T0y6dD8VFp7ioW6zP3ru8lTda7VJyPTuU_C45ZJrRgc; _gid=GA1.2.2001739854.1704575650; _ga=GA1.1.1119046135.1704575552; AWSALB=LZ+Ss7xBrSp5iKW5zWsxG00wz55J//Ngj1FKxfspC9YvXnA5+dpvJ3fedTRaAheygeMbetdp61YUpYFbdl42k7xPSXqvuqyFSWhZt07LrgjzK90WSwYhqSol3shm; AWSALBCORS=LZ+Ss7xBrSp5iKW5zWsxG00wz55J//Ngj1FKxfspC9YvXnA5+dpvJ3fedTRaAheygeMbetdp61YUpYFbdl42k7xPSXqvuqyFSWhZt07LrgjzK90WSwYhqSol3shm; _ga_PZ985ML4Z1=GS1.1.1704575552.1.1.1704576795.60.0.0"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Decorate the function with caching
@lru_cache(maxsize=128)
def get_virtual_number(id, seeker_member_id):
    url = f"https://www.urbanpro.com/virtualNumberAllocation/getVirtualNumberToCall?callMember={seeker_member_id}&enquiryId={id}"
    headers = {
        "Host": "www.urbanpro.com",
        "Connection": "keep-alive",
        "requestType": "xhr",
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Cookie": "JSESSIONID=119675D06A371C74C173A5F3651D9072; vis=8984ef76-2bd1-4abb-86ac-e7862ceb4ea5; referrer=seo%7Cwww.google.com%7C%7C%2Flogin%7C%7C; _gcl_au=1.1.2010139210.1720893302; _cc=accept; _ga=GA1.1.1942893954.1720893303; _fbp=fb.1.1720893304183.768707582735537715; grails_remember_me=a3VzdW1rdW1hcmlwYW5kZXkxMkBnbWFpbC5jb206MTc1MTk5NzM2ODQxODoxNDYwNTQyYjdjMmVmYjYxYmNhYjc1ZDc0NjJlMGFjZQ; X-Auth-Token=eyJhbGciOiJIUzI1NiJ9.eyJwcmluY2lwYWwiOiJINHNJQUFBQUFBQUFBSlZTdTI0VFFSUzlObzZDWkFrU0pKQW9URU9RS05EYVhqOEF1UUZIQmdsdEVoVGpKa2lnOGU3c012SHN6REtQeEc2UUt5aFNCQUdSRVB4Q1N2NENHajRBUVVHYmhvYVd1NXZIR3BxSXFVWjN6cDV6N2ptN2Z3QnpXa0VqVW9SeDdTVGNSa3c0T2xGTVJKcjZWakV6Y2F5bUtxQW1ROXpQZ0FPY3dPRXBGS0hnUVpFRkJpNTRtMlNMVkRrUlVYVnR1RWw5MHhrcmNLV0tqaGhEUldLNkxkWElPZUgycGFKXC9DZVRVaFE5Rm1OK0FSZUw3MGdxektrVnZuREJGZ3cxWXlHZWU5RWZwNktLUEwxUVlScmllaGM1VFFZYWNCaDZVaVRYUEpLb3lxZzJjUHpSckRlUFZQalVkRDg0bVJHdDA5ODhtZlpOYVQ5OVRtd0kzZUE0dm9EUk9Dbmd3dTJzcDFFbDVuR1hKT1c3TnBOQkxBeEhMZ0lVc0ZVZithZVhOMTkyUDAwRVJBRE81Y2ZvMytmeHlGNmFmblwveStrZ1ZkOEExY21yR2V3enJqQk4wczVzeVBGRTJWdjcxXC8rSGJ2NE5Yak02aWNJdTc5Zng5TGQ0K1NteXpMT0NHS0dEblRFZEp1bDlJN2tuZFBKejl1WWVMMFdaeHdpbitVTURRNGtjaUpjZDJTa3Z3NGJ3UGw5VFd2OTNTbHQ5THRyWThOWEFcL2J0MnVrUWQxbU9HelYzWnROV21zMDYyR3QzYXFIdzdicis0MWJidGlrYmRkQVpXUzFqVWMySm9vbFJBUjBVbmZ2UkRGdWlLWmlOSDR1eXkwdDNQRWsxcjN6OFwvV1gzYXZmMGNRRG1Oc2kzRktzYlNFSHJkcDRTTlhMXC9iMUsrZDJQblN5RXpQZW4xcThcL0g3Ylp1bFFEQUFBPSIsInN1YiI6Imt1c3Vta3VtYXJpcGFuZGV5MTJAZ21haWwuY29tIiwicm9sZXMiOlsiUk9MRV9NRU1CRVIiXSwiZXhwIjoyMDMxOTMzMzY4LCJpYXQiOjE3MjA4OTMzNjh9.LtZTwOSeOUawoJ0Ol_7yYu3arkcRUbHrKHghmqWgB4g; city=Delhi; _ga_PZ985ML4Z1=GS1.1.1720893303.1.1.1720893396.33.0.0"
        
    }
    response = requests.get(url, headers=headers)
    return response.json()

@app.route("/generate_response", methods=["POST"])
def generate_response():
    try:
        data = request.get_json()
        id = data.get("id")

        # Use threading for parallel execution
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Execute the first API call asynchronously
            top_header_future = executor.submit(get_top_header_detail, id)

        # Retrieve the result of the first API call
        top_header_data = top_header_future.result()

        seeker_member_id = top_header_data["data"]["seekerMemberId"]

        # Execute the second API call asynchronously
        with concurrent.futures.ThreadPoolExecutor() as executor:
            virtual_number_future = executor.submit(get_virtual_number, id, seeker_member_id)

        # Retrieve the result of the second API call
        virtual_number_data = virtual_number_future.result()

        actual_number = virtual_number_data.get("actualNumber")

        return jsonify({"actualNumber": actual_number})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

