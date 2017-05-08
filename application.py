from flask import Flask, render_template
import json
import single,double

application = Flask(__name__)

#Load json data
with open('tournament_2070.json',encoding='utf-8') as json_data:
	data = json.load(json_data)

tournament_name = data['data']['tournament']['title']
game = data['data']['tournament']['game']['title']
stages = data['data']['tournament']['stages']

#DOUBLE ELIM BRACKETS
double_data = double.tournament(stages) #Filter data for double-elim bracket

@application.route('/stage/<substage>')
def double(substage):
    return render_template('double.html',  data=double_data[substage])


#SINGLE ELIM BRACKETS
new_data = single.tournament(stages) #Filter data for single-elim bracket
stage_names = single.stage_names(stages)

substage_list = []
substages = list(double_data.keys())
for substage in substages:
	substage_list.append([substage, double_data[substage]['title']])

#Run server
@application.route('/')
def single():
	return render_template('single.html', data=new_data, stages = stage_names, substages = substage_list)



if __name__ == '__main__':
	application.run()