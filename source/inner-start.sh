# normally this would be in a dockerfile. 
# doing it this way beacause of unraid

apk update 
apk add --no-cache gcc musl-dev libffi-dev openssl-dev

pip install -r requirements.txt

python3 app.py
