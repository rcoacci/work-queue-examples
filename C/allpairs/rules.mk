#
# Rules for building various sorts of files
#

%.o: %.c
	$(CC) -o $@ -c $(CCFLAGS) $(LOCAL_CCFLAGS) $<

%.o: %.cc
	$(CXX) -o $@ -c $(CXXFLAGS) $(LOCAL_CXXFLAGS) $<

%.o: %.C
	$(CXX) -o $@ -c $(CXXFLAGS) $(LOCAL_CXXFLAGS) $<

%.a:
	$(AR) rv $@ $^
	ranlib $@

%: %.o
ifeq ($(STATIC),1)
	$(LD) -static -g -o $@ $(LOCAL_LINKAGE) $^ $(STATIC_LINKAGE)
else
	$(LD) -o $@ $(LDFLAGS) $(LOCAL_LDFLAGS) $^ $(LOCAL_LINKAGE) $(EXTERNAL_LINKAGE)
endif

%.so:
	$(LD) -o $@ -fPIC $(DYNAMIC_FLAG) $(LDFLAGS) $(LOCAL_LDFLAGS) $^ $(LOCAL_LINKAGE) $(EXTERNAL_DYNLIBS)

%.$(DYNAMIC_SUFFIX):
	$(LD) -o $@ -fPIC $(DYNAMIC_FLAG) $(LDFLAGS) $(LOCAL_LDFLAGS) $^ $(LOCAL_LINKAGE) $(EXTERNAL_DYNLIBS)

# Cancel Make defined implicit rule:
%: %.c
%: %.cc
%: %.C

.PRECIOUS: %.o
