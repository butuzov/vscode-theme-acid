
build:
	./scripts/compiler

build_quick:
	./scripts/compiler --quick

node_modules/vsce:
	npm install vsce


build_ext_prod: node_modules/vsce build_quick
	vsce package

build_ext_dev: node_modules/vsce build_quick
	vsce package -o acid-dev.vsix

install_ext_dev: build_ext_dev
	code --force --install-extension acid-dev.vsix

publush_ext: build_ext_prod
	@read -p "VSCode Marketplace Token: " TOKEN; \
	vsce publish -p $$TOKEN

syntax:
	@read -p "Enter tmLanguage filename: " language; \
	./scripts/grammar syntaxes/$$language;
