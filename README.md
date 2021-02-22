### Repository to test python concepts and libraries

Before working on any python project, its always recommended to use virtualenv to control the dependencies you use for a specific project. I prefer using virtualenvwrapper to manage the python virtualenvs I use during the project lifecycle.

`Reference:` https://virtualenvwrapper.readthedocs.io/en/latest/

#### Creating and using virtualenv:

- Export WORKON_HOME env variable:
  - `export WORKON_HOME=~/Envs`
  
- Create virtualenv using virtualenvwrapper:
  - `mkvirtualenv pylearn-elasticsearch`
  This will create a virtualenv at your user home inside Envs directory. 
  
- Select this virtualenv in your IDE.

- Install elasticsearch python library based on your elasticsearch cluster version:
  `pip install elasticsearch>=7.0.0,<8.0.0`
