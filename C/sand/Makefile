include config.mk
include rules.mk

SAND_PACKAGES=src

all: $(SAND_PACKAGES)

config.mk:
	@echo "You must run 'configure' before '${MAKE}'."
	@exit 1

$(SAND_PACKAGES): config.mk
	@$(MAKE) -C $@

CLEAN_PACKAGES = $(SAND_PACKAGES:%=clean-%)
$(CLEAN_PACKAGES):
	@$(MAKE) -C $(@:clean-%=%) clean
clean: $(CLEAN_PACKAGES)

INSTALL_PACKAGES = $(SAND_PACKAGES:%=install-%)
$(INSTALL_PACKAGES): $(SAND_PACKAGES)
	@$(MAKE) -C $(@:install-%=%) install
install: $(INSTALL_PACKAGES)
	mkdir -p $(SAND_INSTALL_DIR)/bin
	mkdir -p ${SAND_INSTALL_DIR}/etc
	cp config.mk ${SAND_INSTALL_DIR}/etc/

.PHONY: $(SAND_PACKAGES) $(INSTALL_PACKAGES) $(CLEAN_PACKAGES) all clean install 
