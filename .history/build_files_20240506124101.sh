# build_files.sh
python3.12cpip install -r requirements.txt
python3.12 manage.py collectstatic
