import store 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')
def get_list():
    return [1,2,3]


@app.get('/contact')
def get_contact():
    return {'name' : 'Platzi'}


@app.get('/contact-html', response_class=HTMLResponse)
def get_contact():
    return '''
    <html>
        <head>
            <title>Contact</title>
        </head>
        <body>
            <h1>This is the CONTACT PAGE I designed</h1>
            <p>My name is <strong>Fernando</strong></p>
        </body>
    </html>
'''


def run():
    store.get_categories()



if __name__ == '__main__':
    run()