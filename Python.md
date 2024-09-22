# Why do we need VIRTUAL ENVIRONMENT ....
if your project is working as a specific python version requirement and if you already installed python so that specific version you can't use as a 
correctly.....   and  you are working different different project and having different versions  so you can't run python properly ..

##  virtual environment 
It makes python project specific versions that actually needs that project and it isolate your global python version..

cmd  :  python3  -m  venv  <VIRTUAL_ENV_NAME>
e.g. :  python3  -m  venv  my_env

##  Active virtual Environment :
  :  source  <VIRTUAL_ENV_NAME>/bin/active

##  Deactive virtual Environment :
  :  deactive


##  separately download this 
pip3 install pandas==1.4.3

##  Organization or Project uses its requirement.txt file for maintaining all python version.
pip3 install   -r requirement.txt


##  exit function exits from python shell/terminal..
exit()

## all the installed version shows that is installed in local python // if you are in virtual env so shows installed versions
pip freeze

pip freeze > requirement.txt  ( creates a file with added containent of all download python version )

