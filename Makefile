publish:
	git config --global user.email tonybutzer@gmail.com
	git config --global user.name tonybutzer
	git config --global push.default simple
	git add .
	git commit -m "automatic git update from Makefile"
	git push

build:
	sudo pip3 install -e .

web:
	(cd docs/build/html && python -m SimpleHTTPServer)
