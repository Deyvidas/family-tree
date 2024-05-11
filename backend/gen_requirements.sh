REQUIREMENTS_PATH=${PWD}/requirements

if [ ! -d ${REQUIREMENTS_PATH} ];
then
    mkdir ${REQUIREMENTS_PATH}
fi

warnings=`poetry config warnings.export` &&
poetry config warnings.export false &&

poetry lock --no-update &&
poetry export --with test --without-hashes --without-urls | awk '{ print $1 }' FS=' ; ' > requirements/test_requirements.txt &&
poetry export --with prod --without-hashes --without-urls | awk '{ print $1 }' FS=' ; ' > requirements/prod_requirements.txt &&
poetry export --with dev  --without-hashes --without-urls | awk '{ print $1 }' FS=' ; ' > requirements/dev_requirements.txt &&

poetry config warnings.export $warnings