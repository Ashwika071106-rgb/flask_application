from flask import Flask, jsonify, request

#the constructor of this class Flask that we imported takes the name of the current module,
#stored in __name__ as an argument and the variable app is now a Flask object.
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': "Buy Groceries",
        'description': "Milk, Cheese, Butter, Bread, Fruits",
        'done': False
    },
    {
        'id': 2,
        'title': "Study",
        'description': "English, Maths",
        'done': False
    }
]

#the route() function of this Flask class is a decorator, which will tell our
#web app which URL endpoint should call the associated function, hello_world in this case.
@app.route("/")
def hello_world():
    return "Hello World!"


#In this post request we'll create an add_task() function which will check for the data 
# #and if it doesn't find any then it'll show the 400 error with a message to provide data #
# and allow us to add data to the API and to the tasks array of objects.
@app.route("/add-data", methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    #create a skeleton/ structure of how the task will look like.
    #Our task will be an object/dictionary which will have multiple keys such as Id, title of the task, description of the
    #task and the status of the task.
    #We'll automate the id to increment by 1 every time a new task is added and
    #keep the initial status of the task as false.
    #Title and description will be provided by the user
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    #As the user provides the title and description we have to add the task to
    #the main list of tasks and then show the message - "task added successfully
    tasks.append(task)
    return jsonify({
        "status":"success",
        #converting the message to a json object and then showing it.
        #We are doing it because most of the time the data we get is in a Json format.
        "message": "Task added succesfully!" 
    })

#create a get method to see all the available tasks.
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    })

#to run our web application.
if (__name__ == "__main__"):
    #we are keeping debug=True so that the server will reload every time you make some change to the code
    app.run(debug=True)