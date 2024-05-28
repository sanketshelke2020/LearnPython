### Variables 

```python
x = "hello"
x = 2
x = 2.4 ( If float and int calculation reurlt will be float )
x = true 
```
### Format String
```python
print(f"{x}")  
```
### List
```python
cars = ["bugati","lambo","honda"]
```
### Foreach
```python
foreach car in cars : 
    print(car)
```
### Range 
```python
for num in range(1,11,2) : 
    print(num)
```

###  findout
```python
list = [num**2 for num in range(1,11,2)] 
```

### Functions 
```python
def add_me(a,b) : 
    return a + b
```

### User input 
```python
name = input("What is your name ?")
```

### Import 
```python
import chess
from cars import bugati,farari
from students import girls as gf

chess.moves()
bugati()
gf.totalCount()

def add_me(a,b) : 
    return a + b
```


### Class
```python
class Student(Dog): 
    ``` Student Class ```

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getMarks(self): 
        return f"My name is {self.name}"
# Initiate Call 
myDog = Student('Moti',10)
```

### File Read
| *with* handle open and close no need to worrry

```python
filename = "hello.json"

with open(filename) as file_obj
    lines = file_obj.read()
    for line in lines: 
        pring(line)
```

### File Create/Write

```python
filename = "hello.json"

with open(filename,'w') as file_obj
    line = "f**k u"
    file_obj.wirte(line)
```


### Exception Handling 
```python
try
    def add_me(a,b) : 
        return a + b

except FileNotFound : 
    print("File Not Fount")

else 
```


### Json File Management 
```python
with open("my_info.json") as jObj
    numbers = json.load(jObj)

with open("my_write.json") as f
    json.dump(username , f )

```