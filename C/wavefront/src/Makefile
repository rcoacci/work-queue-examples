include ../config.mk


EXTERNAL_DEPENDENCIES = ${CCTOOLS_INSTALL_DIR}/lib/libbatch_job.a ${CCTOOLS_INSTALL_DIR}/lib/libwork_queue.a ${CCTOOLS_INSTALL_DIR}/lib/libchirp.a ${CCTOOLS_INSTALL_DIR}/lib/libdttools.a
PROGRAMS = wavefront wavefront_master
TARGETS = $(PROGRAMS)

all: $(PROGRAMS)
$(PROGRAMS): $(EXTERNAL_DEPENDENCIES)

CC=@echo COMPILE $@;gcc

%.o: %.c
	$(CC) -o $@ -c -I${CCTOOLS_INSTALL_DIR}/include/cctools/ $< 


LD = @echo LINK $@;gcc

%: %.o
	$(LD) -o $@ $(LDFLAGS) $(LOCAL_LDFLAGS) $^ -lm -lz

# Cancel Make defined implicit rule:
%: %.c

.PRECIOUS: %.o

clean:
	rm -f $(PROGRAMS) *.o

install: all
	mkdir -p $(CCTOOLS_INSTALL_DIR)/bin
	cp $(PROGRAMS) $(CCTOOLS_INSTALL_DIR)/bin/

test: all

.PHONY: all clean install test
