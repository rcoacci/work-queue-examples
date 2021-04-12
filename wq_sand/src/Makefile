include ../config.mk

LOCAL_CCFLAGS = -O3

EXTERNAL_DEPENDENCIES = ${CCTOOLS_INSTALL_DIR}/lib/libwork_queue.a ${CCTOOLS_INSTALL_DIR}/lib/libdttools.a
LIBRARIES = libsandtools.a
OBJECTS = $(SOURCES:%.c=%.o)
PROGRAMS = sand_align_master sand_align_kernel sand_filter_master sand_filter_kernel sand_compress_reads sand_uncompress_reads
SCRIPTS = sand_runCA_5.4 sand_runCA_6.1 sand_runCA_7.0
SOURCES = compressed_sequence.c sequence_filter.c sequence.c matrix.c overlap.c align.c
HEADERS_PUBLIC = align.h matrix.h
TARGETS = $(PROGRAMS) $(LIBRARIES)

CC=@echo COMPILE $@;gcc

%.o: %.c
	$(CC) -o $@ -c $(CCFLAGS) $(LOCAL_CCFLAGS) $<

%.a:
	$(AR) rv $@ $^
	ranlib $@

%: %.o
	$(LD) -o $@ $(LDFLAGS) $^ $(EXTERNAL_LINKAGE)

# Cancel Make defined implicit rule:
%: %.c

.PRECIOUS: %.o

all: $(TARGETS)

libsandtools.a: $(OBJECTS)

$(PROGRAMS): $(LIBRARIES) $(EXTERNAL_DEPENDENCIES)

clean:
	rm -f $(OBJECTS) $(PROGRAMS) $(LIBRARIES) *.o

install: all
	mkdir -p $(SAND_INSTALL_DIR)/bin
	chmod 755 $(PROGRAMS) $(SCRIPTS)
	cp $(PROGRAMS) $(SCRIPTS) $(SAND_INSTALL_DIR)/bin/
	mkdir -p $(SAND_INSTALL_DIR)/lib
	cp $(LIBRARIES) $(SAND_INSTALL_DIR)/lib/
	mkdir -p $(SAND_INSTALL_DIR)/include
	cp $(HEADERS_PUBLIC) $(SAND_INSTALL_DIR)/include/

test: all

.PHONY: all clean install test
