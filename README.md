### Installation
- clone git repo 
```
git clone https://github.com/Zharkyn20/employee_tree.git
```
- move to employee_tree
```
cd employee_tree
```
- install requirements
```
pip install -r requirements.txt
```
- make migrations
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
- populate db (randomly creates 50 departments, and more than 100_000 employees)
- also creates superuser with username: 'admin', password: 'admin'
```
python3 manage.py populate
```
- run script
```
python3 manage.py runserver
```
