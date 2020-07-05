all:
	${MAKE} -C models $@
	${MAKE} -C data $@

clean:
	${MAKE} -C models $@
	${MAKE} -C data $@
