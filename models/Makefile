SCRIPTS=../scripts

all:
	${MAKE} second-wave.ka

clean:
	rm -f second-wave.ka

%.ka: %.pka
	${SCRIPTS}/stratify < $< > $@
