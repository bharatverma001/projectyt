from flask import Flask,jsonify,request
app = Flask(__name__)
task = [
    {
        "id":1,
        "title":u"buy grociries",
        "description":u"milk,pizza,cheesse,fruit",
        "done":False
    },
     {
        "id":2,
        "title":u"learn python",
        "description":u"looking for good python tutorial",
        "done":False
    },
    
]
@app.route("/")
def hello_world():
    return "hello World"
@app.route("/add-data",method=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        },400)

    task = {
        "id":task[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),

        "done":False
    }
    tasks.append(task)
    return jsonify ({
            "status":"success",
            "message":"task added successfull" 
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks  
    })
if(__name__=="__main__"):
    app.run(debug=True)
