#!/usr/bin/env bash

paperstack-cli db reset

doctypes=(Article Eprint
	  Thesis ThesisD ThesisM ThesisB Presentation
	  Manual Specification Tutorial TechnicalNote Datasheet
	  Review Book)
for dt in ${doctypes[*]}; do
    paperstack-cli doctype create ${dt}
done

paperstack-cli document create\
	       --title 'Inclusive jet cross sections and dijet correlations in D^{*\pm} photoproduction at HERA'\
	       --authors 'ZEUS Collaboration'\
	       --eprint 'hep-ex/0507089'\
	       --reference 'Nucl.Phys.B729:492-525,2005'\
	       --doi '10.1016/j.nuclphysb.2005.09.021'
