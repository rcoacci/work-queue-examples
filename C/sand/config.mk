# Generated at Tue Jun  4 10:48:54 EDT 2019 by nhazekam@disc24.crc.nd.edu

CCTOOLS_INSTALL_DIR=/afs/crc.nd.edu/user/n/nhazekam/cctools/
SAND_INSTALL_DIR=/afs/crc.nd.edu/user/n/nhazekam/work-queue-examples/C/sand


CCFLAGS= \
    -I${CCTOOLS_INSTALL_DIR}/include/cctools/ \
	-DCCTOOLS_OPSYS_LINUX \

#	-D_GNU_SOURCE \
# Only needed if
#   -std=c99

LD = @echo LINK $@;gcc

#BASE_LDFLAGS =  -Xlinker -Bstatic -static-libgcc -Xlinker -Bdynamic -Xlinker --as-needed -g

EXTERNAL_LINKAGE =  -lresolv -lnsl -lrt -ldl -lz -lstdc++ -lpthread -lz -lc -lm

LDFLAGS = -L$(SAND_INSTALL_DIR)/lib $(BASE_LDFLAGSa)

#READLINE_LDFLAGS=-lreadline -Xlinker --no-as-needed -lncurses -lhistory -Xlinker --as-needed

#AR=ar

