tests:
	nosetests
	
dev_test:
	when-changed -r test 'clear && make tests'; 