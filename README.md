# AgriEdge ML project template 
## Overview 
this is a biased template to be used for AgriEdge project hosted in google drive 
## How to use : 
> Method 1
- clone the template localy and start working 
> Method 2 
- create a colab notebook and run this script : 
```python
def create_project_from_template( project_name , projects_folder ,template_path = 'https://github.com/AnasAito/AgriEdge-project-template.git' ):
  # mount drive 
  
  from google.colab import drive
  drive.mount('/content/gdrive')
  # cd to projects folder 
  %cd  gdrive/MyDrive/{projects_folder} 
  # clone template 
  ! git clone https://github.com/AnasAito/AgriEdge-project-template.git
  # chnage name to project_name
  ! mv AgriEdge-project-template {project_name}
  
## run this function
create_project_from_template( project_name='-Project Name-' , projects_folder ='-Parent folder-',template_path = 'https://github.com/AnasAito/AgriEdge-project-template.git' )
```
- the script create a new folder for your project by cloning this template 
