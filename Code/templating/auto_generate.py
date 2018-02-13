import csv
import bs4
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

# User inputes whether to create img or modal
templateType = input("img or modal?: ")

# Find the right template to run
env = Environment(loader=FileSystemLoader(''))
template = env.get_template( templateType + "Template.html" )

# Local CSV to read data from
rdr = csv.DictReader( open("MobileProjects.csv", "r" , encoding='utf-8') )

# If image specified
if templateType == "img":
	year = input("Enter year: ")
	f = open("projects" + year + ".html", "w")

	for row in rdr:
		if row["Semester"] == "Spring " + year:
			f.write(template.render( row=row ))

	f.close()

# If modal specified
elif templateType == "modal":
	# f = open("modals.html", "w")
	# f.write(template.render( data=rdr ))

	# Open and instantiate file with beautiful soup 
	with open("../projects2.html") as inf:
	    txt = inf.read()
	    soup = bs4.BeautifulSoup(txt, 'html.parser')
	
	# Use template and csv data to render output
	template_content = template.render( data=rdr )
	template_soup = BeautifulSoup(template_content, 'html.parser')
	old_modals = soup.find(class_="modals").findAll(class_="auto-generate")
	if len(old_modals) > 0:
		for modal in old_modals:
			modal.decompose()

	# Insert into document
	soup.find(class_="modals").insert(0,template_soup)


	# Save the projects file
	with open("../projects2.html", "w") as outf:
		outf.write(str(soup))