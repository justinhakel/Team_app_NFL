from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Load team data from CSV
teams = []
with open('team_data.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        teams.append(row)

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_team = None
    team_info = None
    if request.method == 'POST':
        selected_team = request.form.get('team')
        for team in teams:
            if team['team_name'] == selected_team:
                team_info = team
                break
    return render_template('index.html', teams=teams, team_info=team_info, selected_team=selected_team)

if __name__ == '__main__':
    app.run(debug=True)
