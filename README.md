## Currency Converter

create virtual environment:
```console
python3.10 -m venv venv
``` 
virtual environment activate:
```console
. venv/bin/activate
```  
install libs:
```console
pip install -r requirements.txt
```
generate value API KEY at https://fixer.io/  
create .env file and add API_KEY variable with generated value
```console
touch .env
``` 
start app:
```console
uvicorn app.main:app --reload
```  

api docs:
> http://127.0.0.1:8000/redoc
