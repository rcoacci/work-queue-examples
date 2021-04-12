
# Set the variable to point to your cctools installation directory.
CCTOOLS_INSTALL_DIR=${HOME}/cctools

all: wq_sort

wq_sort: wq_sort.o

%.o: %.c
	gcc -o $@ -c -I${CCTOOLS_INSTALL_DIR}/include/cctools $< 

%: %.o
	gcc -o $@ $(LDFLAGS) $^ -L${CCTOOLS_INSTALL_DIR}/lib -lwork_queue -ldttools -lm -lz

clean:
	rm -f wq_sort.o wq_sort

