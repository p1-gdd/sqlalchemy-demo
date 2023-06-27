SRC=sqlalchemy

.PHONY: preview pdf clean predeps

all: pdf

pdf: $(SRC).pdf
view: view-$(SRC)

%.pdf: %.tex prepare
	latexmk -pdf $<

preview-%: %.tex prepare
	latexmk -pdf -pvc $<

view-%: %.pdf
	impressive --nologo --time-display --transition None --tracking $<

.ONESHELL:
clean: restore
	git clean -dxf -e $(SRC).tex


predeps:
	sudo apt update
	sudo apt install -qq -y docker.io
	sudo apt install -qq -y texlive-full zathura impressive
	sudo apt install -qq -y mariadb-client-core libmariadb-dev python3-sqlalchemy
	sudo pip3 install -qq --break-system-packages mariadb

prepare restore clean-mariadb:
	make -sC data $@
