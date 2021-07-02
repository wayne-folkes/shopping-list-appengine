
export GOOGLE_APPLICATION_CREDENTIALS=/Users/wayne/dev/shopping-list-appengine/creds.json

deploy:
	gcloud app deploy -q

view:
	gcloud app browse

local:
	python main.py
