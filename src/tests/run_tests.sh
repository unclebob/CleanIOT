REPO_CODE_ROOT=~/repos/bitbucket/clean-iot/src
PYTHONPATH+=$REPO_CODE_ROOT/hub
PYTHONPATH+=:$REPO_CODE_ROOT/snappyImages

pushd $REPO_CODE_ROOT/tests

python -m unittest discover

popd