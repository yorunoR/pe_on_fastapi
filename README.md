# pe_on_fastapi
Python code Executor on FastAPI

## Start
```
docker compose up
```
Open http://localhost:5000/docs

## Example

Submit the following python code:
```
def add_numbers(a, b):
    return a + b

def main(inputs):
    result = add_numbers(*inputs)
    print(result)
```


### Request body
```
{
  "code": "def add_numbers(a, b):\n    return a + b\n\ndef main(inputs):\n    result = add_numbers(*inputs)\n    print(result)\n",
  "inputs": "3, 4"
}
```

### Response body
```
{
  "result": "7\n"
}
```
