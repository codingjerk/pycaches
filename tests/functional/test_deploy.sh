#!/usr/bin/env sh

# === Setup ===
version=$(grep -oP 'version="\K[^"]+' setup.py)
python3 -m venv .venv_test_deploy
. .venv_test_deploy/bin/activate

clean_exit() {
  rm -rf .venv_test_deploy
  exit 1
}

# === Check if pycaches installable ===
pip3 install --upgrade "pycaches==$version"
ret=$?
if [ $ret -ne 0 ]; then
  echo "Error: unable to install pycaches version $version"
  clean_exit 1
fi

# === Check if it is importable ===
yes | python3 -c "import pycaches; help(pycaches.Cache); help(pycaches.cache)"
ret=$?
if [ $ret -ne 0 ]; then
  echo "Error: unable to correctly import pycaches"
  clean_exit 2
fi

clean_exit 0
