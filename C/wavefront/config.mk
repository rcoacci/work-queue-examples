# Generated at Tue Jun  4 10:48:54 EDT 2019 by nhazekam@disc24.crc.nd.edu

CCTOOLS_INSTALL_DIR=/afs/crc.nd.edu/user/n/nhazekam/cctools/
WAVEFRONT_INSTALL_DIR=/afs/crc.nd.edu/user/n/nhazekam/work-queue-examples/C/sand

CC=@echo COMPILE $@;gcc

BASE_CCFLAGS= -D__EXTENSIONS__ -D_LARGEFILE64_SOURCE -D__LARGE64_FILES -Wall -Wextra -Wno-unused-parameter -Wno-unknown-pragmas -Wno-deprecated-declarations -Wno-unused-const-variable -fPIC -DHAS_EXT2FS -DHAS_LIBREADLINE -DHAVE_GMTIME_R -DHAVE_FDATASYNC -DHAS_ISNAN -DHAVE_ISNAN -DSQLITE_HAVE_ISNAN -DHAVE_LOCALTIME_R -DHAS_OPENAT -DHAS_PREAD -DUSE_PREAD -DUSE_PREAD64 -DHAS_PWRITE -DUSE_PWRITE -DUSE_PWRITE64 -DHAVE_STRCHRNUL -DHAS_STRSIGNAL -DHAS_USLEEP -DHAVE_USLEEP -DHAS_UTIME -DHAVE_UTIME -DHAS_UTIMENSAT -DHAS_ATTR_XATTR_H -DHAS_SYS_XATTR_H -DHAS_IFADDRS -DHAS_INTTYPES_H -DHAVE_INTTYPES_H -DHAS_STDINT_H -DHAVE_STDINT_H -DHAS_SYS_STATFS_H -DHAS_SYS_STATVFS_H -DHAS_SYSLOG_H -D_GNU_SOURCE -D_REENTRANT -g

CCFLAGS= -I${CCTOOLS_INSTALL_DIR}/include/cctools/ ${BASE_CCFLAGS} -std=c99

CXX=@echo COMPILE $@;g++

BASE_CXXFLAGS=${BASE_CCFLAGS}

CXXFLAGS=${BASE_CCFLAGS}

LD = @echo LINK $@;gcc

BASE_LDFLAGS =  -Xlinker -Bstatic -static-libgcc -Xlinker -Bdynamic -Xlinker --as-needed -g

INTERNAL_LDFLAGS = $(BASE_LDFLAGS) 

EXTERNAL_LINKAGE =  -lresolv -lnsl -lrt -ldl -lz -lstdc++ -lpthread -lz -lc -lm

LDFLAGS = -L$(INSTALL_DIR)/lib $(BASE_LDFLAGS)

READLINE_LDFLAGS=-lreadline -Xlinker --no-as-needed -lncurses -lhistory -Xlinker --as-needed

AR=ar

