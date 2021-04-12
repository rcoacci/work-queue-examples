include ../config.mk

OBJECTS = allpairs_compare.o
PROG_OBJ =  allpairs_master.o allpairs_multicore.o
PROGRAMS = allpairs_multicore allpairs_master
TARGETS = $(PROGRAMS)

all: $(TARGETS)

CCFLAGS= -I${SAND_INSTALL_DIR}/include/ -I${CCTOOLS_INSTALL_DIR}/include/cctools/
EXTERNAL_DEPENDENCIES = ${SAND_INSTALL_DIR}/lib/libsandtools.a ${CCTOOLS_INSTALL_DIR}/lib/libwork_queue.a ${CCTOOLS_INSTALL_DIR}/lib/libdttools.a

EXTERNAL_LINKAGE = \
     -lz \
    -lpthread \
    -lm \

LDFLAGS = -L$(SAND_INSTALL_DIR)/lib -L$(CCTOOLS_INSTALL_DIR)/lib $(BASE_LDFLAGS)

CC=@echo COMPILE $@;gcc

%.o: %.c
	$(CC) -o $@ -c $(CCFLAGS) $<

LD = @echo LINK $@;gcc

%: %.o
	$(LD) -o $@ $(LDFLAGS) $^ $(EXTERNAL_LINKAGE)

# Cancel Make defined implicit rule:
%: %.c

.PRECIOUS: %.o

$(PROGRAMS): $(OBJECTS) $(EXTERNAL_DEPENDENCIES)

clean:
	rm -f $(OBJECTS) $(PROG_OBJ) $(TARGETS)

install: all
	mkdir -p $(ALLPAIRS_INSTALL_DIR)/bin
	cp $(PROGRAMS) $(ALLPAIRS_INSTALL_DIR)/bin/

test: all

.PHONY: all clean install test
