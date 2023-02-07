This is a project to generate Job Description based on inputs. 
A well-written job description will establish a solid set of expectations for employers to communicate to their employees which helps to work more efficiently in their roles. Inconsistent job descriptions lead to improper selection which affects the ROI. To overcome the above mentioned problem we need an AI based solution to write the job description.


We have generated excel as well as pickle file  to be used by other codes. 

<b>Releases</b>
To see only the output, please go to <b> Projects--->API----> Task7_Api.ipynb file </b>. At the end you will get a public URL. Please use that to see final results. 

<b>To run manually</b>

1. Mount your google drive on colab. 
2. Install Dependencies using requirements.txt
3. Upload this project directory.
4. Go to notebooks and run the files as per sequence mentioned. 
**  Please note that transformer notebooks takes a lot of time to run. We have saved trained model (tar files) under Resources/Model. You can skip running Task4.1_GPT5Model_Skill.ipynb,Task4.2_GPT5Model_Role.ipynb and Task4.3_GPT5Model_AboutCompany.ipynb Instead you can directly run Task5_ModelOutputGenerator.ipynb


Project Organization

├── README.txt         		<- The top-level README for developers using this project.
│
├── Core 	                <- Logging files and dependencies file.
│ 	├── requirement.txt 	<- Stores all the dependencies of this project
│
├── Resources                   <- Stores files to be used by project.
│       ├── data
│  	        ├── external    <- Data from third party sources.
│               │ 
│  	        ├── interim     <- Intermediate data that has been transformed.
│               │  	  ├── cleaned_indeed_job_dataset.xlsx     <- cleaned excel file generated from  Task1_JobDescriptionDataCleaning.ipnyb   
│               │ 
│               ├── processed    <- The final data sets for modeling.
│	 	│         ├── skills_dataset.xlsx
│	 	│         ├── skill_dataset.txt 
│	 	│         ├── roles_dataset.xlsx
│		│         ├── role_dataset.txt
│	 	│         ├── whyus_dataset.xlsx
│	        │         ├── whyus_dataset.txt
│	    	│ 
│     		├──  raw         <- The original data set.
│		          ├── indeed_job_dataset.csv
│
│      ├── Model	        <- contains saved models trained on our dataset.
│		├── T5-Aboutcompany      <- For saving T5 trained model
│	  	├── T5-Role
│	 	├── T5-Skill
│		├── checkpoint_run1.tar   <- tar files are for saved GPT2 models
│		├── checkpoint_run2.tar
│		├── checkpoint_run3.tar
│      ├── Templates            <- contains HTML files for API
│		├── datainsights.html
│	  	├── index.html
│	 	├── textGeneration.html
├── notebooks                   <- contains ipnyb files with results to  get a quick glance.  
│
│	├── Visualizations
│		├── ExploratoryDataAnalysis.ipynb
│		├── InsightsUsingSQL.ipynb
│		├── SQL_EDA.ipynb
│
│	├── Task1_JobDescriptionDataCleaning.ipnyb
│	├── Task2_JobDescription_Segregator.ipynb
│	├── Task3.1_GPT2Model_Skill.ipynb
│	├── Task3.2_GPT2Model_Role.ipynb
│	├── Task3.3_GPT2Model_AboutCompany.ipynb
│	├── Task4.1_GPT5Model_Skill.ipynb
│	├── Task4.2_GPT5Model_Role.ipynb
│	├── Task4.3_GPT5Model_AboutCompany.ipynb
│	├── Task5_ModelOutputGenerator.ipynb
│	├── Task6_EvaluatingModel.ipynb
│    	
├── Project
│       ├── API
│	      ├── Task7_Api.ipynb
│       ├── Services
│	├── Utils             <- contains .py files to be used to as modules for importing
│		├── main.py   
│		├── Task1_indeedJobScraping.py
│		├── task2_insightsusingsql.py
│		├── task8_modeloutputgenerator.py
│		├── task9_evaluatingmodel.py
├── runtime  <- contains the fastapi implemetation
        ├─ 
	
