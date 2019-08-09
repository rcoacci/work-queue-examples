include ../config.mk
include ../rules.mk

LOCAL_LINKAGE = -lpthread

EXTERNAL_DEPENDENCIES = ${SAND_INSTALL_DIR}/lib/libsandtools.a ${CCTOOLS_INSTALL_DIR}/lib/libwork_queue.a ${CCTOOLS_INSTALL_DIR}/lib/libdttools.a
OBJECTS = allpairs_compare.o allpairs_master.o allpairs_multicore.o
PROGRAMS = allpairs_multicore allpairs_master
TARGETS = $(PROGRAMS)

all: $(TARGETS)

$(PROGRAMS): $(OBJECTS) $(EXTERNAL_DEPENDENCIES)

clean:
	rm -f $(OBJECTS) $(TARGETS)

install: all
	mkdir -p $(ALLPAIRS_INSTALL_DIR)/bin
	cp $(PROGRAMS) $(ALLPAIRS_INSTALL_DIR)/bin/

test: all

.PHONY: all clean install test
