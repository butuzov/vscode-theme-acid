
build:
	./scripts/compiler

build_quick:
	./scripts/compiler --quick

syntax:
	@read -p "Enter tmLanguage filename: " language; \
	./scripts/grammar syntaxes/$$language;

install-acid: package-theme
	code --force --install-extension acid.vsix

install-yq:
	sudo apt-get install jq

install-vsce:
	npm install vsce

deps-ci-release: install-vsce install-yq

package-theme: node_modules/vsce
	npm run package:vsix

package-publish: node_modules/vsce
	npm run publish:vsix
