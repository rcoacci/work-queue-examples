include config.mk
include rules.mk

ALLPAIRS_PACKAGES=src

all: $(ALLPAIRS_PACKAGES)

config.mk:
	@echo "You must run 'configure' before '${MAKE}'."
	@exit 1

$(ALLPAIRS_PACKAGES): config.mk
	@$(MAKE) -C $@

CLEAN_PACKAGES = $(ALLPAIRS_PACKAGES:%=clean-%)
$(CLEAN_PACKAGES):
	@$(MAKE) -C $(@:clean-%=%) clean
clean: $(CLEAN_PACKAGES)

INSTALL_PACKAGES = $(ALLPAIRS_PACKAGES:%=install-%)
$(INSTALL_PACKAGES): $(ALLPAIRS_PACKAGES)
	@$(MAKE) -C $(@:install-%=%) install
install: $(INSTALL_PACKAGES)
	mkdir -p $(ALLPAIRS_INSTALL_DIR)/bin
	mkdir -p ${ALLPAIRS_INSTALL_DIR}/etc
	cp config.mk ${ALLPAIRS_INSTALL_DIR}/etc/

.PHONY: $(ALLPAIRS_PACKAGES) $(INSTALL_PACKAGES) $(CLEAN_PACKAGES) all clean install 
