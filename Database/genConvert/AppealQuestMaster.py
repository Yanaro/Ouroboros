def AppealQuestMaster(json):
    this={}#AppealQuestMasterjson)
    #returnfalse
    if 'fields' in json:
        this['appeal_id'] = json['fields'].appeal_id
    if 'fields' in json:
        this['start_at'] = TimeManager.FromDateTime)
    if 'fields' in json:
        this['end_at'] = TimeManager.FromDateTime)
    #returntrue
return this
