# Commented out IPython magic to ensure Python compatibility.
#    %tensorflow_version 1.x
import os
from pathlib import Path
import gpt_2_simple as gpt2
from datetime import datetime
import pandas as pd
import tensorflow as tf
import nltk
import regex as re
from app.configurations.settings import get_settings

def runModelSingleInput(run_name, input):
  RESOURCE_PATH = os.getcwd() + get_settings().checkpoint_dir
  file_path = Path(os.path.join(RESOURCE_PATH))
  print( 'inside run_Model')
  tf.reset_default_graph()
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess,checkpoint_dir= file_path,run_name=run_name)
  print( run_name, ' :: Model loaded ')
  output = predict(sess,run_name,input)
  return output
  
def runModelMultipleInputs(run_name, input):
  print( 'inside run_Model')
  RESOURCE_PATH = os.getcwd() + get_settings().checkpoint_dir
  file_path = Path(os.path.join(RESOURCE_PATH))
  tf.reset_default_graph()
  sess = gpt2.start_tf_sess()
  gpt2.load_gpt2(sess,checkpoint_dir= file_path,run_name=run_name)
  print( run_name, ' :: Model loaded ')
  output= []
  for i in input:
    print('input i ::',i)
    output.append(predict(run_name,i))
  return output

def predict(sess,run_name,input):
  RESOURCE_PATH = os.getcwd() + get_settings().checkpoint_dir
  file_path = Path(os.path.join(RESOURCE_PATH))
  output = gpt2.generate(sess,
                         checkpoint_dir= file_path,
                         run_name = run_name,
                  prefix=input,
                  length=100,
                  temperature=0.7,
                  nsamples=1,
                  return_as_list=True
                  )
  output = output[0].replace(input,'')
  output = output.replace('\', \'','')
  output = output.replace('[\'','')
  output = output.replace('[','')
  output = output.replace(']','')
  output = output.replace('.,','.')
  output = output.replace('"','.')
  output = re.sub('\s+',' ',output)
  output = re.sub('^,','',output)
  print( run_name, ' :: Output generated ')
  return output

def getModelOutputSingleInput(Input_Job_title,Input_Skills,Input_Company_name,Input_Location):
  text_skills = runModelSingleInput('run1',Input_Job_title+ ' '+Input_Skills)
  
  text_role = runModelSingleInput('run2',Input_Job_title+ ' '+Input_Skills)
  
  text_aboutCompany = runModelSingleInput('run3',Input_Company_name +' '+Input_Location)
  
  output = {}
  output['SKILLS']=text_skills 
  output['ROLES']=text_role
  output['ABOUT COMPANY']=text_aboutCompany
  return output

def getModelOutputMultipleInputs(Input_Job_title,Input_Skills,Input_Company_name,Input_Location):

  text_skills = runModelMultipleInputs('run1',Input_Job_title+ ' '+Input_Skills)
  
  text_role = runModelMultipleInputs('run2',Input_Job_title+ ' '+Input_Skills)
  
  text_aboutCompany = runModelMultipleInputs('run3',Input_Company_name +' '+Input_Location)
  
  output = {}
  output['SKILLS']=text_skills 
  output['ROLES']=text_role
  output['ABOUT COMPANY']=text_aboutCompany
  return output

       