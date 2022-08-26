default: clean
	python3 main.py

clean:
	rm -f links.txt geckodriver.log

unfollow:
	