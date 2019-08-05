include ../config.mk
include ../rules.mk

EXTERNAL_DEPENDENCIES = ${CCTOOLS_INSTALL_DIR}/lib/libbatch_job.a ${CCTOOLS_INSTALL_DIR}/lib/libwork_queue.a ${CCTOOLS_INSTALL_DIR}/lib/libchirp.a ${CCTOOLS_INSTALL_DIR}/lib/libdttools.a
PROGRAMS = wavefront wavefront_master
TARGETS = $(PROGRAMS)

all: $(PROGRAMS)
$(PROGRAMS): $(EXTERNAL_DEPENDENCIES)

clean:
	rm -f $(PROGRAMS) *.o

install: all
	mkdir -p $(CCTOOLS_INSTALL_DIR)/bin
	cp $(PROGRAMS) $(CCTOOLS_INSTALL_DIR)/bin/

test: all

.PHONY: all clean install test
