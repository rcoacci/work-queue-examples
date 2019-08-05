include config.mk
include rules.mk

WAVEFRONT_PACKAGES=src

all: $(WAVEFRONT_PACKAGES)

config.mk:
	@echo "You must run 'configure' before '${MAKE}'."
	@exit 1

$(WAVEFRONT_PACKAGES): config.mk
	@$(MAKE) -C $@

CLEAN_PACKAGES = $(WAVEFRONT_PACKAGES:%=clean-%)
$(CLEAN_PACKAGES):
	@$(MAKE) -C $(@:clean-%=%) clean
clean: $(CLEAN_PACKAGES)

INSTALL_PACKAGES = $(WAVEFRONT_PACKAGES:%=install-%)
$(INSTALL_PACKAGES): $(WAVEFRONT_PACKAGES)
	@$(MAKE) -C $(@:install-%=%) install
install: $(INSTALL_PACKAGES)
	mkdir -p $(WAVEFRONT_INSTALL_DIR)/bin
	mkdir -p ${WAVEFRONT_INSTALL_DIR}/etc
	cp config.mk ${WAVEFRONT_INSTALL_DIR}/etc/

.PHONY: $(WAVEFRONT_PACKAGES) $(INSTALL_PACKAGES) $(CLEAN_PACKAGES) all clean install 
