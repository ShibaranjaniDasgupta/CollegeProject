import os
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
from flask_mail import Message, Mail
import requests

load_dotenv()

app = Flask(__name__, static_folder='static')

userinfo = {'name': 'Subham Ghorui',
            'shortIntro': 'Aspiring Web Developer and Professional Programmer',
            'longIntro': 'Subham Ghorui is from jadavpur, Kolkata. He obtained his diploma at APC roy polytechnic. He currently works as a Software Developer. He is a driven individual who plans to one day work as a for his dream company: "IBM".',
            'work': [{'jobTitle': 'Software Engineer @ MLH', 'desc': "I created the backend of the LMS", "year": "2021",
                      'link': './static/img/logo.jpg'},
                     {'jobTitle': 'Software Engineer @ Meta', 'desc': "I created facebook mobile application",
                      "year": "2021-2022", 'link': './static/img/logo.jpg'}],
            'skills': ['./static/img/skillicons/c-.png', './static/img/skillicons/css-3.png',
                       './static/img/skillicons/html-5.png',
                       './static/img/skillicons/js.png', './static/img/skillicons/python.png'],
            'education': [{'type': 'Diploma of Computer Science', 'from': 'APC roy polytechnic', 'when': '2019-2022',
                           'desc': 'I studied stuff', 'link': './static/img/logo.jpg'}],
            'email': '123fakemail@gmail.com',
            'hobbies': [{'name': 'Basketball', 'caption': 'My Favorite Sport!',
                         'img': './static/img/hobbies_gallery/basketball.jpeg', 'active': 'active'},
                        {'name': 'Fishing', 'caption': 'My favorite way to relax!',
                         'img': './static/img/hobbies_gallery/fishing.jpg', 'active': ''},
                        {'name': 'Paddleboarding', 'caption': 'My favorite watersport!',
                         'img': './static/img/hobbies_gallery/paddleboarding.jpg', 'active': ''}],
            'project_rows': [[{'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#',
                               'link': 'github.com', 'img': './static/img/logo.jpg'},
                              {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#',
                               'link': 'github.com', 'img': './static/img/logo.jpg'},
                              {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#',
                               'link': 'github.com', 'img': './static/img/logo.jpg'}
                              ], [{'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#',
                                   'link': 'github.com', 'img': './static/img/logo.jpg'},
                                  {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#',
                                   'link': 'github.com', 'img': './static/img/logo.jpg'},
                                  {'name': 'Mario', 'tag': 'Loving Recreation of Mario', 'tools': 'Unity, C#',
                                   'link': 'github.com', 'img': './static/img/logo.jpg'}
                                  ]],
            'facebook': 'facebook.com',
            'github': 'github.com',
            'instagram': 'instagram.com',
            'linkedin': 'linkedin.com',
            'twitter': 'twitter.com'
            }


def openweathermap(city_name):
    api_key = str(os.getenv("APIKEY"))  # Openweathermap api key is easy to obtain
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + f'&APPID={api_key}'
    response = requests.get(complete_url)
    # requests json information from the API
    x = response.json()
    x = x['weather']
    x = x[0]
    return x['description']


@app.route('/')
def index():
    return render_template('index.html', title='Portfolio website', url=os.getenv('URL'), name=userinfo['name'],
                           shortIntro=userinfo['shortIntro'], longIntro=userinfo['longIntro'], work=userinfo['work'],
                           skills=userinfo['skills'],
                           education=userinfo['education'], email=userinfo['email'], facebook=userinfo['facebook'],
                           instagram=userinfo['instagram'],
                           github=userinfo['github'], linkedin=userinfo['linkedin'], twitter=userinfo['twitter'],
                           profilepic='./static/img/profile.jpg',
                           weather=openweathermap('Kolkata,INDIA'))


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html',
                           title="Hobbies",
                           url=os.getenv("URL"),
                           hobbies=userinfo["hobbies"],
                           email=userinfo['email'],
                           facebook=userinfo['facebook'],
                           instagram=userinfo['instagram'],
                           github=userinfo['github'],
                           linkedin=userinfo['linkedin'],
                           twitter=userinfo['twitter']
                           )


@app.route('/projects')
def projects():
    return render_template('projects.html',
                           title="Projects",
                           url=os.getenv("URL"),
                           project_rows=userinfo['project_rows'],
                           email=userinfo['email'],
                           facebook=userinfo['facebook'],
                           instagram=userinfo['instagram'],
                           github=userinfo['github'],
                           linkedin=userinfo['linkedin'],
                           twitter=userinfo['twitter']
                           )


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    print("test")
