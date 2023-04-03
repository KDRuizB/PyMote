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
    try:
        # get the user's csv file
        current_user = currentUser[0]
        user_csv_key = f"{current_user}.csv"

        with open(user_csv_key, 'r') as f:
            reader = csv.reader(f)
            data = [row for row in reader]

        if request.method == "POST":
            with open(user_csv_key, "a", newline="") as f:
                writer = csv.writer(f)
                # save new gadget in a csv file
                gadget = request.form['gadget']
                writer.writerow([gadget, "Off"])
         
                with open(user_csv_key, 'r') as f:
                    reader = csv.reader(f)
                    data = [row for row in reader]
            return render_template("gadgets.html", data=data)

        # data is the user profile csv content
        return render_template("gadgets.html", data=data)
    except IndexError:
        return render_template("login.html")

@app.route('/delet-gadget', methods=["GET", "POST"])
def delet():
    if request.metghod == "POST":
         # get the user's csv file
        current_user = currentUser[0]
        user_csv_key = f"{current_user}.csv"
    
        # get the gadget to delete from the form
        gadget_to_delete = request.form['gadget']

        # find the row index of the gadget to delete
        with open(user_csv_key, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if row[0] == gadget_to_delete:
                    row_index = i
                    break

        # Remove the row from the data
        with open(user_csv_key, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
        del data[row_index]

        # Write the updated data back to the file
        with open(user_csv_key, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            return render_template("gadgets.html")
    return render_template("delet-gadget.html")



# manage account settings
@app.route('/account', methods=["GET", "POST"])
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(debug=True)