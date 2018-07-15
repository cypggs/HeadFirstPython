import cgi
import athletemodel
import yate

athletes = athletemodel.get_from_store()
form_date = cgi.FileldStorage()
athlete_name = form_data['which_athlete'].value

print (yate.start_response())
print (yate.include_header("Coach Kelly's List of Athletes"))
print (yate.header("Thelete:"+ athlete_name + ",DOB:" + athletes[athlete_name].dob +"."))
print (yate.para("The top times for theis athlete are:"))
print (yate.u_list(athletes[athlete_name].top3))

print (yate.include_footer({"Home":"/index.html","Select another athlete":"generate_list.py"}))
