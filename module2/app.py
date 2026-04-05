from flask import Flask, render_template
from report import generate_report
from notification import send_notification
from analytics import analytics_data
from api_integration import get_external_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    result = generate_report()
    return render_template("result.html", title="Report Generated", data=result)


@app.route("/notify")
def notify():
    result = send_notification("New system update")
    return render_template("result.html", title="Notification Status", data=result)


@app.route("/analytics")
def analytics():
    data = analytics_data()
    return render_template("result.html", title="Analytics Data", data=data)


@app.route("/external-api")
def api():
    data = get_external_data()
    return render_template("result.html", title="External API Data", data=data)


if __name__ == "__main__":
    app.run(port=5001, debug=True)