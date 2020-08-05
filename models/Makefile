SCRIPTS=../scripts
MODELS=second-wave.ka scotland-england.ka

all:
	${MAKE} ${MODELS}

clean:
	rm -f ${MODELS}

%.ka: %.ska
	${SCRIPTS}/stratify < $< > $@
