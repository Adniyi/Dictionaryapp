from flask import Flask, render_template,request,flash
import requests as rq

app = Flask(__name__)
app.config["SECRET_KEY"] = "Jbhualvhviyasvjnhvak"

url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        try:
            word = request.form.get("word")
            response = rq.get(url.format(word)).json()

            words = []

            search_result = {
                "Name": response[0]["word"],
                # "Phonetic":response[0]["phonetic"],
                "Phonetics":response[0]["phonetics"][0]["audio"],
                "Meaning1": response[0]["meanings"][0]["definitions"][0]["definition"],
                "Meaning2": response[0]["meanings"][0]["definitions"][1]["definition"],
                "Meaning3": response[0]["meanings"][0]["definitions"][2]["definition"],
                "Meaning4": response[0]["meanings"][0]["definitions"][3]["definition"],
                "Meaning5": response[0]["meanings"][0]["definitions"][4]["definition"],
            }
            words.append(search_result)
            flash("Success",category="success")
            return render_template("index.html", words=words, search_result=search_result)
        except Exception as e:
            flash(f'A Error Occured: {e}', category="error")
    return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)