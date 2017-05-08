#Python module that filters stage data for single-elimination Abios tournament bracket
def tournament(stages):
	playoffs = []
	for stage in stages:
		for substage in stage['substages']:
			if substage['type'] == 1:
				playoffs = substage
	data = {}
	stages = []
	for series in playoffs['series']:
		stage = series['title']
		if stage not in stages:
			stages.append(stage)
		home_team = series['rosters'][0]['teams'][0]
		away_team = series['rosters'][1]['teams'][0]
		home_url = series['rosters'][0]['teams'][0]['images']['default']
		away_url = series['rosters'][1]['teams'][0]['images']['default']
		home_team_id = str(series['rosters'][0]['id'])
		away_team_id = str(series['rosters'][1]['id'])
		stage_data = [
			{
				'name':home_team['name'],
				'id': home_team_id,
				'score': series['scores'][home_team_id],
				'url':home_url
			},
			{
				'name':away_team['name'],
				'id': away_team_id,
				'score': series['scores'][away_team_id],
				'url':away_url
			}]
		if stage in data:
			data[stage].append(stage_data)
		else:
			data[stage] = [stage_data]

	stages = stages[::-1]
	stages.append("Winner")

	new_data = []
	for key in data:
		new_data.append(data[key])
	new_data = sorted(new_data, key=lambda x: len(x), reverse=True)

	#Add the winner to the bracket
	if new_data[-1][0][0]['score'] > new_data[-1][0][1]['score']:
		new_data.append([[new_data[-1][0][0]]])
	else:
		new_data.append([[new_data[-1][0][1]]])
	return new_data

def stage_names(stages):
	for stage in stages:
		for substage in stage['substages']:
			if substage['title'] == 'Playoffs':
				playoffs = substage
	stages = []
	for series in playoffs['series']:
		stage = series['title']
		if stage not in stages:
			stages.append(stage)
	stages = stages[::-1]
	stages.append("Winner")
	return stages






