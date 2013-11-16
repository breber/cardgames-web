CARHUB_MOBILE=$(pwd)/../CarHubMobile/CarHubMobile
CARHUB_IOS=$(pwd)/../carhub-ios
LIB_VERSION=1.17.0-rc

# Generate the Java client library
endpointscfg.py get_client_lib java -o . api.CarHubApi

# Unzip the generated zip
mv carhub-v1.zip /tmp/CarHubApi.zip
pushd /tmp/
yes | unzip CarHubApi.zip
pushd carhub

# Remove existing Jars from the libs folder of Android app
rm $CARHUB_MOBILE/CarHub/libs/google-*
rm $CARHUB_MOBILE/CarHub/libs/gson-*
rm $CARHUB_MOBILE/CarHub/libs/jsr*

# Copy new jars to the Android app
cp libs/gson-*.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/jsr*.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/google-api-client-$LIB_VERSION.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/google-api-client-android-$LIB_VERSION.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/google-http-client-$LIB_VERSION.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/google-http-client-android-$LIB_VERSION.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/google-http-client-gson-$LIB_VERSION.jar $CARHUB_MOBILE/CarHub/libs/
cp libs/google-oauth-client-$LIB_VERSION.jar $CARHUB_MOBILE/CarHub/libs/

# Get the java files out of the generated Jar
mv *.jar car-hub-carhub.zip
unzip car-hub-carhub.zip

cp -R com/appspot/* $CARHUB_MOBILE/CarHub/src/main/java/com/appspot/

popd # carhub
popd # /tmp/

# Clean up after ourselves
rm /tmp/CarHubApi.zip
rm -rf /tmp/carhub

# Generate for iOS
if [ -d $CARHUB_IOS ]; then
    endpointscfg.py gen_discovery_doc -o . -f rpc api.CarHubApi

    svn checkout \
        http://google-api-objectivec-client.googlecode.com/svn/trunk/ \
        google-api-objectivec-client-read-only

    pushd google-api-objectivec-client-read-only/Source/Tools/ServiceGenerator/
    xcodebuild -project ServiceGenerator.xcodeproj
    popd
    ./google-api-objectivec-client-read-only/Source/Tools/ServiceGenerator/build/Release/ServiceGenerator \
        carhub-v1.discovery --outputDir $CARHUB_IOS/CarHubApi/

    rm -rf google-api-objectivec-client-read-only
fi
