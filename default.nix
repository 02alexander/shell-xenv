{stdenv, lib, python311}:
stdenv.mkDerivation {
  name = "shell-xenv";
  src = ./.;
  buildInputs = [
    python311
  ];
  installPhase = ''
    mkdir -p $out/bin
    mv shell-xenv.py $out/bin/shell-xenv
  '';
}
