#
# csc427-222 makefile proj1
# author: bjr
# last-update:
#	20 jan 2022 -bjr: created
#	26 feb 2022 -aak: trunc and testing targets
#


F= proj1
PY= python3

all:
	@echo "testing process"	

testing:
	make trunc
	${PY} $F-testing.py >> grade.txt

trunc:
	head -n`grep -ns "comments:" grade.txt  | sed 's/:.*//'` grade.txt > grade_t.txt
	mv grade_t.txt grade.txt

nbconvert:
	jupyter nbconvert --to=script $F.ipynb

clean:
	-rm $F.py grade_t.txt
