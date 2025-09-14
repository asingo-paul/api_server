from fastapi import FastAPI

app = FastAPI(title = "api server")


@app.get('/home/{name}')
def greetings(name):

    return {
        "greetings":"hello, " + name
    }

@app.get("/about/hello/{name1}")
def about(name1):

    return {

        "name1" : name1
    }