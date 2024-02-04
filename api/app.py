from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/generate_response", methods=["POST"])
def generate_response():
    data = request.get_json()
    id = data.get("id")

    # Your existing code for generating the response
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
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    seekerMemberId = data["data"]["seekerMemberId"]

    # Modify the URL and headers for the second request
    url = f"https://www.urbanpro.com/virtualNumberAllocation/getVirtualNumberToCall?callMember={seekerMemberId}&enquiryId={id}"

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
        
        
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    actualNumber = data.get("actualNumber")

    return jsonify({"actualNumber": actualNumber})
