$pdflatex = 'pdflatex --shell-escape %O %S';
$recorder = 1;
$pdf_previewer = 'zathura %S';

$hash_calc_ignore_pattern{'pdf'} = '.*';
$hash_calc_ignore_pattern{'gdb'} = '.*';
$hash_calc_ignore_pattern{'stdout'} = '.*';
$hash_calc_ignore_pattern{'stderr'} = '.*';

add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');

sub run_makeglossaries {
  if ( $silent ) {
    system "makeglossaries -q '$_[0]'";
  }
  else {
    system "makeglossaries '$_[0]'";
  };
}
push @generated_exts, 'glo', 'gls', 'glg';
push @generated_exts, 'acn', 'acr', 'alg';
$clean_ext .= ' %R.ist %R.xdy';

add_cus_dep('dot', 'pdf', 0, 'run_dot');
sub run_dot {
  if ( $silent ) {
    system "dot -Gcharset=latin1 -Tpdf -o'init[0].pdf' 'init[0].dot'";
  }
  else {
    system "dot -v -Gcharset=latin1 -Tpdf -o'init[0].pdf' 'init[0].dot'";
  };
  &cus_dep_require_primary_run;
}
