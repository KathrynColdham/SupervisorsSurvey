#!/bin/bash

QuestionArray=(  '1. For how many years have you been a member of the CMS collaboration?'
		 '2. In which age range do you fall under?'
                 '3. What gender do you identify as?'
                 '4. What is your country of residence?'
                 '5. In which country is your home institute?'
                 '6. Do you have children?'
                 '7. Are you a carer?'
                 '8. For how long have you had experience in supervising PhD students, either in or outside of CMS?'
                 '9. How many PhD students have you supervised during your career?'
                 '10. How many PhD students do you currently supervise?'
                 '11. Of the PhD students you have supervised, what percentage have worked in a different field to you?'
                 '12. If you have supervised PhD students who work in a different field to you, how have you found this in comparison to supervising a PhD student in the same field as you?'
                 '13. If you have supervised PhD students who work in a different field to you, is there anything you wish to add about how you have found this?'
                 '14. Of the PhD students you have supervised, what percentage have worked on an experiment other than CMS (e.g. experiments at DESY, FNAL, etc...)?'
                 '15. If you have supervised PhD students on other experiments, how have you found this in comparison to supervising a CMS PhD student?'
                 '16. If you have supervised PhD students that work on experiments other than CMS, is there anything you would like to add about how have you found this?'
                 '17. How often do/did you have one-to-one meetings with your PhD students?'
                 '18. For how long do/did these one-to-one meetings normally last?'
                 '19. How often do/did you meet with your PhD students in a group setting?'
                 '20. For how long do/did these group meetings normally last?'
                 '21. Which of the following methods of communication do/did you use with your students?'
                 '22.  Do/did you as a PhD supervisor provide other individuals - for example postdocs - for PhD students to talk to and get help from?'
                 '23. Considering all support offered in combination, including from yourself, co-supervisors, and from others like postdocs, how frequent is the support your students receive?'
                 '24. Which of the following best describes how you interact(ed) and the frequency of your interactions with your PhD students?'
                 '25. How similar is/was this to the interactions you had with your supervisor when you were a PhD student?'
                 '26. Is the way in which you interact(ed) and the frequency of your interactions with your PhD students the result of a conscious decision? Why or why not?'
                 '27. Which of the following best describes your job/best described your job whilst you supervised PhD students? If your job is not listed, please add it in the "other" field.'
                 '28. Do/did you hold other professional roles in addition to supervising PhD students? Please indicate these using the below options. If you hold/held any responsibilities not listed, please list them in "other".'
                 '29. How happy are/were you with being a supervisor in general?'
                 '30. How satisfied are/were you with the level of support offered to supervisors within your home institution?'
                 '31. Please highlight the sources of support within your home institution that you benefit(ted) from.'
                 '32. How satisfied are you/were with the level of support offered to supervisors within CMS? '
                 '33. Please highlight the sources of support within CMS that you benefit(ted) from.'
                 '34. Please highlight any sources of support for supervisors that you feel are missing within CMS.'
                 '35. Would you (have) benefit(ted) from a CMS training programme for PhD supervisors?'
                 '36. If a CMS training programme for PhD supervisors were to be created, which of the following would you like for it to include? Multiple choices can be selected for this answer. If you would like to suggest an option not included, please provide it in the "other" field.'
                 '37. Which of the following do you feel would be helpful for supervisors to have access to? If you would like to contribute a suggestion, please add this by selecting the "other" field.'
                 '38. This question is completely optional for you to answer, should you feel comfortable enough to do so. Please rate how has your mental health been since the COVID-19 pandemic began? '
                 '39. This question is completely optional for you to answer, should you feel comfortable enough to do so. Please rate the overall impact that your supervisory responsibilities had/have on your mental health?'
                 '40. This question is completely optional for you to answer, should you feel comfortable enough to do so.  On a typical day, how manageable is/was your workload while being a supervisor?')



if [ ! -d Results_HeatMaps ]; then
  mkdir Results_HeatMaps;
fi


for i in ${!QuestionArray[@]}; do
	for j in ${!QuestionArray[@]}; do
        	python3 HeatMap.py --first "${QuestionArray[j]}" --second "${QuestionArray[i]}"
	done
done
