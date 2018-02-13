import csv
from jinja2 import Environment, FileSystemLoader

templateType = input("img or modal?: ")

env = Environment(loader=FileSystemLoader(''))
template = env.get_template( templateType + "Template.html" )

rdr = csv.DictReader( open("MobileProjects.csv", "r" , encoding='utf-8') )

if templateType == "img":
	year = input("Enter year: ")
	f = open("projects" + year + ".html", "w")

	for row in rdr:
		if row["Semester"] == "Spring " + year:
			f.write(template.render( row=row ))

	f.close()

elif templateType == "modal":
	f = open("modals.html", "w")
	f.write(template.render( data=rdr ))


print(template.render( data=rdr ))
