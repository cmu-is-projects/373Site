
1) The first step to adding new semester projects is to create a csv file with the headers:
Semester,Type,Company,Community_Partner,Project_Vision,Student1_Name,Student2_Name,Student3_Name,Student4_Name,Logo_file,pdf_file_name

and load this csv into the templating file (see existing .csv files for reference)

2) load all of the PDFs for the semester into the PDF folder - make sure that the names of the PDFs are properly spelled in the csv for each group

3) Load the images for the new logos into the images folder - make sure that the names of the images are properly spelled in the csv for each group

4)To add new semesters to this application itself, in a terminal cd into the templating folder:

	Once in, run the command $python auto_generate.py
		- Specify the csv to be used
		- chose img first
		- Input the semester and year as matched in the csv (ex Spring 2018)
	Run $python auto_generate.py a second time
		- Specify the csv to be used
		- chose modal

	Open the web page and you should see the new project added

