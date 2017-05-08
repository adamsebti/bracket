#Python module that filters stage data for double-elimination Abios tournament bracket
def tournament(stages):
	playoffs = []
	data = {}
	for stage in stages:
		for substage in stage['substages']:
			if substage['type'] == 2:
				playoffs.append(substage)
				data[substage['title'][0:2].lower()] = {'ub': 
						{'semi':[
							{'team':[{'name':'--','score':0},{'name':'--','score':0}]},
							{'team':[{'name':'--','score':0},{'name':'--','score':0}]}
							]
						,
						'final':{'team':[{'name':'--','score':0},{'name':'--','score':0}]}
						},
						'lb': {'semi': {'team':[{'name':'--','score':0},{'name':'--','score':0}]},
						'final': {'team':[{'name':'--','score':0},{'name':'--','score':0}]}
						},
						'gf': {'team':[{'name':'--','score':0},{'name':'--','score':0}]}
						}

	for substage in playoffs:
		game = 0
		for series in substage['series']:
			stage = series['title']
			key = stage[0:2].lower()
			if len(series['rosters']) == 0:
				break
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
			if 'Grand final' in stage:
				data[key]['gf']['team'] = stage_data
			if 'UB Finals' in stage:
				data[key]['ub']['final']['team'] = stage_data
			if 'LB Final' in stage:
				data[key]['lb']['semi']['team'] = stage_data
			elif 'Finals' in stage:
				data[key]['gf']['team'] = stage_data
			if 'Cons.' in stage:
				data[key]['lb']['final']['team'] = stage_data
			if 'UB Semifinal' in stage or 'Semifinals' in stage:
				data[key]['ub']['semi'][game]['team'] = stage_data
				game = 1
			data[key]['title'] = substage['title']
	return data