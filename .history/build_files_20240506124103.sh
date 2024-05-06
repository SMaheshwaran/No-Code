# build_files.sh
python3.12pip install -r requirements.txt
python3.12 manage.py collectstatic
