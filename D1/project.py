import json
import urllib.request

def lambda_handler(event, context):
    api_key = "c4c037ac0ebc48c5725d6cbf800da2ec"
    city = event.get('city', 'London')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
        
        weather = {
            "city": city,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        
        return {"statusCode": 200, "body": json.dumps(weather)}
    
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}