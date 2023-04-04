from flask import Flask,request

app = Flask(__name__)

hackathons_list = {
    "GHW: API Week": {
        "start_date": "2023-04-03 12:00:00",
        "end_date": "2023-04-10 12:00:00",
        "location": "Everywhere, Online",
        "type": Digital Only"
    },
    "Bitcamp": {
        "start_date": "2023-04-07 12:00:00",
        "end_date": "2023-04-9 12:00:00",
        "location": "College Pk, Maryland",
        "type": In-person"
}

@app.route("/")
def hello_ghw():
    return "<p>Hello GHW API Coders!</p>"

@app.route('/getHackathons',methods=["GET"])
def get_hackathons():
    return hackathons_list

if __name__ == '__main__':
    app.run(debug=True)