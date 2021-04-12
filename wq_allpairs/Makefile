
# Set the variable to point to your cctools installation directory.
CCTOOLS_INSTALL_DIR=${HOME}/cctools

all: allpairs_multicore allpairs_manager

allpairs_multicore: allpairs_multicore.o allpairs_compare.o

allpairs_manager: allpairs_manager.o allpairs_compare.o

%.o: %.c
	gcc -o $@ -c -I${CCTOOLS_INSTALL_DIR}/include/cctools $< 

%: %.o
	gcc -o $@ $(LDFLAGS) $^ -L${CCTOOLS_INSTALL_DIR}/lib -lbatch_job -lwork_queue -ldttools -lchirp -ldttools -lm -lz -lpthread

clean:
	rm -f allpairs_multicore.o allpairs_multicore allpairs_manager.o allpairs_manager
