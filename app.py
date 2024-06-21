from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/home")
def read_root():
    return {"Hello": "MCC Students!!!"}

@app.get("/about")
def about():
    return {"msg": "About Us"}

class LoginForm(BaseModel):
    username: str
    password: str

@app.get("/login", response_class=HTMLResponse)
def login_form():
    return """
    <form action="/login" method="post">
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
    """

@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # Dummy authentication logic for demonstration purposes
    if username == "admin" and password == "password":
        return {"msg": "Login successful"}
    else:
        return {"msg": "Invalid username or password"}