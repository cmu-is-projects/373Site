import csv
import bs4
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader

# User indicates the csv to be used in the upload
csv_file = input("Enter csv filename to use: ")

# User inputes whether to create img or modal
templateType = input("img or modal?: ")

# Find the right template to run
env = Environment(loader=FileSystemLoader(''))
template = env.get_template( templateType + "Template.html" )

# Local CSV to read data from
rdr = csv.DictReader( open(csv_file, "r" , encoding='utf-8') )

# If image specified
if templateType == "img":
	
	year = input("Enter semseter and year: ")
	year_string = year.replace(" ", "-")
	img_data = []

	# Open and instantiate file with beautiful soup 
	with open("../projects.html") as inf:
	    txt = inf.read()
	    soup = bs4.BeautifulSoup(txt, 'html.parser')
	
	for row in rdr:
		if row["Semester"] == year:
			img_content = template.render( row=row )
			img_data.append(BeautifulSoup(img_content, 'html.parser'))
	
	section = f"""<h2>{year}</h2>
    			<section class="row text-center placeholders" id="img-section">

    			</section>"""

	section_soup = BeautifulSoup(section, "html.parser")
	soup.find(class_="icon-images").insert(0, section_soup)

	# Save the projects file
	with open("../projects.html", "w") as outf:
		outf.write(str(soup))
	
	# Reopen and instantiate file with beautiful soup 
	with open("../projects.html") as inf:
	    txt = inf.read()
	    soup = bs4.BeautifulSoup(txt, 'html.parser')
	
	# Insert individual images
	for img in img_data:
		soup.find(class_="row text-center placeholders").insert(0, img)

	# Save the projects file again
	with open("../projects.html", "w") as outf:
		outf.write(str(soup))

# If modal specified
elif templateType == "modal":
	# Open and instantiate file with beautiful soup 
	with open("../projects.html") as inf:
	    txt = inf.read()
	    soup = bs4.BeautifulSoup(txt, 'html.parser')
	
	# Use template and csv data to render output
	template_content = template.render( data=rdr )
	template_soup = BeautifulSoup(template_content, 'html.parser')

	# Insert into document
	soup.find(class_="modals").insert(0,template_soup)


	# Save the projects file
	with open("../projects.html", "w") as outf:
		outf.write(str(soup))


