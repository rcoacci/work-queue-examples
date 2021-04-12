
# Set the variable to point to your cctools installation directory.
CCTOOLS_INSTALL_DIR=${HOME}/cctools

all: wavefront wavefront_master

wavefront: wavefront.o

wavefront_master: wavefront_master.o

%.o: %.c
	gcc -o $@ -c -I${CCTOOLS_INSTALL_DIR}/include/cctools $< 

%: %.o
	gcc -o $@ $(LDFLAGS) $^ -L${CCTOOLS_INSTALL_DIR}/lib -lbatch_job -lwork_queue -ldttools -lchirp -ldttools -lm -lz

clean:
	rm -f wavefront.o wavefront wavefront_master.o wavefront_master
