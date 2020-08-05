SAMPLES?=24
TMAX?=365
N?=100000
MAXMEM?=2097152
PROCS?=
MODELS=../models
SCRIPTS=../scripts
PLOT?=coupled-epidemics-caseplot
KASIM=KaSim -mode batch -u time -p 1 --no-log

all:
	${MAKE} MODEL=second-wave second-wave-avg.tsv
	${MAKE} MODEL=scotland-england scotland-england-avg.tsv
	${MAKE} PLOT=coupled-epidemics-scoeng scotland-england.png
	${MAKE} MODEL=scotland-england ARGS="-var reopen 0" scotland-england-notransport-avg.tsv
	${MAKE} PLOT=coupled-epidemics-scoeng scotland-england-notransport.png

clean:
	rm -rf *.png *.tsv traj
	rm -f deadlock.ka
	rm -f inputs*.ka

%.png: %-avg.tsv
	${SCRIPTS}/${PLOT} ${@:%.png=%}

%-avg.tsv: ${MODELS}/${MODEL}.ka
	mkdir -p traj
	ulimit -v ${MAXMEM}; seq ${SAMPLES} | parallel ${PROCS} ${KASIM} -seed '{}' -o traj/${@:%-avg.tsv=%}-'{}'.dat -l ${TMAX} -var N ${N} ${ARGS} $< ${KAPPA} || true
	${SCRIPTS}/combine -k -d, -o ${@:%-avg.tsv=%} -i traj/${@:%-avg.tsv=%}-[0-9]*.dat
