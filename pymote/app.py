from flask import Flask, render_template, request, redirect, url_for
import csv
    
app = Flask(__name__)
currentUser = []

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
    
        with open("user.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == username and row[1] == password:
                    currentUser.append(username)
                    return render_template("start.html")
        
            # If we get to this point, no matching username/password was found
            return "No matching Password or Username. Maybe you forgot to make a Account."

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # get user name
        currentUser.append(username)

        # Checking if the user already exist
        with open("user.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == username:
                    return "User already exist"
        
            # If we get to this point, a new user will be created
            with open("user.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([username, password])
                # get the shorthand symbol for the user
                current_user = currentUser[0]
                user_csv_key = f"{current_user}.csv"
                # create userprofile
                with open(user_csv_key, "w", newline="") as file:
                    # Give the Profile headings for gadgets and status
                    header = ['gadget', 'status']
                    # make a write object to write data to file
                    writer = csv.writer(file)
                    # save the headings
                    writer.writerow(header)

        return redirect(url_for('login'))

    return render_template("register.html")

# only visual stuff
@app.route('/start', methods=["GET", "POST"])
def start():
    return render_template("start.html")

# delet and add gadgets / turn on or off
@app.route('/gadgets', methods=["GET", "POST"])
def gadgets():
    # get the user's csv file
    current_user = currentUser[0]
    user_csv_key = f"{current_user}.csv"
    if request.method == "POST":
        with open(user_csv_key, "a", newline="") as f:
            writer = csv.writer(f)
            # save new gadget in a csv file
            gadget = request.form['gadget']
            writer.writerow([gadget])
         
    with open(user_csv_key, 'r') as f:
        reader = csv.reader(f)
        item = [row[0] for row in reader]
        return render_template("gadgets.html", item=item)
    return render_template("gadgets.html")

# manage account settings
@app.route('/account', methods=["GET", "POST"])
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)