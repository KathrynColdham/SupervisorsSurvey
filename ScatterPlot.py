import tkinter
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import os


#input arguments
parser = argparse.ArgumentParser()

parser.add_argument("-a", "--first", type=str, help="title of first column")
parser.add_argument("-b", "--second", type=str, help="name of column to compare to")

args = parser.parse_args()

Col1 = args.first
Col2 = args.second


QuestionArray = ['1. For how many years have you been a member of the CMS collaboration?', 
		 '2. In which age range do you fall under?',
		 '3. What gender do you identify as?', 				           
		 '4. What is your country of residence?', 
	         '5. In which country is your home institute?',			           
		 '6. Do you have children?',
		 '7. Are you a carer?', 						   				      
		 '8. For how long have you had experience in supervising PhD students, either in or outside of CMS?',
		 '9. How many PhD students have you supervised during your career?',       				      
		 '10. How many PhD students do you currently supervise?',
		 '11. Of the PhD students you have supervised, what percentage have worked in a different field to you?',     
		 '12. If you have supervised PhD students who work in a different field to you, how have you found this in comparison to supervising a PhD student in the same field as you?',
		 '13. If you have supervised PhD students who work in a different field to you, is there anything you wish to add about how you have found this?',
		 '14. Of the PhD students you have supervised, what percentage have worked on an experiment other than CMS (e.g. experiments at DESY, FNAL, etc...)?',
		 '15. If you have supervised PhD students on other experiments, how have you found this in comparison to supervising a CMS PhD student?',
		 '16. If you have supervised PhD students that work on experiments other than CMS, is there anything you would like to add about how have you found this?',
		 '17. How often do/did you have one-to-one meetings with your PhD students?',
	         '18. For how long do/did these one-to-one meetings normally last?',
		 '19. How often do/did you meet with your PhD students in a group setting?',
		 '20. For how long do/did these group meetings normally last?',
		 '21. Which of the following methods of communication do/did you use with your students?',
		 '22.  Do/did you as a PhD supervisor provide other individuals - for example postdocs - for PhD students to talk to and get help from?',
		 '23. Considering all support offered in combination, including from yourself, co-supervisors, and from others like postdocs, how frequent is the support your students receive?',
		 '24. Which of the following best describes how you interact(ed) and the frequency of your interactions with your PhD students?',
		 '25. How similar is/was this to the interactions you had with your supervisor when you were a PhD student?',
		 '26. Is the way in which you interact(ed) and the frequency of your interactions with your PhD students the result of a conscious decision? Why or why not?',
		 '27. Which of the following best describes your job/best described your job whilst you supervised PhD students? If your job is not listed, please add it in the "other" field.',
		 '28. Do/did you hold other professional roles in addition to supervising PhD students? Please indicate these using the below options. If you hold/held any responsibilities not listed, please list them in "other".',
		 '29. How happy are/were you with being a supervisor in general?',
	         '30. How satisfied are/were you with the level of support offered to supervisors within your home institution?',
		 '31. Please highlight the sources of support within your home institution that you benefit(ted) from.',		
		 '32. How satisfied are you/were with the level of support offered to supervisors within CMS? ',
		 '33. Please highlight the sources of support within CMS that you benefit(ted) from.',
		 '34. Please highlight any sources of support for supervisors that you feel are missing within CMS.',
		 '35. Would you (have) benefit(ted) from a CMS training programme for PhD supervisors?',
	         '36. If a CMS training programme for PhD supervisors were to be created, which of the following would you like for it to include? Multiple choices can be selected for this answer. If you would like to suggest an option not included, please provide it in the "other" field.',
		 '37. Which of the following do you feel would be helpful for supervisors to have access to? If you would like to contribute a suggestion, please add this by selecting the "other" field.',
		 '38. This question is completely optional for you to answer, should you feel comfortable enough to do so. Please rate how has your mental health been since the COVID-19 pandemic began?',
		 '39. This question is completely optional for you to answer, should you feel comfortable enough to do so. Please rate the overall impact that your supervisory responsibilities had/have on your mental health?',
		 '40. This question is completely optional for you to answer, should you feel comfortable enough to do so.  On a typical day, how manageable is/was your workload while being a supervisor?']




GraphTitleArray = ['collaboration membership length',       
		   'age',                                            
		   'gender',                
		   'country of residence',                  
		   'country of home institute',                      
		   'parenthood', 			     
                   'carer',  
		   'supervisory experience',    
		   'number of PhD students supervised during career', 
		   'number of PhD students currently supervised',
		   '%age of students in a different field', 
		   ' vs experience of supervising in different field',
		   ' ',
		   '%age of students on another experiment',
		   ' vs experience of supervising on another experiment',
		   ' ',
		   'frequency of one-to-one meetings',
		   'length of one-to-one meetings',
		   'frequency of group meetings',
                   'length of group meetings', 
		   'communication methods',
		   'other individuals provided',
		   'frequency of student support',
		   'style and frequency of interaction',
		   'interactions as a PhD student',
		   ' ',
		   'job title',
		   'other roles',
		   'supervisor satisfaction',
		   'satisfaction (level of support from home institute)',
		   ' ',
		   'satisfaction (level of support from CMS)',
		   ' ',
		   ' ',
		   'benefitted from training?',
		   ' ',
		   ' ',
		   'mental health since pandemic began',
		   'mental health since becoming a supervisor',
		   'managability of workload']

PdfTitleArray = ['CMSMembershipLength', 
		 'Age', 
		 'Gender', 
		 'CountryOfResidence', 
		 'CountryOfHomeInstitute',
		 'Parenthood',
                 'Carer',
                 'SupervisoryExperience',
                 'NumberOfPhDStudentsSupervisedDuringCareer',
                 'NumberOfPhDStudentsCurrentlySupervised',
                 'PercentageOfStudentsInADifferentField',
                 'ExperienceOfSupervisingInDifferentField',
                 ' ',
                 'PercentageOfStudentsOnAnotherExperiment',
                 'ExperienceOSupervisingOnAnotherExperiment',
		 ' ',
                 'FrequencyOfOneToOneMeetings',
                 'LengthOfOneToOneMeetings',
                 'FrequencyOfGroupMeetings',
                 'LengthOfGroupMeetings',
                 'CommunicationMethods',
                 'OtherIndividualsProvided',
                 'FrequencyOfStudentSupport',
                 'StyleAndFrequencyOfInteraction',
                 'InteractionsAsAPhDStudent',
                 ' ',
                 'JobTitle',
		 'OtherRoles',
                 'SupervisorSatisfaction',
                 'Satisfaction_SupportFromHomeInstitute',
                 ' ',
                 'Satisfaction_SupportFromCMS',
                 ' ',
                 ' ',
                 'BenefittedFromTraining?',
                 ' ',
                 ' ',
                 'MentalHealthSincePandemicBegan',
                 'MentalHealthSinceBecomingASupervisor',
                 'ManagabilityOfWorkload']

AxisLabelArray = ['CMS membership length', 
		  'Age', 
		  'Gender', 
		  'Country', 
		  'Country',
		  'Has children?',
                  'Is a carer?',
                  'Supervisory experience (years)',
                  'Number of students',
		  'Number of students',
                  'Percentage',
                  'Experience Of Supervising In A Different Field',
                  ' ',
		  'Percentage',
                  'Experience Of Supervising On Another Experiment',
		  ' ',
                  'Frequency',
                  'Length',
                  'Frequency',
                  'Length',
                  'Communication Methods',
                  'Other Individuals Provided?',
                  'Frequency',
                  'Style And Frequency Of Interaction',
                  'Interactions As A PhD Student',
                  ' ',
                  'Job',
		  'Other responsibilities',
                  'Satisfaction score',
		  'Satisfaction score',
                  ' ',
                  'Satisfaction score',  
		  ' ',
                  ' ',
                  'Benefitted From Training?',
                  ' ',
                  ' ',
                  'Rating',
		  'Rating',
		  'Rating']


print('len(QuestionArray) = ', len(QuestionArray))
print('len(GraphTitleArray) = ', len(GraphTitleArray))
print('len(PdfTitleArray) = ', len(PdfTitleArray))
print('len(AxisLabelArray) = ', len(AxisLabelArray))

counter = 1

#Setting the titles and labels for depending on the first column
for i in QuestionArray:
	if Col1 == i:

		FirstColumnNumber = counter
		GraphTitleStart = GraphTitleArray[counter-1]
		PdfTitleStart = PdfTitleArray[counter-1]
		XAxisLabel = AxisLabelArray[counter-1]

		counter = 1

		break

	elif Col1 != i and counter == len(QuestionArray):

		print('Error: Check the name of the first column')
		quit() 

	counter+=1


#Setting the titles and labels for depending on the first column
for i in QuestionArray:
	if Col2 == i:
	
		SecondColumnNumber = counter
		GraphTitleEnd = GraphTitleArray[counter-1]
		PdfTitleEnd = PdfTitleArray[counter-1]
		YAxisLabel = AxisLabelArray[counter-1]

		break

	elif Col2 != i and counter == len(QuestionArray):

		print('Error: Check the name of the second column')
		quit()

	counter+=1



def reader(filename):

	# Read the data file
	df_original = pd.read_csv(filename)

	# Sort by the two relevant columns
	df = df_original.sort_values(by=[Col1, Col2])

	# Skim the dataframe
	df = df[[Col1, Col2]]

	# Count and remove duplicates
	df = df.groupby(df.columns.tolist()).size().reset_index().rename(columns={0:"Counts"})

	# Form an numpy array
	np_arr = df.values

	# Split into three
	x = np_arr[:, 0]
	y = np_arr[:, 1]
	counts = np_arr[:, 2]

	index = 0
	
	counts_new = []
	
	#Converting to percentages
	for i in x:
		Total = df_original[df_original[Col1] == i].shape[0] #to get the total number of respondents for each category (e.g. each age category)
		new_value = (counts[index]/Total) * 100
		counts_new.append(new_value)
		index += 1

	# Protection for nans
	where_are_NaNs = pd.isna(x)
	x[where_are_NaNs] = "nan"

	# Make the plot
	sc = plt.scatter(x, y, c=counts_new, cmap=matplotlib.cm.viridis, marker="s")	

	# Cosmetics
	plt.title(GraphTitleStart + ' vs ' + GraphTitleEnd)
	plt.xlabel(XAxisLabel)
	plt.ylabel(YAxisLabel)
	plt.xticks(rotation = 90)


	# Colour bar
	cbar= plt.colorbar(sc)
	cbar.set_label("Responses (%)", labelpad=+5)

	# Save the plot
	if not os.path.exists('Results_ScatterPlots'):
		os.mkdir('Results_ScatterPlots')

	pdf_name = 'ScatterPlots_' + PdfTitleStart + '_' + PdfTitleEnd + '.pdf'
		
	os.chdir('Results_ScatterPlots')
	plt.savefig(pdf_name, bbox_inches='tight')
	
	print('The file ', pdf_name, ' has been saved.')	


if __name__ == '__main__':
	reader('Survey_Supervisors.csv')		
