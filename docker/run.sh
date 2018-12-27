#!/bin/bash

pytest_args=$1

gat_dir=$(cd ../ && pwd)
image_name_full='gat-tests:latest'

test_env='test'
driver='chrome-headless'

pytest_command="pytest ${pytest_args} --reruns 3"

docker run --rm \
    -e TESTS_CONFIG_ENV_FILENAME=${test_env} \
    -e DRIVER=${driver} \
    -v ${gat_dir}:/usr/src/gat \
    -it ${image_name_full} \
    /bin/bash -c "/usr/src/cleanup_cache.sh && ${pytest_command}"

source cleanup_local_cache.sh