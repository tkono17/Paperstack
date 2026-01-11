#!/usr/bin/env bash

paperstack-cli db reset

doctypes=(Article Eprint
	  Thesis ThesisD ThesisM ThesisB Presentation
	  Manual Specification Tutorial TechnicalNote Datasheet
	  Review Book)
for dt in ${doctypes[*]}; do
    paperstack-cli doctype create ${dt}
done
