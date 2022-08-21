
import  requests

a = requests.get("http://localhost:5000/time")

print(a.text)
